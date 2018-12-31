#!/usr/bin/env python
import rospy
from sensor_msgs.msg import Joy

# 5   Motor 1 FLT Fault indicator: When the driver channel is functioning normally, this pin should be pulled high by the Raspberry Pi. In the event of a driver fault, FLT is driven low. See below for details.
# 6   Motor 2 FLT

# 12  Motor 1 PWM Motor speed input: A PWM (pulse-width modulation) signal on this pin corresponds to a PWM output on the corresponding channel’s motor outputs. When this pin is low, the motor brakes low. When it is high, the motor is on. The maximum allowed PWM frequency is 100 kHz.
# 13  Motor 2 PWM

# 22  Motor 1 SLP Inverted sleep input: This pin is pulled low by default, putting the motor driver channel into a low-current sleep mode and disabling the motor outputs (setting them to high impedance). SLP must be driven high to enable the motor channel.
# 23  Motor 2 SLP

# 24  Motor 1 DIR Motor direction input: When DIR is low, motor current flows from output A to output B; when DIR is high, current flows from B to A.
# 25  Motor 2 DIR

m1_fault = 21
m2_fault = 22

m1_pwm = 33
m2_pwm = 19

m1_slp = 3
m2_slp = 4

m1_dir = 5
m2_dir = 11

motors = G2MotorShield(, m1_dir, m1_pwm, m1_fault, m1_slp, m2_dir, m2_pwm, m2_fault, m2_slp)


def callback(data): 
    yaw = data.axes[0]/2 + 0.5
    throttle = data.axes[1]/2 + 0.5
    print 'Throttle: {0}, Yaw: {1}'.format(throttle, yaw)
    motosrs.setSpeeds(yaw, throttle)

def listener():
    rospy.init_node('motor_controller')
    rospy.Subscriber("joy", Joy, callback)
    rospy.spin()

if __name__ == '__main__':
    listener()
