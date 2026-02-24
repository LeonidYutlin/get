import numpy
import time

def get_sin_wave_ampl(freq, time):
    return (numpy.sin(2 * numpy.pi * freq * time) + 1) / 2

def wait_for_sampling_period(sampling_freq):
    time.sleep(1/sampling_freq)