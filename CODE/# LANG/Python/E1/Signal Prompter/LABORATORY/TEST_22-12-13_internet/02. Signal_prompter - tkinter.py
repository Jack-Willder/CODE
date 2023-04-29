from time import sleep
from subprocess import getoutput
import tkinter as tk
from threading import Thread


class MyGUI:
    def __init__(self):
        self.t = None
        self.root = tk.Tk()

        self.root.geometry("500x500")
        self.root.title("First")

        self.lbl1 = tk.Label(self.root, text="Getting...", font=("Arial", 10))
        self.lbl1.configure(background="#DC04E6", width=60, height=20, justify="left")
        self.lbl1.grid(row=0, column=0, columnspan=4, padx=5, pady=5, sticky=tk.E+tk.W)
        self.start()

        self.btn1 = tk.Button(self.root, text="click Me!", font=("Arial", 10), command=self.start)
        self.btn1.grid(row=1, column=0, columnspan=1, sticky=tk.E+tk.W, padx=5)

        self.btn2 = tk.Button(self.root, text="Stop!", font=("Arial", 10))
        self.btn2.grid(row=1, column=2, columnspan=3, sticky=tk.E+tk.W, pady=5)

        self.root.mainloop()

    def start(self):
        self.t = Thread(target=self.main, daemon=True)
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
            print(f'{m}:{n}')
            self.lbl1.configure(text=line)
            self.root.update()
            sleep(1)


MyGUI()
