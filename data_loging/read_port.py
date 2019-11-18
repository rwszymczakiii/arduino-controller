import serial

port = '/dev/cu.usbmodem142101'
ser = serial.Serial(port,9600)

while 1:
    data = ser.read().decode('utf-8')
    print(data)