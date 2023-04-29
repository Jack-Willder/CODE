from time import sleep
from subprocess import getoutput
from tkinter import *
from threading import Thread
# from PIL import ImageTk, Image


class MyGUI:
    def __init__(self):
        self.lbl1 = None
        self.t = None
        self.root = Tk()

        self.root.title("First")
        self.root.iconbitmap("C:\\Users\\Suriya\\Downloads\\@\\Protocol\\STARTUP-PROTOCOL\\flickr.ico")

        # # Importing Image
        # self.img1 = ImageTk.PhotoImage(Image.open("C:\\Users\\Suriya\\Downloads\\@\\Wallpaper\\MOD1.png"))
        # self.lbl2 = Label(self.root, image=self.img1)
        # self.lbl2.grid(row=2, column=0, columnspan=4, padx=5, pady=5)

        self.start()

        self.btn1 = Button(self.root, text="click Me!", font=("Arial", 10), command=self.start)
        self.btn1.grid(row=1, column=0, columnspan=2, sticky=E + W, padx=5, pady=5)

        self.btn2 = Button(self.root, text="Exit", font=("Arial", 10), command=self.root.quit)
        self.btn2.grid(row=1, column=2, columnspan=4, sticky=E + W, padx=5, pady=5)

        self.root.mainloop()

    def start(self):
        self.t = Thread(target=self.main)
        self.t.setDaemon(True)
        self.t.start()

#   noinspection PyBroadException
    def main(self):
        global line, bgcol
        n = 0
        m = 0
        h = 0
        loss = 0
        while True:
            sleep(1)
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
                n = int(n)
                n = n + 1
                if n == 60:
                    n = 00
                    m = int(m)
                    m = m + 2
                if m == 60:
                    n = 00
                    m = 00
                    h = int(h)
                    h = h + 1
                if int(n) < 10:
                    n = int(n)
                    n = f"0{n}"
                if int(m) < 10:
                    m = int(m)
                    m = f"0{m}"
                if int(h) < 10:
                    h = int(h)
                    h = f"0{h}"

#   Changing the background color of the Label
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
        TIME\t\t\t:\t {h}:{m}:{n}
        STATE\t\t\t:\t{line01[1]}
        SSID\t\t\t:\t{line02[1]}
        CONNECTION\t\t:\t{line03[1]}
        CHANNEL\t\t\t:\t{line04[1]}
        RECEIVE RATE (Mbps)\t:\t{line05[1]}
        TRANSMIT RATE (Mbps)\t:\t{line06[1]}
        SIGNAL\t\t\t:\t{line07[1]}
        PROFILE\t\t\t:\t{line08[1]}
        PACKETLOSS\t\t:\t{loss}'''

#   Tinker Lable Part
                self.root.update()
                self.lbl1 = Label(self.root, text=line, font=("Arial", 10))
                #   "#DC04E6"
                self.lbl1.configure(background=bgcol, width=50, height=15, justify="left", fg="#f6fff8")
                self.lbl1.grid(row=0, column=0, columnspan=4, padx=5, pady=5, sticky=E + W)
                self.root.update()
                # timer = 1 * 0.0001
                # sleep(timer)

            except Exception as _:
                print("Error 01")
                loss = loss + 1
                self.root.update()
                self.lbl1 = Label(self.root, text="NOT CONNECTED", font=("Arial", 10))
                self.lbl1.configure(background=bgcol, width=50, height=15, justify="left", fg="#f6fff8")
                self.lbl1.grid(row=0, column=0, columnspan=4, padx=5, pady=5, sticky=E + W)
                self.root.update()


MyGUI()
