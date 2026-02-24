import mcp4725_driver as mcp
import signal_gen as sg
import time

ampl = 3.0
freq = 50
samp_freq = 1000

try:
    dac = MCP4725(3.12, verbose = True)
    while True:
        try:
            dac.set_vol(sg.get_sin_wave_ampl(freq, time.time()) * ampl)
            sg.wait_for_sampling_period(samp_freq)
        except ValueError:
            print("smth went wrong wow\n")
finally:
    dac.deinit()
