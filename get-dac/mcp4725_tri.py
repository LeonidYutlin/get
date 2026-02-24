import mcp4725_driver as mcp
import signal_gen as sg
import time

ampl = 3.0
freq = 50
samp_freq = 1000

try:
    #dac = mcp.MCP4725(3.12, verbose = True)
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
