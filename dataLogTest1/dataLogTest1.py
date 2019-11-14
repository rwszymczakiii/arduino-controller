import serial 
import time

arduinoData = serial.Serial('/dev/cu.usbmodem142101', 9600, timeout=1)
time.sleep(0.5)
arduinoData.write(b'1')