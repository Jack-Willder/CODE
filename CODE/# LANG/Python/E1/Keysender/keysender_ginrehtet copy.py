import win32gui, win32ui, win32con
from time import sleep

def main():
    window_name = "FORMAL"
    try:
        while True:
            hwnd = win32gui.FindWindow(None, window_name)
            win = win32ui.CreateWindowFromHandle(hwnd)
            win.PostMessage(win32con.WM_KEYDOWN, 0x43, 0)
            win.PostMessage(win32con.WM_KEYUP, 0x43, 0)
            win.PostMessage(win32con.WM_KEYDOWN, win32con.VK_RETURN, 0)
            # win.PostMessage(win32con.WM_CHAR, 0x0D, 0)
            sleep(0.100)
    except Exception as e:
        print(
            "This Line Is Not Ensured",
            "This Program is malfunctioned"
        )

sleep(3)
main()