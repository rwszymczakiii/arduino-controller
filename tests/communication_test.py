import serial

with serial.Serial('com6', 9600) as ser:
	x = ser.readline()
	print(x.decode('utf-8'))
	
	ser.write("123456789$".encode())

	y = ser.readline()
	print(y.decode('utf-8'))

	ser.close()

def convert_code(code):
	while len(code) < 3:	
		code = '0' + code
	return code
x = "1"
y = "22"
z = "333"
x = convert_code(x)
y = convert_code(y)
z = convert_code(z)
print(x)
print(y)
print(z)