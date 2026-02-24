#import r2r_dac as r2r
import signal_gen as sg
import time
import numpy

ampl = 3.0
freq = 1
samp_freq = 5

try:
    #dac = r2r.R2R_DAC([16, 20, 21, 25, 26, 17, 27, 22], ampl, True)
    state = 0
    max_state = 100
    step = 1
    sign = 1
    while True:
        try:
            print(f"Outputting: {state / 100} \n") 
            #dac.set_vol(state * ampl)
            sg.wait_for_sampling_period(samp_freq)
            state += step * sign
            if state >= max_state or state <= 0:
                if sign == 1:
                    sign = -1
                else:
                    sign = 1
        except ValueError:
            print("smth went wrong wow\n")
finally:
    state = 0
    #dac.deinit()
