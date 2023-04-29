from os import system
from time import sleep
from subprocess import getoutput
from multiprocessing import Process


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
        if note[0] == "1":
            pass
        elif note[0] == "0":
            print("Exit command received from Master - 02")
            exit()
        else:
            print("Error-02")


def main():
    while True:
        f = open("Temp_dump_test.txt", "r")
        note = f.readlines()
        if note[0] == "1":
            th = Process(target=start_formal)
            th.start()
            start_checker()
        elif note[0] == "0":
            print("Exit command received from Master - 01")
            exit()
        else:
            print("Error-01")


main()
