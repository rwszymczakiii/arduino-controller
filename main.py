import serial
import tkinter as tk
from tkinter import messagebox
from time import sleep
import threading
try: 
    import data_handler as dh
except PermissionError:
    root = tk.Tk()
    root.withdraw()
    messagebox.showinfo('Permission Error', 'cannot write data log without appropriate permissions')

class App:
    def __init__(self, master):
        frame = tk.Frame(master)
        frame.pack()
        self.reading = False

        # COM PORT 
        tk.Label(frame, text='COM PORT: ').grid(row=0, column=0)
        self.com_var = tk.StringVar()
        tk.Entry(frame, textvariable=self.com_var).grid(row=0, column=1)
        self.com_button = tk.Button(frame, text='SET COM PORT', command=self.set_com)
        self.com_button.grid(row=1, columnspan=2)
        self.com_response = tk.StringVar()
        tk.Label(frame, textvariable=self.com_response).grid(row=2, columnspan=2)
        # VARS INPUT
        tk.Label(frame, text='CYCLES:         ').grid(row=3, column=0)
        self.cycles_var = tk.StringVar()
        tk.Entry(frame, textvariable=self.cycles_var).grid(row=3, column=1)
        tk.Label(frame, text='PUMPS:          ').grid(row=4, column=0)
        self.pumps_var = tk.StringVar()
        tk.Entry(frame, textvariable=self.pumps_var).grid(row=4, column=1)
        tk.Label(frame, text='PUFF TIME (s): ').grid(row=5, column=0)
        self.time_var = tk.StringVar()
        tk.Entry(frame, textvariable=self.time_var).grid(row=5, column=1)
        # START/STOP
        self.on_button = tk.Button(frame, text='ON ', command=self.led_on)
        self.on_button.grid(row=6, column=0)
        self.off_button = tk.Button(frame, text='OFF', command=self.led_off)
        self.off_button.grid(row=6, column=1)
        # STATUS
        self.status_report = tk.StringVar()
        tk.Label(frame, textvariable=self.status_report).grid(row=7, columnspan=2)

    # SET COM PORT
    def set_com(self):
        self.com_response.set('connecting...')
        self.com_port = self.com_var.get()
        self.arduinoData = serial.Serial(f'{self.com_port}', 9600, timeout=1)
        sleep(0.500)
        self.com_response.set('COM PORT has been set')
    # START CYCLE
    def led_on(self):
        self.cycles_num = self.cycles_var.get()
        self.pumps_num = self.pumps_var.get()
        self.time_num = self.time_var.get()
        def convert_code(code):
              while len(code) < 3:	
                code = '0' + code
              return code
        self.cycles_num = convert_code(self.cycles_num)
        self.pumps_num = convert_code(self.pumps_num)
        if int(self.pumps_num) > 10:
            self.status_report.set('a maximum of 10 pumps are available')
            self.cycles_num = "000"
        else:
            self.status_report.set('ON')
        self.time_num = convert_code(self.time_num)
        self.start_code = self.cycles_num + self.pumps_num + self.time_num + "000"
        print(f"{self.start_code}")
        # self.arduinoData = serial.Serial('/dev/cu.usbmodem141101', 9600, timeout=1)
        self.reading = True
        self.arduinoData.readline()
        self.arduinoData.readline()
        self.arduinoData.write(f"{self.start_code}$".encode())
        def print_serial():
            data_list = []
            while self.reading:
                try:
                    data = self.arduinoData.read().decode('utf-8')
                    data_list.append(data)
                    # print(data_list)
                    converted_data = dh.convert_data(data_list)
                    dh.data_to_csv(converted_data)
                except:
                    break
        print_serial = threading.Thread(target=print_serial)
        print_serial.start()
    # STOP CYCLE
    def led_off(self):
        self.reading = False
        self.status_report.set('OFF')
        if self.arduinoData.isOpen() == True:
            self.arduinoData.close()
            self.arduinoData.open()
   
root = tk.Tk()
root.geometry('400x250')
root.wm_title('Arduino Controller')  
app = App(root)
root.mainloop()