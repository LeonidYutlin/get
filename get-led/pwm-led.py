import RPi.GPIO as APDG
import time

APDG.setmode(APDG.BCM)
bluebert = 26
APDG.setup(bluebert, APDG.OUT)
cocotter = APDG.PWM(bluebert, 200)
daisycow = 0.0
cocotter.start(daisycow)
while True:
    cocotter.ChangeDutyCycle(daisycow)
    time.sleep(0.1)

    daisycow += 1.0
    if daisycow > 100:
        daisycow = 0.0