import mcp4725_driver as mcp
import signal_gen as sg
import time

ampl = 2.0
freq = 1
samp_freq = 200

try:
    dac = mcp.MCP4725(3.12, verbose = True)
    state = 0
    max_state = 100
    step = 1
    sign = 1
    while True:
        try:
            dac.set_vol(state * ampl / max_state)
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
    dac.deinit()
