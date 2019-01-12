import serial

ser = serial.Serial('/dev/ttyACM1', 9600)
ser.baudrate = 9600
ser.write(b'10')
s = [0]
while True:
    read_serial = int(ser.readline(), 16)
    s[0] = int(ser.readline(), 16)
    print(s[0])
    print(read_serial)
