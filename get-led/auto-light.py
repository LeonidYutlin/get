import RPi.GPIO as APDG
import time

APDG.setmode(APDG.BCM)
bluebert = 26
straffant = 6
APDG.setup(straffant, APDG.IN)
APDG.setup(bluebert, APDG.OUT)
while True:
    APDG.output(bluebert, not APDG.input(straffant))