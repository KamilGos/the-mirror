import cv2 as cv
from scipy.spatial import distance as dist
import dlib
import math_functions
import math
import serial

CAM_HOLDER = 3
EYE_THRESH = 0.19
EYE_AR_CONSEC_FRAMES = 3
AR_SIZEX = 500
AR_SIZEY = 500
X_RESIZE = 1
Y_RESIZE = 1
FACE_DETECTED = 0

PORT = 'COM10'
SPEED = 9600
DATA2SEND = 0

USE_FILTRATION = 0
USE_COMM = 0

# init serial communication
if USE_COMM == 1:
    ser = serial.Serial()
    ser.port = PORT
    ser.baudrate = SPEED
    if(ser.isOpen() == False):
        ser.open()
        print("Serial open")
    else:
        print("Serial is already open")
    if(ser.isOpen() == False):
        print("I cant open serial {}".format(PORT))
    print("Serial id: {}".format(ser))

# face detector and shape predictor initialization
detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor('shape_predictor_68_face_landmarks.dat')

# open camera
cap = cv.VideoCapture(CAM_HOLDER)
if(cap.isOpened() == False):
    print("Unable to connect to camera")
    exit()
else:
    print("Connected to camera")

##  main loop
while(True):
    ret, frame = cap.read()
    clean_frame = frame
    frame = cv.cvtColor(frame, cv.COLOR_BGR2HSV)
    frame_split = cv.split(frame)
    frame = frame_split[2]
    frame = cv.resize(frame,(0,0), fx=X_RESIZE, fy=Y_RESIZE)

    rects = detector(frame,1)
    FACE0 = 0
    if len(rects) != 0:
        for(i, rect) in enumerate(rects):
            FACE0 = rects[0]

    # if face detected
    if FACE0 != 0:
        FACE_DETECTED = 1
        rect=FACE0
        (x,y,w,h) = math_functions.rect_to_bb(rect)
        face_frame = frame[y:y+h, x:x+w]
        face_frame = cv.resize(face_frame, (AR_SIZEX,AR_SIZEY))
        shape = predictor(face_frame, dlib.rectangle(0,0,AR_SIZEX,AR_SIZEY))
        shape = math_functions.shape_to_np(shape)

        for (x, y) in shape:
            cv.circle(face_frame, (x,y), 4, (0, 0, 0), -1)

        leftEye = shape[36:42]
        rightEye = shape[42:48]
        leftEC = math_functions.eye_center(leftEye)
        rightEC = math_functions.eye_center(rightEye)
        cv.circle(face_frame, leftEC, 5, (255, 255, 255), -1)
        cv.circle(face_frame, rightEC, 5, (255, 255, 255), -1)
        Rotation_point = math_functions.two_points_center(leftEC, rightEC)
        Rotation_angle = math.asin(dist.euclidean(rightEC, (rightEC[0],leftEC[1])) / (dist.euclidean(leftEC,rightEC)))
        if rightEC[1] >= leftEC[1]:
            Rotation_angle = (Rotation_angle*180)/(math.pi)
        else:
            Rotation_angle = (Rotation_angle * 180) /(-(math.pi))

        Rotation_matrix= cv.getRotationMatrix2D(Rotation_point,Rotation_angle,1)
        face_frame_AR = cv.warpAffine(face_frame, Rotation_matrix, (AR_SIZEX,AR_SIZEY))
        cv.imshow("face_frame", face_frame)

        # image filtration
        if USE_FILTRATION == 1:
            face_frame_AR = cv.GaussianBlur(face_frame_AR, (3,3), 0)
            clahe = cv.createCLAHE(clipLimit=1.0, tileGridSize=(5,5))
            face_frame_AR = clahe.apply(face_frame_AR)
            face_frame_AR = cv.equalizeHist(face_frame_AR)

        # get the face shape (points)
        shape = predictor(face_frame_AR, dlib.rectangle(0,0,AR_SIZEX,AR_SIZEY))
        shape = math_functions.shape_to_np(shape)

        # smile detection
        ALFA = math.atan( dist.euclidean(shape[48], (shape[48,0],shape[50,1])) /
                          dist.euclidean(shape[50], (shape[48,0],shape[50,1])))
        ALFA = (ALFA*180)/math.pi

        BETA = math.atan( dist.euclidean(shape[52], (shape[52,0],shape[54,1])) /
                          dist.euclidean(shape[54], shape[52]))
        BETA = (BETA*180)/math.pi

        MEAN = (int(((ALFA+BETA)/2)*10))
        SMILE = MEAN

        cv.putText(face_frame_AR, "SR: {}".format(MEAN), (300, 30),
                   cv.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)

        # eye blink detection
        leftEye = shape[36:42]
        rightEye = shape[42:48]
        leftEAR = math_functions.eye_ratio(leftEye)
        rightEAR = math_functions.eye_ratio(rightEye)
        EAR = ((leftEAR + rightEAR) / 2 )
        cv.putText(face_frame_AR, "EAR: {:.2f}".format(EAR), (150, 30),
                   cv.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)

        # create data frame
        if USE_COMM == 1:
            if FACE_DETECTED == 1:
                if EAR < EYE_THRESH:
                    EAR_BYTE = 0
                else:
                    EAR_BYTE = 1

                if SMILE > 200:
                    SMILE = 200
                if SMILE < 50:
                    SMILE = 50

                if SMILE < 10:
                    DATA = '00' + str(SMILE)+str(EAR_BYTE)
                elif ((SMILE < 100) and (SMILE > 10)):
                    DATA = '0'  + str(SMILE)+str(EAR_BYTE)
                else:
                    DATA = str(SMILE)+str(EAR_BYTE)
                print("Send: {}".format(DATA))
                ser.write(DATA.encode())
            else:
                DATA = '0' + str(500)
                print("Send: {}".format(DATA))

                # write data to stm
                ser.write(DATA.encode())
        cv.imshow('face_frame_AR', face_frame_AR)
    else:
        print("No face detected")
        FACE_DETECTED = 0

    cv.imshow("clean_frame", clean_frame)

    if cv.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv.destroyAllWindows()
