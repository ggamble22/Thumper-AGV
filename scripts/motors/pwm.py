
import math 
import os

class PWM():
    _dir = None
    _pin = None
    _freq = None
    _duty = 0

    def __init__(self, pin, freq=100000, pwm_dir='/sys/devices/pwm-ctrl', start_duty=0):        

        if pin == 33:
            self._pin = 0
        elif pin ==  19:
            self._pin = 1
        else:
            self._pin = pin

        self._freq = freq
        self._dir = pwm_dir
        
        self.freq(self._freq)
        self.duty(0)
        self.enable()
    

    def close(self):
        self.disable()

    def write(self, path, value):
        with open(path, 'w') as f:
            f.write(str(value))

    def duty(self, duty):
        path = f'{self._dir}/duty{self._pin}'

        if duty>=0 and duty<1024:
            self.write(path, duty)

    def duty_pct(self, duty):
        path = f'{self._dir}/duty{self._pin}'

        if duty>=0 and duty<=100:
            duty = (duty * (1023) / (100))

            duty = math.floor(duty)
            self.write(path, duty)

    def duty_float(self, duty):
        path = f'{self._dir}/duty{self._pin}'

        if duty>=0 and duty<=1:
            duty = duty * 1023

            duty = math.floor(duty)
            self.write(path, duty)


    def enable(self):
        path = f'{self._dir}/enable{self._pin}'
        val = 1
        self.write(path,val)

    def disable(self):
        path = f'{self._dir}/enable{self._pin}'
        val = 0
        self.write(path,val)

    def freq(self, freq):
        self._freq = freq
        path = f'{self._dir}/freq{self._pin}'
        self.write(path, self._freq)


