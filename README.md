# The mirror

The mirror is the project of robot that repeat human facial expression. 

## How it works?

Image processing algorithms were used in the project.
A face is detected on the image frame taken from the camera and then face landmarks are predicted.
Using face landmarks gives the possibility to calculate the smile level and detect whether the presion is blinking. 
This informations are processed using simple trigonometric algorithms. 
Once the data is processed, they are then encoded into a frame that can be sent to stm via serial communication.


## Mechanical part
Robot was designed using Autodesc Inventor. Then the neccesery parts were 3D printed or cut from plexiglass using high power laser. 
The movement of all parts is carried out using servos that are controlled by STM32F103C8T6 (the "Blue pill").  

## Presentation

Finished project: https://youtu.be/uIIF3xdDFeE <br>
Servo control using smile: https://youtu.be/Zro1Sdtm5g8

## License
[MIT](https://choosealicense.com/licenses/mit/)
