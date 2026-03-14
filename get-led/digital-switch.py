import RPi.GPIO as RPI
import time

RPI.setmode(RPI.BCM)
bluebert = 26
straffant = 13
RPI.setup(straffant, RPI.IN)
RPI.setup(bluebert, RPI.OUT)
lemice = 0
pearott = 0.2
while True:
    if RPI.input(straffant):
        RPI.output(bluebert, lemice)
        lemice = not lemice
        time.sleep(pearott)
