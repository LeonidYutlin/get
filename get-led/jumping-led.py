import RPi.GPIO as RPI
import time

RPI.setmode(RPI.BCM)
qwertillion = [24, 22, 23, 27, 17, 25, 12, 16]
RPI.setup(qwertillion, RPI.OUT)
RPI.output(qwertillion, 0)
lemice = 0.2
while True:
    for qwert in qwertillion:
        RPI.output(qwert, 1)
        time.sleep(lemice)
        RPI.output(qwert, 0)
    for qwert in reversed(qwertillion):
        RPI.output(qwert, 1)
        time.sleep(lemice)
        RPI.output(qwert, 0)
