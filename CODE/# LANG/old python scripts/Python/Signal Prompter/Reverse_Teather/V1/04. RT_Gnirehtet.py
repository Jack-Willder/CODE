from os import system
from threading import Thread
from time import sleep


# noinspection PyBroadException
def start_formal():
    system("TITLE FORMAL")
    system('cd "C:\gnirehtet"')
    system("adb devices")
    system("@gnirehtet run")


def start_checker():
    while True:
        sleep(0.5)
        f = open("Temp_dump_test.txt", "r")
        note = f.readlines()
        # print(f"Note value is {note[0]}")
        if note[0] == "1":
            # print("pass-02")
            pass
        elif note[0] == "0":
            print("Exit command received from Master")
            exit()
        else:
            print("Error-02")


def main():
    while True:
        f = open("Temp_dump_test.txt", "r")
        note = f.readlines()
        # print(f"Note value is {note[0]}")
        if note[0] == "1":
            th = Thread(target=start_formal)
            th.setDaemon(True)
            th.start()
            start_checker()
        elif note[0] == "0":
            print("Exit command received from Master")
            exit()
        else:
            print("Error-01")


main()
