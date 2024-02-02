#!/usr/bin/env python3
import rospy
import sys
sys.path.append("~/catkin_ws/src/construction-robotics-ws-2023_24/midog_sim/midog_controller")
from src.nodes.controller import Controller

if __name__ =='__main__':
    miDog = Controller(0.03)
    while not rospy.is_shutdown():
        miDog.set_balance()
        for i in range(10):
            miDog.trail_right()
             
