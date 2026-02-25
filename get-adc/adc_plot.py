import matplotlib.pyplot as plot

def plot_vol_vs_time(time, vol, max_vol):
    plot.figure(figsize = (10, 6))
    plot.plot(time, vol)
    plot.xlabel("Time, s")
    plot.ylabel("Voltage, V")
    plot.grid()
    plot.show()