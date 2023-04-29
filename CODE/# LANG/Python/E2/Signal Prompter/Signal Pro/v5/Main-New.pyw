from subprocess import getoutput
from threading import Thread
from time import sleep
from time import time
from tkinter import *
import concurrent.futures


class MyGUI:
    def __init__(self):
        self.bgcol = None
        self.t = None
        self.lbl1 = None
        self.ping = None
        self.line00 = []
        self.root = Tk()
        # self.root.geometry("416x295")
        self.root.geometry(f"416x550+{-7 + 10}+10")
        self.root.resizable(False, True)
        self.root.configure(bg="#343434")
        self.root.title("Signal Info Pro")
        self.root.iconbitmap("C:\\Users\\Suriya\\Downloads\\@\\Protocol\\STARTUP-PROTOCOL\\flickr.ico")
        self.lbl1 = Label(self.root, text="...", font=("Arial", 10))
        self.lbl1.configure(background="#003049", width=50, height=15, justify="left", fg="#f6fff8")
        self.lbl1.grid(row=0, column=0, columnspan=4, padx=5, pady=5, sticky=E + W)
        self.lbl2 = Label(self.root, text="None", font=("Arial", 10))
        self.lbl2.configure(background="#878748", width=50, height=15, justify="center", fg="#000")
        self.lbl2.grid(row=1, column=0, columnspan=4, padx=5, sticky=E + W)
        self.btn1 = Button(self.root, text="click Me!", font=("Arial", 10))
        self.btn1.grid(row=2, column=0, columnspan=2, sticky=E + W, padx=5, pady=5)
        self.btn2 = Button(self.root, text="Exit", font=("Arial", 10), command=self.root.quit)
        self.btn2.grid(row=2, column=2, columnspan=4, sticky=E + W, padx=5, pady=5)
        self.root.update_idletasks()
        width = self.root.winfo_width()
        frm_width = self.root.winfo_rootx() - self.root.winfo_x()
        win_width = width + 2 * frm_width
        height = self.root.winfo_height()
        titlebar_height = self.root.winfo_rooty() - self.root.winfo_y()
        win_height = height + titlebar_height + frm_width
        x = self.root.winfo_screenwidth() // 2 - win_width // 2
        y = self.root.winfo_screenheight() // 2 - win_height // 2
        self.root.geometry('{}x{}+{}+{}'.format(width, height, x, y))
        self.root.deiconify()
        self.t = Thread(target=self.main, daemon=True)
        self.t.start()
        self.root.mainloop()

    #   noinspection PyBroadException
    def ping_checker(self):
        try:
            self.ping = getoutput('ping /n 1 google.com')
            pings = self.ping.splitlines()
            pings = pings[2].split()
            pings = pings[4].split('=')
            pings = pings[1]
            return pings
        except Exception as _:
            pings = 'NoPing'
            return pings

    #   noinspection PyBroadException
    def network_details(self):
        try:
            self.line00.clear()
            lines = getoutput("netsh wlan show interfaces").splitlines(False)
            line01 = lines[7].split(':')
            line02 = lines[8].split(':')
            line03 = lines[14].split(':')
            line04 = lines[15].split(':')
            line05 = lines[16].split(':')
            line06 = lines[17].split(':')
            line07 = lines[18].split(':')
            line08 = lines[19].split(':')

            self.line00.append(line01[1])
            self.line00.append(line02[1])
            self.line00.append(line03[1])
            self.line00.append(line04[1])
            self.line00.append(line05[1])
            self.line00.append(line06[1])
            self.line00.append(line07[1])
            self.line00.append(line08[1])
            self.bgcol = None
            self.ping = None

            speed = float(line05[1])
            if speed > 130:
                self.bgcol = "#003049"
            elif 80 <= speed <= 129:
                self.bgcol = "#d62828"
            elif 60 <= speed <= 79:
                self.bgcol = "#fcbf49"
            elif speed < 60:
                self.bgcol = "#370617"
            else:
                self.bgcol = "#f77f00"

            with concurrent.futures.ThreadPoolExecutor() as executor:
                pinger = executor.submit(self.ping_checker)
                self.ping = pinger.result()
            return self.line00
        except Exception as error_2:
            print(error_2)

    #   noinspection PyBroadException
    def main(self):
        global line, bgcol, ping
        loss = 0
        while True:
            sleep(0.2)
            start = time()
            with concurrent.futures.ThreadPoolExecutor() as executor01:
                executor01.submit(self.network_details)
            try:
                line = f'''STATE\t\t\t:\t{self.line00[0]}
SSID\t\t\t:\t{self.line00[1]}
CONNECTION\t\t:\t{self.line00[2]}
CHANNEL\t\t:\t{self.line00[3]}
RECEIVE RATE (Mbps)\t:\t{self.line00[4]}
TRANSMIT RATE (Mbps)\t:\t{self.line00[5]}
SIGNAL\t\t\t:\t{self.line00[6]}
PROFILE\t\t\t:\t{self.line00[7]}
PING\t\t\t:\t {self.ping}
PACKETLOSS\t\t:\t {loss}'''
                self.root.update()
                self.lbl1 = Label(self.root, text=line, font=("Arial", 10))
                self.lbl1.configure(background=self.bgcol, width=50, height=15, justify="left", fg="#f6fff8")
                self.lbl1.grid(row=0, column=0, columnspan=4, padx=5, pady=5, sticky=E + W)
                self.root.update()
            except Exception as _:
                print("Error-01")
                loss += 1
                self.root.update()
                self.lbl1 = Label(self.root, text="NOT CONNECTED", font=("Arial", 10))
                self.lbl1.configure(background='red', width=50, height=15, justify="left", fg="#f6fff8")
                self.lbl1.grid(row=0, column=0, columnspan=4, padx=5, pady=5, sticky=E + W)
                self.root.update()
                # executor01.submit()
            end = time()
            print(f"Execution Time - {round((end - start), 4)}")


MyGUI()
