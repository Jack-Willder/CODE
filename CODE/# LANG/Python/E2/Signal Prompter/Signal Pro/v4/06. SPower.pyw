from time import sleep
from subprocess import getoutput
from tkinter import *
from threading import Thread
from playsound import playsound


class MyGUI:
    def __init__(self):
        self.lbl1 = None
        self.t = None
        self.ping = None
        self.root = Tk()
        self.root.geometry("416x295")
        self.root.configure(bg="#343434")
        self.root.title("Signal Info Pro")
        self.root.iconbitmap("C:\\Users\\Suriya\\Downloads\\@\\Protocol\\STARTUP-PROTOCOL\\flickr.ico")
        self.lbl1 = Label(self.root, text="...", font=("Arial", 10))
        self.lbl1.configure(background="#003049", width=50, height=15, justify="left", fg="#f6fff8")
        self.lbl1.grid(row=0, column=0, columnspan=4, padx=5, pady=5, sticky=E + W)
        self.btn1 = Button(self.root, text="click Me!", font=("Arial", 10))
        self.btn1.grid(row=1, column=0, columnspan=2, sticky=E + W, padx=5, pady=5)
        self.btn2 = Button(self.root, text="Exit", font=("Arial", 10), command=self.root.quit)
        self.btn2.grid(row=1, column=2, columnspan=4, sticky=E + W, padx=5, pady=5)
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
    def main(self):
        global line, bgcol, ping
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
                self.ping = 'None'
                speed = int(line05[1])
                if speed > 130:
                    bgcol = "#003049"
                elif 80 <= speed <= 129:
                    bgcol = "#d62828"
                    playsound('C:\\Users\\Suriya\\Desktop\\Python\\E2\\Signal Prompter\\Signal Pro\\resource\\Music\\Soft Notification.mp3')
                elif 60 <= speed <= 79:
                    bgcol = "#fcbf49"
                    playsound('C:\\Users\\Suriya\\Desktop\\Python\\E2\\Signal Prompter\\Signal Pro\\resource\\Music\\Soft Notification.mp3')
                elif speed < 60:
                    bgcol = "#370617"
                    playsound('C:\\Users\\Suriya\\Desktop\\Python\\E2\\Signal Prompter\\Signal Pro\\resource\\Music\\Soft Notification.mp3')
                else:
                    bgcol = "#f77f00"
                    playsound('C:\\Users\\Suriya\\Desktop\\Python\\E2\\Signal Prompter\\Signal Pro\\resource\\Music\\Soft Notification.mp3')

                try:
                    self.ping = getoutput('ping /n 1 google.com')
                    ping = self.ping.splitlines()
                    ping = ping[2].split()
                    ping = ping[4].split('=')
                    ping = ping[1]
                except Exception as _:
                    ping = 'NoPing'
                line = f'''
        STATE\t\t\t:\t{line01[1]}
        SSID\t\t\t:\t{line02[1]}
        CONNECTION\t\t:\t{line03[1]}
        CHANNEL\t\t\t:\t{line04[1]}
        RECEIVE RATE (Mbps)\t:\t{line05[1]}
        TRANSMIT RATE (Mbps)\t:\t{line06[1]}
        SIGNAL\t\t\t:\t{line07[1]}
        PROFILE\t\t\t:\t{line08[1]}
        PING\t\t\t:\t {ping}
        PACKETLOSS\t\t:\t {loss}'''
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
                self.lbl1.configure(background='red', width=50, height=15, justify="left", fg="#f6fff8")
                self.lbl1.grid(row=0, column=0, columnspan=4, padx=5, pady=5, sticky=E + W)
                playsound('C:\\Users\\Suriya\\Desktop\\Python\\E2\\Signal Prompter\\Signal Pro\\resource\\Music\\not_connected.mp3')
                self.root.update()


MyGUI()
