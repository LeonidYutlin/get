import r2r_adc as r2r
import adc_plot as plot
import time

max_vol = 3.3
r2r = r2r.R2R_ADC(max_vol)
vols = []
ts = []
duration = 5.0

if __name__ == "__main__":
    try:
        t = time.time()
        while time.time() - t <= duration:
            vols.append(r2r.sequential_counting_adc())
            ts.append(time.time() - t)
        plot.plot_vol_vs_time(ts, vols, max_vol)
    finally:
        r2r.deinit()