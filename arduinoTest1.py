# -*- coding: utf-8 -*-
"""
Created on Fri Nov  1 14:01:19 2019

@author: rwszy
"""

import serial
import tkinter as tk

arduinoData = serial.Serial('com3', 9600)

def led_on():
    arduinoData.write(b'1')
    
def led_off():
    arduinoData.write(b'0')
    
led_control_window = tk.Tk()

Button = tk.Button 

btn1 = Button(led_control_window, text="ON ", command=led_on)
btn2 = Button(led_control_window, text="OFF", command=led_off)

btn1.grid(row=0, column=0)
btn2.grid(row=1, column=0)

led_control_window.mainloop()

input("press enter to exit")