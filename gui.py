import serial
import tkinter as tk
from tkinter import messagebox
from time import sleep
from datetime import datetime
import threading
import csv
import os
import sys

def data_to_csv(data):
  with open("./data_report.csv",'a') as file:
    writer = csv.writer(file,delimiter=",")
    for i in data: 
      writer.writerow([i])

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
        # self.arduinoData = serial.Serial('/dev/cu.usbmodem141101', 9600, timeout=1)
        self.arduinoData = serial.Serial(f'{self.com_port}', 9600, timeout=1)
        sleep(0.500)
        self.com_response.set('COM PORT has been set')

    # START CYCLE
    def led_on(self):
        if self.arduinoData.isOpen() == False:
            self.arduinoData.open()

        #START CODE FOR ARDUINO    
        self.cycles_num = self.cycles_var.get()
        self.pumps_num = self.pumps_var.get()
        self.time_num = self.time_var.get()
        def convert_code(code):
              while len(code) < 3:	
                code = '0' + code
              return code
        self.cycles_num = convert_code(self.cycles_num)
        self.pumps_num = convert_code(self.pumps_num)
        self.time_num = convert_code(self.time_num)
        if int(self.pumps_num) > 10:
            self.status_report.set('a maximum of 10 pumps are available')
            self.cycles_num = "000"
        else:
            self.status_report.set('ON')
        self.start_code = self.cycles_num + self.pumps_num + self.time_num + "000"
        self.reading = True
        self.arduinoData.readline()
        self.arduinoData.readline()
        self.arduinoData.write(f"{self.start_code}$".encode())

        #BEGIN LOG
        self.start_time = datetime.now()
        try: 
            with open("./data_report.csv",'w') as f:
                writer = csv.writer(f,delimiter=",")
                writer.writerow([f"Run Started at: {self.start_time}"])
        except PermissionError:
            self.reading = False
            self.arduinoData.close()
            self.arduinoData.open()
            root = tk.Tk()
            root.withdraw()
            messagebox.showinfo('Permission Error', 'cannot write data log without appropriate permissions')

        # COLLECT DATA
        self.cycle_count = 0
        # self.data_list = []
        def print_serial():
            while self.reading == True:
                try:
                    data = self.arduinoData.read().decode('utf-8')
                    if data == 'a':
                        self.cycle_count += 1
                        self.status_report.set(f"Cycle: {self.cycle_count}    Pump: 1")
                        data_to_csv([f"--- Cycle # : {self.cycle_count} at {datetime.now()}"])
                        data_to_csv([f"Pump 1 at {datetime.now()}"])
                        continue
                    elif data == 'b':
                        self.status_report.set(f"Cycle: {self.cycle_count}    Pump: 2")
                        data_to_csv([f"Pump 2 at {datetime.now()}"])
                        continue
                    elif data == 'c':
                        self.status_report.set(f"Cycle: {self.cycle_count}    Pump: 3")
                        data_to_csv([f"Pump 3 at {datetime.now()}"])
                        continue
                    elif data == 'd':
                        self.status_report.set(f"Cycle: {self.cycle_count}    Pump: 4")
                        data_to_csv([f"Pump 4 at {datetime.now()}"])
                        continue
                    elif data == 'e':
                        self.status_report.set(f"Cycle: {self.cycle_count}    Pump: 5")
                        data_to_csv([f"Pump 5 at {datetime.now()}"])
                        continue
                    elif data == 'f':
                        self.status_report.set(f"Cycle: {self.cycle_count}    Pump: 6")
                        data_to_csv([f"Pump 6 at {datetime.now()}"])
                        continue
                    elif data == 'g':
                        self.status_report.set(f"Cycle: {self.cycle_count}    Pump: 7")
                        data_to_csv([f"Pump 7 at {datetime.now()}"])
                        continue
                    elif data == 'h':
                        self.status_report.set(f"Cycle: {self.cycle_count}    Pump: 8")
                        data_to_csv([f"Pump 8 at {datetime.now()}"])
                        continue
                    elif data == 'i':
                        self.status_report.set(f"Cycle: {self.cycle_count}    Pump: 9")
                        data_to_csv([f"Pump 9 at {datetime.now()}"])
                        continue
                    elif data == 'j':
                        self.status_report.set(f"Cycle: {self.cycle_count}    Pump: 10")
                        data_to_csv([f"Pump 10 at {datetime.now()}"])
                        continue
                except:
                    # data_to_csv(f"Run Stopped at {datetime.now()}")
                    self.reading = False
                    break
            # try:
            #     converted_data = dh.convert_data(self.data_list)
            #     dh.data_to_csv(converted_data)
            # except:
            #     pass
        print_serial = threading.Thread(target=print_serial)
        print_serial.start()

        #TIMER TO END RUN
        self.max_time = int(self.cycles_num)*int(self.pumps_num)*int(self.time_num)+3
        def stop_data():
            self.arduinoData.close()
            self.arduinoData.open()
            self.status_report.set("Run Complete")
            data_to_csv([f"Run finished at: {datetime.now()}"])
            os.rename("./data_report.csv",f"./data_report{datetime.now()}.csv")
            self.reading = False
        self.run_timer = threading.Timer(self.max_time, stop_data)
        self.run_timer.start()

    # STOP CYCLE
    def led_off(self):
        self.reading = False
        self.run_timer.cancel()
        data_to_csv([f"Run stopped at: {datetime.now()}"])
        os.rename("./data_report.csv",f"./data_report{datetime.now()}.csv")
        self.status_report.set('OFF')
        if self.arduinoData.isOpen() == True:
            self.arduinoData.close()
            self.arduinoData.open()

   
root = tk.Tk()
root.geometry('400x250')
root.wm_title('Arduino Controller') 
app = App(root)

def stop():
    # serial.Serial.close()
    root.destroy()
    sys.exit()
root.protocol("WM_DELETE_WINDOW", stop)

if __name__ == "__main__":
    root.mainloop()

# def remove_consecutive_duplicates(lst):
#   ahead = iter(lst)
#   next(ahead)
#   return [ x for x, y in zip_longest(lst, ahead) if x and x != y ]

# data = remove_consecutive_duplicates(data)