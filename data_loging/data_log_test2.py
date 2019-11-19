# -*- coding: utf-8 -\*-
"""
Created on Fri Nov  1 14:01:19 2019

@author: rwszy
"""

import serial
import tkinter as tk
from time import sleep
import threading
import data_handler as dh


class App:
    def __init__(self, master):
        frame = tk.Frame(master)
        frame.pack()

        self.arduinoData = serial.Serial('/dev/cu.usbmodem142101', 9600, timeout=1)
        sleep(0.5)
        
        # LED ON/OFF
        self.on_button = tk.Button(frame, text='ON ', command=self.led_on)
        self.on_button.grid(row=3, column=0)
        self.off_button = tk.Button(frame, text='OFF', command=self.led_off)
        self.off_button.grid(row=3, column=1)

        # LOG
        self.status_report = tk.StringVar()
        tk.Label(frame, textvariable=self.status_report).grid(row=4, columnspan=2)     

    def led_on(self):
        self.status_report.set('on')
        sleep(0.2)
        self.arduinoData.write(b'1')
        def print_serial():
            data_list = []
            while 1:
                try:
                    data = self.arduinoData.read().decode('utf-8')
                    data_list.append(data)
                    print(data_list)
                    return data_list
                except:
                    converted_data = dh.convert_data(data_list)
                    dh.data_to_csv(converted_data)
        print_serial = threading.Thread(target=print_serial)
        print_serial.start()

    def led_off(self):
        self.status_report.set('off')
        self.arduinoData.close()
        self.arduinoData.open()
 
root = tk.Tk()
root.geometry('300x150')
root.wm_title('Arduino Controller')  
app = App(root)
root.mainloop()