#!/usr/bin/env python
import rospy
from sensor_msgs.msg import Joy
from G2MotorShield import DualG2MotorShield

m1_fault = 21
m2_fault = 22

m1_pwm = 1
m2_pwm = 0

m1_slp = 3
m2_slp = 4

m1_dir = 5
m2_dir = 6

motors = DualG2MotorShield(m1_dir, m1_pwm, m1_fault, m1_slp, m2_dir, m2_pwm, m2_fault, m2_slp)


def manual_control_callback(data): 
    '''!
        \brief Callback method for receiving a joy message from the joy_node
         with a connected controller
    '''
    yaw = float(data.axes[0])
    throttle = float(data.axes[1])
    print 'Throttle: {0}, Yaw: {1}'.format(throttle, yaw)
    motors.setSpeeds(yaw, throttle)

def listener():
    rospy.init_node('motor_controller')
    rospy.Subscriber("joy", Joy, manual_control_callback)
    rospy.spin()

if __name__ == '__main__':
    listener()
