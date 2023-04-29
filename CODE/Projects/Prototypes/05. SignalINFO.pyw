from time import sleep
from subprocess import getoutput
from tkinter import *
from threading import Thread


class MyGUI:
    def __init__(self):
        self.lbl1 = None
        self.t = None
        self.root = Tk()
        self.root.geometry("416x295")
        self.root.configure(bg="#343434")
        self.root.title("First")
        self.root.iconbitmap("C:\\Users\\Suriya\\Downloads\\@\\Protocol\\STARTUP-PROTOCOL\\flickr.ico")
        self.lbl1 = Label(self.root, text="...", font=("Arial", 10))
        self.lbl1.configure(background="#003049", width=50, height=15, justify="left", fg="#f6fff8")
        self.lbl1.grid(row=0, column=0, columnspan=4, padx=5, pady=5, sticky=E + W)
        self.btn1 = Button(self.root, text="click Me!", font=("Arial", 10))
        self.btn1.grid(row=1, column=0, columnspan=2, sticky=E + W, padx=5, pady=5)
        self.btn2 = Button(self.root, text="Exit", font=("Arial", 10), command=self.root.quit)
        self.btn2.grid(row=1, column=2, columnspan=4, sticky=E + W, padx=5, pady=5)
        self.t = Thread(target=self.main, daemon=True)
        self.t.start()
        self.root.mainloop()

#   noinspection PyBroadException
    def main(self):
        global line, bgcol
        loss = 0
        while True:
            sleep(0.2)
            try:
                network_interface = getoutput("netsh wlan show interfaces")
                lines = network_interface.splitlines(False)
                line01 = lines[7].split(':')
                line02 = lines[8].split(':')
                line03 = lines[14].split(':')
                line04 = lines[15].split(':')
                line05 = lines[16].split(':')
                line06 = lines[17].split(':')
                line07 = lines[18].split(':')
                line08 = lines[19].split(':')
                bgcol = None
                speed = int(line05[1])
                if speed > 130:
                    bgcol = "#003049"
                elif 80 <= speed <= 129:
                    bgcol = "#d62828"
                elif 60 <= speed <= 79:
                    bgcol = "#fcbf49"
                elif speed < 60:
                    bgcol = "#370617"
                else:
                    bgcol = "#f77f00"

                line = f'''
        STATE\t\t\t:\t{line01[1]}
        SSID\t\t\t:\t{line02[1]}
        CONNECTION\t\t:\t{line03[1]}
        CHANNEL\t\t\t:\t{line04[1]}
        RECEIVE RATE (Mbps)\t:\t{line05[1]}
        TRANSMIT RATE (Mbps)\t:\t{line06[1]}
        SIGNAL\t\t\t:\t{line07[1]}
        PROFILE\t\t\t:\t{line08[1]}
        PACKETLOSS\t\t:\t{loss}'''
                self.root.update()
                self.lbl1 = Label(self.root, text=line, font=("Arial", 10))
                self.lbl1.configure(background=bgcol, width=50, height=15, justify="left", fg="#f6fff8")
                self.lbl1.grid(row=0, column=0, columnspan=4, padx=5, pady=5, sticky=E + W)
                self.root.update()
            except Exception as _:
                print("Error 01")
                loss = loss + 1
                self.root.update()
                self.lbl1 = Label(self.root, text="NOT CONNECTED", font=("Arial", 10))
                self.lbl1.configure(background=bgcol, width=50, height=15, justify="left", fg="#f6fff8")
                self.lbl1.grid(row=0, column=0, columnspan=4, padx=5, pady=5, sticky=E + W)
                self.root.update()


MyGUI()
