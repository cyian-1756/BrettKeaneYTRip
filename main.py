from subprocess import Popen
from time import sleep
waithours = 1
waitmin = waithours*60
waitsecs = waitmin*60
while True:
    p = Popen("brettkeane.bat", cwd= r'E:/BrettKeaneArchive/')
    stdout, stderr = p.communicate()
    sleep(waitsecs)
    choice = input("Wanna Brett Again? [y,n]")
    while choice.lowecase != "y":
        print("Wrong")
        input("Wanna Brett Again? [y,n]")
