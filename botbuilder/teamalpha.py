#!/usr/bin/env pybricks-micropython
from pybricks import ev3brick as brick
from pybricks.tools import print, wait, StopWatch
from pybricks.parameters import (Port, SoundFile, Button, ImageFile, Align)
from botbuilder import robot

 #Ramp
def Ramp():
    robot.GoStraight(12,150)
    robot.FollowLine(19,100)
    robot.GoStraight(7,150)
    robot.TurnTo(-110,100)
    robot.GoTowards(41,-110,150)

def Crane():
   robot.gyro.reset_angle(-90)
   robot.GoTowards(26.5,-90,150)
   robot.GoTowards(2.5,-90,50)
   robot.GoBackTowards(12,-90,150)
   robot.RealStop()
   #Go to the next lever
   robot.TurnTo(0,150)
   robot.GoTowards(4,0,150)
   robot.RealStop()
   robot.TurnTo(-90,150)
   robot.GoTowards(3,-90,100)
   robot.GoTowards(2,-90,28)
   robot.GoBack(0.5,50)
   robot.RealStop()
   wait(500)
   #Do multiple lifts for different enviroments
   robot.MoveMotor(110, 400, True)
   robot.MoveMotor(120, 400, True)
   robot.MoveMotor(130, 400, True)
   robot.MoveMotor(140, 400, True)
   robot.MoveMotor(150, 400, False)
   wait(500)
   robot.MoveMotor(-150, 400, False)
   robot.RealStop()

   #It's time to go back!
   robot.GoBack(23, 200)
   robot.TurnRight(90, 200)
   robot.GoBack(30, 200)
   robot.realStop()
