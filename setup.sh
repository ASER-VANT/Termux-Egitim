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
pkg install root-repo unstable-repo x11-repo -y
apt install game-repo
apt purge game-repo
apt update
apt upgrade -y
apt install git -y
apt install python python2 -y
apt intall python3 -y
apt install pip -y
apt install php -y
apt install perl -y
apt install nano -y
apt install cat -y
apt install pip2 -y
pip install wordlist -y
apt install nmap -y
apt install hydra -y
apt install openssl -y
apt install nodejs -y
apt install cmatrix
alias egitim='python3 Termux-Eğitim.py'
clear

printf "$kirmizi                 KURULUM BİTTİ!!                   $reset"
printf "\n"
printf "$kirmizi     egitim  YAZARAK ARACI ÇALIŞTIRABİLİRSİNİZ     $reset"
