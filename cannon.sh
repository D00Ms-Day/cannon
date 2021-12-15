#!/usr/bin/bash
banner() {
clear
figlet -cf  slant C4NNOON
printf " \e[1;30m                          Version 1.0\n"
printf "\n"
printf " \e[37;1m       ----============================-----          \e[0m\n"
printf " \e[37;1m       |+|   DEVELOPER : D00MS D4Y       |+|           \e[0m\n"
printf " \e[37;1m       |+|   TEAM : ANONYMOUS ELITES     |+|            \e[0m\n"
printf " \e[37;1m       |+|   FACEBOOK : ANONYMOUS ELITES |+|             \e[0m\n"
printf " \e[37;1m       ----============================-----              \e[0m\n"
printf " \e[92m[\e[33;1m*\e[92m]\e[0m\e[30;1m Developed by \e[33;1m D00ms D4y\e[31;1m (ANONYMOUS ELITES)\e[0m\n"
printf " \n"
printf "\e[36;1m:::Choose A Weapon:::\e[0m\n"
printf " \n"
}
menu() {
#printf " \e[1;31m[\e[0m\e[1;77m01\e[0m\e[1;31m]\e[0m\e[30;1m IP Locator    \e[1;31m\e[0m\n"
printf " \e[1;31m[\e[0m\e[1;77m01\e[0m\e[1;31m]\e[0m\e[33;1m Credit Card Validator   \e[0m\e[1;31m\e[0m\n"
printf " \e[1;31m[\e[0m\e[1;77m02\e[0m\e[1;31m]\e[0m\e[31;1m DOS      \e[0m\e[1;31m\e[0m\n"
#printf " \e[1;31m[\e[0m\e[1;77m04\e[0m\e[1;31m]\e[0m\e[35;1m Port Scanner   \e[0m\e[1;31m\e[0m\n"
printf " \e[1;31m[\e[0m\e[1;77m03\e[0m\e[1;31m]\e[0m\e[34;1m Password Cracker \e[0m\e[1;31m\e[0m\n"
printf " \e[1;31m[\e[0m\e[1;77m04\e[0m\e[1;31m]\e[0m\e[93;1m Exit(can use ctrl + c)     \e[0m\e[1;31m\e[0m\n"
printf "\e[0m\n"
read -p $' \e[1;31m[\e[0m\e[1;77m<<+>>\e[0m\e[1;31m]\e[0m\e[1;92m Make A Shot:: \e[0m\e[1;96m\en' option
if [[ $option == 1 || $option == 01 ]]; then
chmod +x cc.py
python3 cc.py
elif [[ $option == 2 || $option == 02 ]]; then
chmod +x dos.py
python3 dos.py
elif [[ $option == 3 || $option == 03 ]]; then
chmod +x passcracker.py
python3 passcracker.py
elif [[ $option == 4 || $option == 04 ]]; then
#chmod +x portscanner.py
#python3 portscanner.py
#elif [[ $option == 5 || $option == 05 ]]; then
#chmod +x passcracker.py
#python3 passcracker.py
#elif [[ $option == 5 || $option == 06 ]]; then
printf " \e[30;1m ::Hope You Enjoyed My Company? Will Like To See You Again! \e[0m\n"
exit 1
else
printf " \e[1;91m[\e[0m\e[1;97m!\e[0m\e[1;91m]\e[0m\e[1;93m Make Rightful Choice The Next Time\e[1;91\e[0m\e[1;97m!\e[0m\e[1;91m\e[0m\n"
printf " \e[30;1m ::Hope You Enjoyed My Company? Will Like To See You Again! \e[0m\n"
sleep 1
banner
menu
#break
fi
}
banner
menu

