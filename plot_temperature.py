from datetime import time as dt_time
from matplotlib import pyplot as plt
from sys import argv

filename = argv[1]

times = []
temps = []

# read in times and temperatures
with open(filename) as file:
    for line in file:
        if '2019' in line:
            # TODO: read in date as well
            time = line.split()
            time = time.split(':')
            time = dt_time(int(time[0]), int(time[1]))
            times.append(time)
        else:
            temps.append(float(temps))

# plot the data
plt.plot(times, temps)
plt.show()
