import os
from time import sleep

    
def check_device():
    os.system('@echo Working')
    os.system('@cd "C:\gnirehtet"')
    os.system('@adb devices > devices.txt')
    f = open('devices.txt', 'r')
    try:
        print('Trying...')
        device = f.readlines()[1]
        list = device.split()
        print('Device Found\nDevice ID = ' ,list[0])
        if(list[1]=='device'):
            os.system('@gnirehtet run')
        f.close()        
    except:
        print('\n\nTry Failed!\nExecuting final:')

while True:
    check_device()
    sleep(5)