from time import sleep
from os import system
from subprocess import getoutput as go


#   noinspection PyBroadException
def main():
    n = 0
    m = 0
    h = 0
    while True:
        sleep(1)
        try:
            network_interface = go("netsh wlan show interfaces")
            lines = network_interface.splitlines(False)
            line01 = lines[7].split(':')
            line02 = lines[8].split(':')
            line03 = lines[14].split(':')
            line04 = lines[15].split(':')
            line05 = lines[16].split(':')
            line06 = lines[17].split(':')
            line07 = lines[18].split(':')
            line08 = lines[19].split(':')
            n = int(n)
            n = n + 1
            if n == 60:
                n = 00
                m = int(m)
                m = m + 2
            if m == 60:
                n = 00
                m = 00
                h = int(h)
                h = h + 1
            if int(n) < 10:
                n = int(n)
                n = f"0{n}"
            if int(m) < 10:
                m = int(m)
                m = f"0{m}"
            if int(h) < 10:
                h = int(h)
                h = f"0{h}"

            line = f'''
    TIME                    :    {h}:{m}:{n}
    STATE                   :   {line01[1]}
    SSID                    :   {line02[1]}
    CONNECTION              :   {line03[1]}
    CHANNEL                 :   {line04[1]}
    RECEIVE RATE (Mbps)     :   {line05[1]}
    TRANSMIT RATE (Mbps)    :   {line06[1]}
    SIGNAL                  :   {line07[1]}
    PROFILE                 :   {line08[1]}'''

            # Output_Screen
            system("cls")
            print(line)
        except Exception:
            print("Error-02 (Disconnected)")


main()
