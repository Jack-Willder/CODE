from time import sleep
from os import system
from subprocess import getoutput


def main():
    while True:
        network_interface = getoutput("netsh wlan show interfaces")
        lines = network_interface.splitlines(False)
        line01 = lines[7].split(':')
        line02 = lines[8].split(':')
        line03 = lines[14].split(':')
        line04 = lines[15].split(':')
        line05 = lines[16].split(':')
        line06 = lines[17].split(':')
        line07 = lines[18].split(':')
        line08 = lines[19].split(':')
        line = f'''
STATE                   :   {line01[1]}
SSID                    :   {line02[1]}
CONNECTION              :   {line03[1]}
CHANNEL                 :   {line04[1]}
RECEIVE RATE (Mbps)     :   {line05[1]}
TRANSMIT RATE (Mbps)    :   {line06[1]}
SIGNAL                  :   {line07[1]}
PROFILE                 :   {line08[1]}'''
        system("cls")
        print(line)
        sleep(1)


main()
