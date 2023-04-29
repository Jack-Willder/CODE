from time import sleep
from subprocess import getoutput
from tkinter import *
from threading import Thread
from PIL import ImageTk, Image


class MyGUI:
    def __init__(self):
        self.t = None
        self.root = Tk()

        self.root.title("First")
        self.root.iconbitmap("C:\\Users\\Suriya\\Downloads\\@\\Protocol\\STARTUP-PROTOCOL\\flickr.ico")

        # Importing Image
        self.img1 = ImageTk.PhotoImage(Image.open("C:\\Users\\Suriya\\Downloads\\@\\Wallpaper\\MOD1.png"))
        self.lbl2 = Label(self.root, image=self.img1)
        self.lbl2.grid(row=2, column=0, columnspan=4, padx=5, pady=5)

        self.lbl1 = Label(self.root, text="Getting...", font=("Arial", 10))
        self.lbl1.configure(background="#DC04E6", width=60, height=20, justify="left")
        self.lbl1.grid(row=0, column=0, columnspan=4, padx=5, pady=5, sticky=E+W)
        self.start()

        self.btn1 = Button(self.root, text="click Me!", font=("Arial", 10), command=self.start)
        self.btn1.grid(row=1, column=0, columnspan=2, sticky=E+W, padx=5, pady=5)

        self.btn2 = Button(self.root, text="Exit", font=("Arial", 10), command=self.root.quit)
        self.btn2.grid(row=1, column=2, columnspan=4, sticky=E+W, padx=5, pady=5)

        self.root.mainloop()

    def start(self):
        self.t = Thread(target=self.main)
        self.t.setDaemon(True)
        self.t.start()

    def main(self):
        n = 00
        m = 00
        while True:
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
            n = n + 1
            if n == 60:
                n = 0
                m = m + 1

            line = f'''
        TIME\t\t\t:    {m}:{n}
        STATE\t\t\t:   {line01[1]}
        SSID\t\t\t:   {line02[1]}
        CONNECTION\t\t:   {line03[1]}
        CHANNEL\t\t\t:   {line04[1]}
        RECEIVE RATE (Mbps)\t:   {line05[1]}
        TRANSMIT RATE (Mbps)\t:   {line06[1]}
        SIGNAL\t\t\t:   {line07[1]}
        PROFILE\t\t\t:   {line08[1]}'''
            self.root.update()
            self.lbl1.configure(text=line)
            self.root.update()
            timer = 1 * 0.0001
            sleep(timer)


MyGUI()
