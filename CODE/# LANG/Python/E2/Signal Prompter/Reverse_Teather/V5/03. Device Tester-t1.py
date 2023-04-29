import sys
from subprocess import getoutput
from time import sleep
from os import system
# import concurrent.futures
from multiprocessing import Process


def start_console():
    print(f"Process_01\t\t:\tstarted")
    print(f"tethering_state\t:\tOnline")
    # system("gnirehtet run")
    return "Success"


#   noinspection PyBroadException
def main():
    global network_status, current_state
    current_state = 0
    # while True:
    sleep(0.5)
#   checking Device Status
    try:
        device = getoutput("adb devices")
        device = device.splitlines()
        device = device[1].split()
        device = device[1]
        device_status = str(device)
    except Exception as _:
        device_status = "No Device"
#   Checking network status
    try:
        network = getoutput("ping -n 1 google.com").splitlines()
        network = network[0].split()
        _ = network[0]
        network_status = "Disconnected"
    except Exception as _:
        network_status = "Connected"

    if device_status == "device" and network_status == "Connected":
        print(f"{device_status}\t\t\t:\tConnected")
        print(f"Network\t\t\t:\t{network_status}")
        p1 = Process(target=start_console, daemon=True)
        p1.start()
        tethering_state = "Online"
        sleep(2)
        p1.terminate()
        p1.join()
        p1.close()
        print(f"Process_01\t\t:\tclosed")
        current_state = 1
        print(current_state)
    if device_status == "No Device" and network_status == "Connected":
        print(f"{device_status}\t\t:\tDisconnected")
    if network_status == "Disconnected" and device_status == "device":
        print(f"Network\t\t:\t{network_status}")
    if device_status == "No Device" and network_status == "Disconnected":
        print("Nothing is Connected")


if __name__ == '__main__':
    main()
