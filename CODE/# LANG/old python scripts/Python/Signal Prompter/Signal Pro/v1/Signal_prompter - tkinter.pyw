from time import sleep
from os import system
from subprocess import getoutput
import tkinter as tk
from threading import Thread


class MyGUI:
    def __init__(self):
        self.root = tk.Tk()

        self.root.geometry("500x500")
        self.root.title("First")

        self.lbl1 = tk.Label(self.root, text="Hello World", font=("Arial", 10), height=20, width=100)
        self.lbl1.configure(background="pink")
        self.lbl1.pack(padx=10, pady=10)

        self.btn1 = tk.Button(self.root, text="click Me!", font=("Arial", 10), command=self.start)
        self.btn1.pack()

        self.root.mainloop()

    def start(self):
        t = Thread(target=self.main)
        t.start()

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
            if n==60:
                n = 0
                m = m + 1

            line = f'''
            TIME                    :   {m}:{n}
            STATE                   :   {line01[1]}
            SSID                    :   {line02[1]}
            CONNECTION              :   {line03[1]}
            CHANNEL                 :   {line04[1]}
            RECEIVE RATE (Mbps)     :   {line05[1]}
            TRANSMIT RATE (Mbps)    :   {line06[1]}
            SIGNAL                  :   {line07[1]}
            PROFILE                 :   {line08[1]}'''
            self.lbl1.configure(text=line)
            self.root.update()
            sleep(1)

MyGUI()