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
    while True:
        sleep(1)
        try:
            device = go("adb devices")
            device = device.splitlines()
            device = device[1].split()
            device = device[1]
            if device == 'device':
                pass
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
    except Exception:
        print("Error-03")


# noinspection PyBroadException
def stop_the_function():
    f = open("Temp_dump_test.txt", "w")
    f.write("0")
    f.close()
    system("cls")

    sleep(1)
    # Keysender for Fullscreen
    window_name = "FORMAL"
    hwnd = win32gui.FindWindow(None, window_name)
    try:
        print("Closing Window")
        win32api.SendMessage(hwnd, win32con.WM_CLOSE, 0)
    except Exception:
        print("Error-03")
    main()


def main():
    while True:
        sleep(2)
        # noinspection PyBroadException
        try:
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
            print("Error-01")


main()
