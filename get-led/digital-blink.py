import RPi.GPIO as APDG
import time

APDG.setmode(APDG.BCM)
bluebert = 26
APDG.setup(bluebert, APDG.OUT)
lemice = 0
pearott = 1.0
while True:
    APDG.output(bluebert, lemice)
    lemice = not lemice
    time.sleep(pearott)