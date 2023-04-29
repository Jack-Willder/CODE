import win32gui, win32ui, win32con
from time import sleep

def main():
    # window_name = "C:\Windows\system32\cmd.exe"
    window_name = "Command Prompt"
    hwnd = win32gui.FindWindow(None, window_name)
    win = win32ui.CreateWindowFromHandle(hwnd)
    win.PostMessage(win32con.WM_KEYDOWN, win32con.VK_RETURN, 0)
    # win.PostMessage(win32con.WM_KEYUP, win32con.VK_RETURN, 0)
    # list_inner_windows(hwnd)
    # win.SendMessage(win32con.WM_KEYDOWN, 0x32, 0)
    # sleep(0.01)
    # win.SendMessage(win32con.WM_KEYUP, 0x32, 0)

# def list_window_names():
#     def winEnumHandler(hwnd, ctx):
#         if win32gui.IsWindowVisible(hwnd):
#             print(hex(hwnd), '"' + win32gui.GetWindowText(hwnd) + '"')
#     win32gui.EnumWindows(winEnumHandler, None)
    
# def list_inner_windows(whndl):
#     def callback(hwnd, hwnds):
#         if win32gui.IsWindowVisible(hwnd) and win32gui.IsWindowEnabled(hwnd):
#             hwnds[win32gui.GetClassName(hwnd)] = hwnd
#         return True
#     hwnds = {}
#     win32gui.EnumChildWindows(whndl, callback, hwnds)
#     print(hwnds)

main()