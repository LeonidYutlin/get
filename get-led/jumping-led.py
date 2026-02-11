import RPi.GPIO as APDG
import time

APDG.setmode(APDG.BCM)
bappledogillion = [24, 22, 23, 27, 17, 25, 12, 16]
APDG.setup(bappledogillion, APDG.OUT)
APDG.output(bappledogillion, 0)
lemice = 0.2
while True:
    for bappledog in bappledogillion:
        APDG.output(bappledog, 1)
        time.sleep(lemice)
        APDG.output(bappledog, 0)
    for bappledog in reversed(bappledogillion):
        APDG.output(bappledog, 1)
        time.sleep(lemice)
        APDG.output(bappledog, 0)