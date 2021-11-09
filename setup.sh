#!/bin/bash

# Author : SAEP ASER





kirmizi="\e[31m"

yesil="\e[32m"

sari="\e[33m"

mor="\e[34m"

mavi="\e[36m"

beyaz="\033[1;37m"

reset="\e[0m"



apt install figlet

clear

figlet HUNTER

printf "\e[1;77m\e[41m     KURULUMLARINIZ 3 SANİYE İÇİNDE BAŞLAYACAKTIR!!     \e[0m\n"

sleep 3

termux-setup-storage -y

pkg install root-repo -y

pkg install unstable-repo

pkg install x11-repo -y

apt update -y

apt upgrade -y

pkg install git -y

pkg install python python2 -y

pkg intall python3 -y

pkg install pip -y

apt install purge-repo -y

pkg install php -y

pkg install perl -y

pkg install nano -y

pkg install cat -y

pkg install pip2 -y

pip install wordlist -y

pkg install nmap -y

pkg install hydra -y

pkg install openssl -y

apt install nodejs -y

pkg install cmatrix

alias eğitim='python3 Termux-Eğitim.py'

clear



printf "\e[1;77m\e[41m                 KURULUM BİTTİ!!                   \e[0m\n"

printf "\n"

printf "\e[1;77m\e[41m     eğitim  YAZARAK ARACI ÇALIŞTIRABİLİRSİNİZ     \e[0m\n"