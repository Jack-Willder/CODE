from subprocess import getoutput
from time import sleep
import concurrent.futures


def checkker():
    print("checker")
    device = getoutput("adb devices")
    device = device.splitlines()
    device = device[1].split()
    device = device[1]
    device = str(device)
    return device


def start_counter():
    print("Start_counter")
    with concurrent.futures.ProcessPoolExecutor() as executor:
        while True:
            p1 = executor.submit(checkker)
            return p1.result()


def state_checker():
    sleep(2)
    print("state_checker")
    print(f' state: > {device_state} <')
    if device_state == 'device':
        print("True")
    # else:
    #     print(device_state)
        # with concurrent.futures.ProcessPoolExecutor() as executor01:
        #     p2 = executor01.submit(start_console)
        #     current_state = p2.result()
        #     print(current_state)


def start_console():
    print("Started")
    # getoutput("@title Unet.JACK\nprompt JACK-->\n@cd C:\gnirehtet\n@gnirehtet run")
    getoutput("notepad.exe")
    return "Success"


def main():
    global device_state
    with concurrent.futures.ProcessPoolExecutor() as executor1:
        m1 = executor1.submit(start_counter)
        executor1.submit(state_checker)
        device_state = m1.result()
        print(f'mainvalue > {device_state} <')


if __name__ == '__main__':
    main()
