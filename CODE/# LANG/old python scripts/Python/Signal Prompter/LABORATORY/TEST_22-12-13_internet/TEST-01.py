from multiprocessing import Process
from time import sleep
from os import system

url = "C:\gnirehtet\gnirehtet-run.cmd"


def problem():
    system("rundll32 url.dll,FileProtocolHandler cmd.exe")


def problem1():
    system("")


if __name__ == '__main__':
    p1 = Process(target=problem, daemon=True, name="Hellp")
    print("start")
    p1.start()
    sleep(2)
    print("close")
    p1.terminate()
    p1.join()
    p1.close()

    problem1()
