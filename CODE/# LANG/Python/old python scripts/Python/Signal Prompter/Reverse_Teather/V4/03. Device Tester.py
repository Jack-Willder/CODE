from subprocess import getoutput as go
from os import system
from time import sleep
from threading import Thread
import win32gui
import win32ui
import win32con
import win32api


# noinspection PyBroadException
def starter_pack():
    system("cls")
    print("Device Found")
    n = 0
    m = 0
    h = 0
    while True:
        sleep(1)
        try:
            device = go("adb devices")
            device = device.splitlines()
            device = device[1].split()
            device = device[1]
            if device == 'device':
                network_interface = go("netsh wlan show interfaces")
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
                    n = 00
                    m = m + 2
                if m == 60:
                    n = 00
                    m = 00
                    h = h + 1

                line = f'''
        TIME                    :   {h}:{m}:{n}
        STATE                   :   {line01[1]}
        SSID                    :   {line02[1]}
        CONNECTION              :   {line03[1]}
        CHANNEL                 :   {line04[1]}
        RECEIVE RATE (Mbps)     :   {line05[1]}
        TRANSMIT RATE (Mbps)    :   {line06[1]}
        SIGNAL                  :   {line07[1]}
        PROFILE                 :   {line08[1]}'''

                # Output_Screen
                system("cls")
                print(line)
        except Exception:
            print("Error-02 (Disconnected)")
            stop_the_function()


# noinspection PyBroadException
def start_protocol():
    print("start_protocol()")
    f = open("Temp_dump_test.txt", "w")
    f.write("1")
    f.close()
    system('rundll32 url.dll,FileProtocolHandler "C:\\Users\\Suriya\\Desktop\\Python\\Signal Prompter\\04. RT_Gnirehtet.py"')

    sleep(1)
    # Keysender for Fullscreen
    window_name = "FORMAL"
    hwnd = win32gui.FindWindow(None, window_name)
    win = win32ui.CreateWindowFromHandle(hwnd)
    try:
        print("Trying Fullscreen")
        win.PostMessage(win32con.WM_KEYDOWN, 0x7A, 0)
        sleep(1)
        win32gui.CloseWindow(hwnd)
    except Exception:
        print("Error-03")


# noinspection PyBroadException
def stop_the_function():
    f = open("Temp_dump_test.txt", "w")
    f.write("0")
    f.close()
    system("cls")

    sleep(1)
    # Keysender for Closing window
    window_name = "FORMAL"
    hwnd = win32gui.FindWindow(None, window_name)
    try:
        print("Closing Window")
        win32api.SendMessage(hwnd, win32con.WM_CLOSE, 0)
    except Exception:
        print("Error-04")
    main()


# noinspection PyBroadException
def main():
    while True:
        try:
            sleep(2)
            device = go("adb devices")
            device = device.splitlines()
            device = device[1].split()
            device = device[1]
            if device == 'device':
                t = Thread(target=start_protocol)
                t.setDaemon(True)
                t.start()
                starter_pack()
        except Exception:
            system("CLS")
            print("No Device")


main()
