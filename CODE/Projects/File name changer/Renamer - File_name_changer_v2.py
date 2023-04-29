import subprocess as sp
import time

def sorterbylength(e):
    return len(e)

animename = str(input("Anime Name - "))
pointernumber = int(input("Pointer Number - "))
extension_type = str(input("Enter the extension Type - "))

names = sp.getoutput("dir /b")
namelist = names.splitlines()
namelist.sort()
namelist.sort(key=sorterbylength)
reference_namelist = []
for name in namelist:
    if name[-(len(extension_type) + 1):] == ".{extension_type}":
        reference_namelist.append(name)
        # print( "Added - ", name)
print("\n\n\n")
count = pointernumber
for name in reference_namelist:
    sp.getoutput(f'ren "{name}" "{animename} - Episode - {count}.ts"')
    print(f"{name}\t\t{animename} - Episode - {count}.{extension_type}")
    count += 1
    
print("press c and press Enter to exit")
    
while True:
    check = str(input())
    if check == c or check==C:
        exit()

