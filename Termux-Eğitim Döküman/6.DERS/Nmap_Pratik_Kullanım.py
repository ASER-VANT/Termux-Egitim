#!usr/bin/env python
# -*- coding: utf-8 -*-

import os

os.system("apt install tcptraceroute")
os.system("apt install traceroute")
os.system("apt install figlet")
os.system("apt-get install nmap")
os.system("clear")
os.system("figlet MAKRO")


print("""Nmap pratik programına hoş geldiniz


1)Kısa Tarama
2)Port tarama
3)Agresif tarama
4)Gizli Tarama(mac adres)
5)Gizli Tarama(İP adres)
6)Hedef İşletim sistemini Öğrenme
7)Hedef Servis Sürümleni Öğrenme
8)Hedef Filitreleme Tespiti
9)Firewall Atlatma

""")


secim = raw_input("Lütfen Seçim Yapınız: ")


if(secim=="1"):
	hedef = raw_input("Lütfen Hedef IP Giriniz: ")
	os.system("nmap "+ hedef)
	print("""
Terminalde Kullanımı İçin: nmap + hedef""")

elif(secim=="2"):
	hedef = raw_input("Lütfen Hedef IP Giriniz: ")	
	os.system("nmap -sS -sV "+hedef )
	print("""
Terminalde Kullanımı İçin: nmap -sS -sV + hedef""")

elif(secim=="3"):
	hedef = raw_input("Lütfen Hedef IP Giriniz: ")
	os.system("nmap -A "+hedef )
	print("""
Terminalde Kullanımı İçin: nmap -A hedef""")
elif(secim=="4"):
	hedef = raw_input("Lütfen Hedef IP Giriniz: ")
	os.system("nmap 10.0.2.15 --spoof-mac 00:0B:DB:82:58:C3 "+ hedef)
	print("""
Terminalde Kullanımı İçin: nmap --spoof-mac + MAC + hedef""")
elif(secim=="5"):
	hedef = raw_input("Lütfen Hedef IP Giriniz: ")
	os.system("nmap -D 77.245.159.2 " + hedef)
	print("""
Terminalde Kullanımı İçin: nmap -D + sahte IP + hedef""")
elif(secim=="6"):
	hedef = raw_input("Lütfen Hedef IP Giriniz: ")
	os.system("nmap -sS "+ hedef)
	print("""
Terminalde Kullanımı İçin: nmap -sS + hedef""")
elif(secim=="7"):
	hedef = raw_input("Lütfen Hedef IP Giriniz: ")
	os.system("nmap -sV "+ hedef)
	print("""
Terminalde Kullanımı İçin: nmap -sV + hedef""")
elif(secim=="8"):
	hedef = raw_input("Lütfen Hedef IP Giriniz: ")
	os.system("nmap -sA "+ hedef)

	print("""
Terminalde Kullanımı İçin: nmap -sA + hedef""")
elif(secim=="9"):
	hedef = raw_input("Lütfen Hedef IP Giriniz: ")
	os.system("nmap -f -f "+ hedef)
	print("""
	Terminalde Kullanımı İçin: nmap -f -f + hedef (-f parametresi firewallı daha kolay atlatmayı sağlar ama tarama süresini uzatır)""")
else:
	print("Hatlı Seçim Yeniden Dene")

tek = raw_input("Tekrar Tarama Yapmak İstermisin y/n: ")

if(tek=="y"):
	os.system("python Nmap_Pratik_Kullanım.py")

elif(tek=="n"):
	print("Tekrar Görüşmek Üzere")
else:
	print("Yanlış Seçim Program Kapatılıyor")
