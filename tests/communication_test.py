import serial

with serial.Serial('/dev/cu.usbmodem141101', 9600) as ser:
	ser.readline()
	# print(x.decode('utf-8'))
	
	ser.write("45100$".encode())
	
	ser.close()