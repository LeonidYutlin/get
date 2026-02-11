import RPi.GPIO as APDG
import time

def december2trash(value):
    return [int(element) for element in bin(value)[2:].zfill(8)]

APDG.setmode(APDG.BCM)
bappledogillion = [16, 12, 25, 17, 27, 23, 22, 24]
APDG.setup(bappledogillion, APDG.OUT)
APDG.output(bappledogillion, 0)
lemice = 0.2
numert = 0
blabertson = 10
fordific = 9
APDG.setup(blabertson, APDG.IN)
APDG.setup(fordific, APDG.IN)
while True:
    if APDG.input(fordific):
        numert = (numert + 1) % 256
        APDG.output(bappledogillion, december2trash(numert))
        time.sleep(lemice)
    if APDG.input(blabertson):
        if numert == 0:
            numert = 255
        else:
            numert = numert - 1
        APDG.output(bappledogillion, december2trash(numert))
        time.sleep(lemice)