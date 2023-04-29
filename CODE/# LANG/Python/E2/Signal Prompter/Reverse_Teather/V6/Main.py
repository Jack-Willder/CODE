from time import sleep
from time import perf_counter
from subprocess import getoutput
from multiprocessing import Process
from os import system


def start_console():
    while True:
        pass
        # print(f"Process_01\t\t:\tstarted")
        # getoutput("gnirehtet run")


#   noinspection PyBroadException
def main(p):
    global tethering_state, current_state, network_status, p1
    p1 = Process(target=start_console, daemon=True)
    # If the process is Running before the program has started close it.
    if p1.is_alive():
        print("Closing Previous processes")
        p1.terminate()
        sleep(0.1)
        if not p1.is_alive():
            print("Joining...")
            p1.join(timeout=1.0)
            p1.close()

    while True:
        start = perf_counter()
        sleep(1)
        # Checking Device Status
        try:
            device = getoutput("adb devices")
            device = device.splitlines()
            device = device[1].split()
            device = device[1]
            device_status = str(device)
        except Exception as _:
            device_status = "No Device"

        # Checking network status
        try:
            network = getoutput("ping -n 1 google.com").splitlines()
            network = network[0].split()
            _ = network[0]
            network_status = "Disconnected"
        except Exception as _:
            network_status = "Connected"

        # Device and Network are Connected
        if device_status == "device" and network_status == "Connected":
            if not current_state == "Device and Network are Connected":
                # system("cls")
                # print(f"{device_status}\t\t\t:\tConnected")
                # print(f"Network\t\t\t:\t{network_status}")
                current_state = "Device and Network are Connected"
            if p1.is_alive():
                pass
            if not p1.is_alive():
                if p == 0:
                    p1.start()
                    print("Starting - Process")
                    p = p + 1
                if not p == 0:
                    pass

        # Device not Connected
        if device_status == "No Device" and network_status == "Connected":
            if not current_state == "Device not Connected":
                system("cls")
                print(f"{device_status}\t\t:\tDisconnected")
                current_state = "Device not Connected"
            if p1.is_alive():
                p1.terminate()
                p = 0
                sleep(0.1)
                if not p1.is_alive():
                    print("Joining...")
                    p1.join(timeout=1.0)
                    p1.close()
                    break
                print(f"Teather Disconnected")

        # Network not Connected
        if network_status == "Disconnected" and device_status == "device":
            if not current_state == "Network not Connected":
                system("cls")
                print(f"Network\t\t:\t{network_status}")
                current_state = "Network not Connected"
            if p1.is_alive():
                p1.terminate()
                sleep(0.1)
                if not p1.is_alive():
                    print("Joining...")
                    p1.join(timeout=1.0)
                    p1.close()
                    break
                print(f"Teather Disconnected")

        # Device and Network Not Connected
        if device_status == "No Device" and network_status == "Disconnected":
            if not current_state == "Device and Network Not Connected":
                system("cls")
                print("Nothing is Connected")
                current_state = "Device and Network Not Connected"
            if p1.is_alive():
                p1.terminate()
                sleep(0.1)
                if not p1.is_alive():
                    print("Joining...")
                    p1.join(timeout=1.0)
                    p1.close()
                    break
                print(f"Teather Disconnected")
        stop = perf_counter()
        print(f"Time Taken - {round((stop - start), 1)}")
    main(p)


if __name__ == '__main__':
    Process_count = 0
    current_state = None
    main(Process_count)
