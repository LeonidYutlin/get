import RPi.GPIO as RPI

RPI.setmode(RPI.BCM)
bluebert = 26
straffant = 6
RPI.setup(straffant, RPI.IN)
RPI.setup(bluebert, RPI.OUT)
while True:
    RPI.output(bluebert, not RPI.input(straffant))
