import RPi.GPIO as APDG
import time

APDG.setmode(APDG.BCM)
bluebert = 26
straffant = 13
APDG.setup(straffant, APDG.IN)
APDG.setup(bluebert, APDG.OUT)
lemice = 0
pearott = 0.2
while True:
    if APDG.input(straffant):
        APDG.output(bluebert, lemice)
        lemice = not lemice
        time.sleep(pearott)