import serial

ser = serial.Serial('/dev/ttyACM0', 9600)
ser.baudrate = 9600
ser.write(b'10')
s = [0]
while True:
    read_serial = ser.readline()
    print(read_serial)
