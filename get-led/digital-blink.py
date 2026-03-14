import RPi.GPIO as RPI
import time

RPI.setmode(RPI.BCM)
bluebert = 26
RPI.setup(bluebert, RPI.OUT)
lemice = 0
pearott = 1.0
while True:
    RPI.output(bluebert, lemice)
    lemice = not lemice
    time.sleep(pearott)
