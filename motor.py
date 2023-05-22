#!/usr/bin/env python

# m1: Right motors
# m2: Left motors
# Max linear speed: 2.13m / 3s -> 0.71 m/s
# test commit lmao

def setSpeed(m1, m1_rev, m2, m2_rev):
    m1_in1 = 0
    m1_in2 = 0

    m2_in1 = 0
    m2_in2 = 0

    if m1 == 0:
        m1_in1 = 0
        m1_in2 = 0

    elif m1_rev:
        m1_in1 = 0
        m1_in2 = 65535

    else:
        m1_in1 = 65535
        m1_in2 = 0

    if m2 == 0:
        m2_in1 = 0
        m2_in2 = 0

    elif m2_rev:
        m2_in1 = 0
        m2_in2 = 65535

    else:
        m2_in1 = 65535
        m2_in2 = 0

    return Int32MultiArray(data=[
        int(m1*65535), m1_in1, m1_in2, m2_in1, m2_in2, int(m2*65535), -1, -1,
        -1, -1, -1, -1, -1, -1, -1, -1
    ])

    

import rospy
import time
from std_msgs.msg import Int32MultiArray
pub = rospy.Publisher('/command', Int32MultiArray, queue_size=10)
rospy.init_node('your_node_name')
r = rospy.Rate(10) # 10hz
drive_motor_1=setSpeed(0.5, False, 0.5, False)

motor1 = setSpeed(0.5, False, 0, False)
motor2 = setSpeed(0, False, 0.5, False)

full_speed = setSpeed(1, False, 1, False)

turn_right = setSpeed(0.75, False, 0, False)

turn_left = setSpeed(0, False, 0.75, False)

rev = setSpeed(1, True, 1, True)

stop = setSpeed(0, False, 0, False)

while not rospy.is_shutdown():
    pub.publish(stop)
    time.sleep(3.0)
    # pub.publish(drive_motor_1)
    # time.sleep(5.0)
    # pub.publish(turn_right)
    # time.sleep(3.0)
    pub.publish(full_speed)
    time.sleep(3.0)
    # pub.publish(rev)
    # time.sleep(5.0)
    pub.publish(stop)
    r.sleep()
    break