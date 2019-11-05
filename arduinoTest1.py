# -*- coding: utf-8 -\*-
"""
Created on Fri Nov  1 14:01:19 2019

@author: rwszy
"""

import serial
import tkinter as tk

class App:
    def __init__(self, master):
        frame = tk.Frame(master)
        frame.pack()
        
        # COM PORT 
        tk.Label(frame, text='COM PORT: ').grid(row=0, column=0)
        self.com_var = tk.StringVar()
        tk.Entry(frame, textvariable=self.com_var).grid(row=0, column=1)
        self.com_button = tk.Button(frame, text='SET COM PORT', command=self.set_com)
        self.com_button.grid(row=1, columnspan=2)
        self.com_response = tk.StringVar()
        tk.Label(frame, textvariable=self.com_response).grid(row=2, columnspan=2)
        
        # LED ON/OFF
        self.on_button = tk.Button(frame, text='ON ', command=self.led_on)
        self.on_button.grid(row=3, column=0)
        self.off_button = tk.Button(frame, text='OFF', command=self.led_off)
        self.off_button.grid(row=3, column=1)

    def set_com(self):
        self.com_port = self.com_var.get()
        self.arduinoData = serial.Serial(f'{self.com_port}', 9600)
        self.com_response.set('COM PORT has been set')

    def led_on(self):
        self.arduinoData.write(b'1')    
    def led_off(self):
        self.arduinoData.write(b'0')
 
root = tk.Tk()
root.geometry('300x100')
root.wm_title('Arduino Controller')  
app = App(root)
root.mainloop()