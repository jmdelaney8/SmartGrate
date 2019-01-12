import serial
import datetime as dt
import sys

device = sys.argv[1]
if device is None:
    device = '/dev/ttyACM0'

ser = serial.Serial(device, 9600)
ser.baudrate = 9600
ser.write(b'10')
s = [0]
while True:
    if ser.in_waiting > 0:
        read_serial = ser.readline()
        print('{}:').format(dt.datetime.now())
        print(read_serial)
