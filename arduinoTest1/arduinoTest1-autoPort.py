# -*- coding: utf-8 -\*-
"""
Created on Fri Nov  1 14:01:19 2019

@author: rwszy
"""

import serial
import tkinter as tk
from time import sleep

class App:
    def __init__(self, master):
        frame = tk.Frame(master)
        frame.pack()

        self.arduinoData = serial.Serial('/dev/cu.usbmodem142101', 9600, timeout=0.5)
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
        self.arduinoData.write(b'1')
        self.status_report.set(self.arduinoData.read(1))    
    def led_off(self):
        self.arduinoData.write(b'0')
        self.status_report.set('off')  
 
root = tk.Tk()
root.geometry('300x150')
root.wm_title('Arduino Controller')  
app = App(root)
root.mainloop()