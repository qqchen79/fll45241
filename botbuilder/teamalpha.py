#!/usr/bin/env pybricks-micropython
from pybricks import ev3brick as brick
from pybricks.tools import print, wait, StopWatch
from pybricks.parameters import (Port, SoundFile, Button, ImageFile, Align)
from botbuilder import robot

# Ramp
def Ramp():
    robot.FollowLine(38,50)
    robot.TurnLeft(90,100)
    robot.FollowLine(41, 195)

def Crane():
   robot.gyro.reset_angle(-90)
   robot.GoTowards(23,-90,150)
   robot.GoTowards(2.5,-90,50)
   robot.GoBackTowards(12,-90,150)
   robot.TurnTo(0,150)
   robot.GoTowards(4,0,150)
   robot.TurnTo(-90,150)
   robot.GoTowards(3,-90,100)
   robot.GoTowards(2,-90,28)
   robot.GoBack(0.5,50)
   wait(500)
   robot.MoveMotor(110, 400, True)
   robot.MoveMotor(120, 400, True)
   robot.MoveMotor(130, 400, True)
   robot.MoveMotor(140, 400, True)
   robot.MoveMotor(150, 400, False)
   wait(500)
   robot.MoveMotor(-150, 400, False)
