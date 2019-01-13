from datetime import time as dt_time
from datetime import datetime
from matplotlib import pyplot as plt
import re
from sys import argv

filename = argv[1]

times = []
temps = []
date_format = "%H:%M"
date_expression = '^\d{4}-\d{2}-\d{2} *'

# 1/12/2019 start time = 17:51:00

start_time = 0
with open(filename) as file:
    start_time = file.readline()
start_time = start_time.split()
start_time = start_time[1].split(':')
date = datetime.today()
start_time = dt_time(hour=int(start_time[0]), minute=int(start_time[1]))
print(start_time)
start_time = date.combine(date, start_time)

# read in times and temperatures
with open(filename) as file:
    for line in file:
        if re.match(date_expression, line):
            # TODO: read in date as well
            time = line.split()
            time = time[1].split(':')
            time = dt_time(hour=int(time[0]), minute=int(time[1]))
            time = date.combine(date, time)
            diff = time - start_time
            times.append(diff.total_seconds() / 60)
        elif len(line.split('.')) > 1:
            temps.append(float(line))

# plot the data
plt.plot(times, temps)
plt.xlabel('Time')
plt.ylabel('Temperature (F)')
plt.xticks(rotation=90)
plt.show()
