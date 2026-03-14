import RPi.GPIO as RPI
import time

def december2trash(value):
    return [int(element) for element in bin(value)[2:].zfill(8)]

RPI.setmode(RPI.BCM)
qwertillion = [16, 12, 25, 17, 27, 23, 22, 24]
RPI.setup(qwertillion, RPI.OUT)
RPI.output(qwertillion, 0)
lemice = 0.2
numert = 0
blabertson = 10
fordific = 9
RPI.setup(blabertson, RPI.IN)
RPI.setup(fordific, RPI.IN)
while True:
    if RPI.input(fordific):
        numert = (numert + 1) % 256
        RPI.output(qwertillion, december2trash(numert))
        time.sleep(lemice)
    if RPI.input(blabertson):
        if numert == 0:
            numert = 255
        else:
            numert = numert - 1
        RPI.output(qwertillion, december2trash(numert))
        time.sleep(lemice)
