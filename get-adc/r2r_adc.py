import RPi.GPIO as GPIO
import time

class R2R_ADC:
    def __init__(self, drange, comp_time = 0.01, verbose = False):
        self.comp_time = comp_time
        self.range = drange
        self.verbose = verbose
        
        self.bits_gpio = [26, 20, 19, 16, 13, 12, 25, 11]
        self.comp_gpio = 21
        
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.bits_gpio, GPIO.OUT, initial = 0)
        GPIO.setup(self.comp_gpio, GPIO.IN)
        
    def deinit(self):
        GPIO.output(self.bits_gpio, 0)
        GPIO.cleanup()
    
    def num_2_dac(self, number):
        GPIO.output(self.bits_gpio, [int(element) for element in bin(number)[2:].zfill(8)])
        
    def sequential_counting_adc(self):
        for i in range(256):
            self.num_2_dac(i)
            time.sleep(self.comp_time)
            if GPIO.input(self.comp_gpio) or i == 255:
                return i * self.range / 255
    
    def get_sc_vol(self):
        print(f"Voltage is: {self.sequential_counting_adc()}\n")
        

if __name__ == "__main__":
    try:
        adc = R2R_ADC(3.183)
        
        while True:
            try:
                adc.get_sc_vol()
            except ValueError:
                print("Incorrect input! Try again\n")
    finally:
        adc.deinit()