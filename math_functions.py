import numpy as np
from scipy.spatial import distance as dist


# return rectangle features
def rect_to_bb(rect):
    x = rect.left()
    y = rect.top()
    w = rect.right() - x
    h = rect.bottom() - y
    return (x, y, w, h)


# reformat shape to numpy matrix
def shape_to_np(shape, dtype="int"):
    coords = np.zeros((68, 2), dtype=dtype)

    for i in range(0, 68):
        coords[i] = (shape.part(i).x, shape.part(i).y)
    return coords


# calculate the eye ratio
def eye_ratio(eye):
    A = dist.euclidean(eye[1], eye[5])
    B = dist.euclidean(eye[2], eye[4])
    C = dist.euclidean(eye[0], eye[3])

    EAR = (A + B) / (2.0 * C)
    return EAR


# calculate the center of eye
def eye_center(eye):
    center = (int(((eye[0, 0] + eye[3, 0]) / 2)), int(((eye[2, 1] + eye[4, 1]) / 2)))
    return center


# calculate the center of two points
def two_points_center(P1, P2):
    TPC = (int((P1[0] + P2[0]) / 2), int((P1[1] + P2[1]) / 2))
    return TPC
