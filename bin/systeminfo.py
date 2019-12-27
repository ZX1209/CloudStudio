#!/usr/bin/env python3
# remin to be done



import platform
from clara import ThirdShell

print(platform.uname())

if platform.system() == "Windows":
    print("")
    print("running systeminfo.exe")
    print("===")
    ThirdShell.runCmdStr(cmdstr="systeminfo.exe")
    print("===")
elif platform.system() == "Linux":
    print("install and run")
    print("""
        sudo apt-get install neofetch

        locale

        date

        cp /usr/share/zoneinfo/Asia/Shanghai /etc/localtime
        echo 'Asia/Shanghai' >/etc/timezone
    """)




