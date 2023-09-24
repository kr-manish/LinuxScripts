#!/usr/bin/bash

#if [ $# -lt 2 ]
#then
#else
#    ports=$(sudo nmap -v -p- --min-rate=1000 -T4 $1 -oN $2-all-ports.txt | grep ^[0-9] | cut -d '/' -f1 | tr '\n' ',' | sed s/,$//)
#    sudo nmap -v -sV -sC -O -p $ports $1 -oN $2-details.txt
#    sudo nmap -v -sU --top-ports 1000 -T4 $1 -oN $2-udp-ports.txt
#fi

for ip in $(seq 4 250)
do
	res=$(ping -c 1 10.11.1.$ip | grep '1 received')
	if [ ! -z "$res" ]
	then
		echo 10.11.1.$ip
		mkdir ${ip}_1_11_10
		ports=$(sudo nmap -v -p- --min-rate=1000 -T4 10.11.1.$ip -oN ${ip}_1_11_10/${ip}-all-ports.txt | grep ^[0-9] | cut -d '/' -f1 | tr '\n' ',' | sed s/,$//)
		sleep 2
		sudo nmap -v -sV -sC -O -p $ports 10.11.1.$ip -oA ${ip}_1_11_10/${ip}-details
		echo "==============================$ip DONE==============================================="
		sleep 2
	fi
done
