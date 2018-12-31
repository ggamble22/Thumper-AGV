
import wiringpi as wpi
from pwm import PWM

class G2MotorShield():
  #pin definitions
  _dir=0
  _cs=0
  _pwm=None
  _fault=0
  _sleep=0 #inverted sleep function, pull high to enable motor


  speed=0

  def __init__(self, dir_pin, pwm, fault, sleep):
      self._pwm = PWM(pwm)
      self._dir = dir_pin
      self._fault = fault
      self._sleep = sleep

      wpi.pinMode(self._dir, wpi.OUTPUT) #set to output
      wpi.pinMode(self._fault, wpi.INPUT) #set as input
      wpi.pinMode(self._sleep, wpi.OUTPUT)
      wpi.digitalWrite(self._sleep, wpi.HIGH)



  def set_speed(self, speed):
    reverse = False

    if speed < 0:
      speed = -speed;  #Make speed a positive quantity
      wpi.digitalWrite(self._dir, wpi.LOW)
    else:
      wpi.digitalWrite(self._dir, wpi.HIGH)

    if speed > 1.0:  # Max PWM dutycycle
      speed = 1.0

    self._pwm.duty_float(speed)

  def brake(self):
    self.set_speed(0)

  def getFault(self):
    return not wpi.digitalRead(_fault)


class DualG2MotorShield():
  _motor1=None
  _motor2=None

  def __init__(self, dir_pin1, pwm1, fault1, sleep1, dir_pin2, pwm2, fault2, sleep2):
    wpi.wiringPiSetup()
    self._motor1 = G2MotorShield(dir_pin1, pwm1, fault1, sleep1)
    self._motor2 = G2MotorShield(dir_pin2, pwm2, fault2, sleep2)

#et speed for motor 1, speed is a number betwenn -400 and 400
  def setM1Speed(self, speed):
    self._motor1.set_speed(speed)

# Set speed for motor 2, speed is a number betwenn -400 and 400
  def setM2Speed(self, speed):
    self._motor2.set_speed(speed)  


# Set speed for motor 1 and 2
  def setSpeeds(self, m1Speed, m2Speed):
    self.setM1Speed(m1Speed);
    self.setM2Speed(m2Speed);

# Brake motor 1, brake is a number between 0 and 400
  def setM1Brake(self):
    self._motor1.brake()

# Brake motor 2, brake is a number between 0 and 400
  def setM2Brake(self):
    self._motor2.brake()

# Brake motor 1 and 2, brake is a number between 0 and 400
  def setBrakes(self):
    self.setM1Brake();
    self.setM2Brake();

  def getMotorsCurrentMilliamps(self):
    return(self._motor.selfgetM1CurrentMilliamps(), )

# Return error status for motor 1
  def getM1Fault(self):
    return self._motor1.getFault()

# Return error status for motor 2
  def getM2Fault(self):
    return self._motor2.getFault()

  def getFaults(self):
    return (self._motor1.getFault(), self._motor2.getFault())
