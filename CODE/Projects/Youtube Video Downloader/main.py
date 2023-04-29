from subprocess import getoutput
from os import system
from time import sleep

directory = getoutput('dir /b')
print(directory)
directory = str(directory)
d = directory.splitlines()
print(d)
v = input(f"Enter the Video Number : ")
a = input(f"Enter the Audio Number : ")
v = int(v) - 1
a = int(a) - 1
print(d[v])
print(d[a])
print(f'ffmpeg -i "{d[v]}" -i "{d[a]}" -c copy "{d[v]}".mkv')
system(f'ffmpeg -i "{d[v]}" -i "{d[a]}" -c copy "{d[v]}.mkv"')
sleep(2)
system(f'move "{d[v]}.mkv" Convert')

system(f'del /f "{d[v]}" "{d[a]}')

sleep(2)
