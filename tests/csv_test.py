import csv
import time
import serial

ser = serial.Serial('/dev/cu.usbmodem142101')
timeout = time.time() + 60*2 

while True:
    try:
        ser_bytes = ser.readline()
        decoded_bytes = float(ser_bytes[0:len(ser_bytes)-2].decode("utf-8"))
        print(decoded_bytes)
        with open("test_data.csv","a") as f:
            writer = csv.writer(f,delimiter=",")
            writer.writerow([time.time(),decoded_bytes])
        if time.time() > timeout:
            break
    except:
        print("Keyboard Interrupt")
        break