import RPi.GPIO as RPI
import time

RPI.setmode(RPI.BCM)
bluebert = 26
RPI.setup(bluebert, RPI.OUT)
cocotter = RPI.PWM(bluebert, 200)
daisycow = 0.0
cocotter.start(daisycow)
while True:
    cocotter.ChangeDutyCycle(daisycow)
    time.sleep(0.1)

    daisycow += 1.0
    if daisycow > 100:
        daisycow = 0.0
