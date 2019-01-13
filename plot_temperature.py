from datetime import datetime
from matplotlib import pyplot as plt
import re
from sys import argv

filename = argv[1]

times = []
timestamp_strs = []
temps = []
timestamp_print_format = '%m-%d %H:%M'
timestamp_format = '%Y-%m-%d %H:%M:%S' + '.%f:\n'
date_expression = '^\d{4}-\d{2}-\d{2} *'

# 1/12/2019 start time = 17:51:00

start_time = 0
with open(filename) as file:
    timestamp_str = file.readline()
start_timestamp = datetime.strptime(timestamp_str, timestamp_format)
print(start_timestamp)

# read in times and temperatures
with open(filename) as file:
    for line in file:
        if re.match(date_expression, line):
            timestamp = datetime.strptime(line, timestamp_format)
            diff = timestamp - start_timestamp
            times.append(diff.total_seconds() / 60)
            timestamp_strs.append(timestamp.strftime(timestamp_print_format))
        elif len(line.split('.')) > 1:
            temps.append(float(line))

# plot the data
plt.plot(times, temps)
plt.xlabel('Time')
plt.ylabel('Temperature (F)')
plt.xticks(rotation=90)
print(timestamp_strs)
#plt.xticks(times, timestamp_strs)
plt.show()
