#!/usr/bin/bash

if [ $# -lt 1 ]
then
    echo "usage: $0 target_IP file_name"
else
    echo "[+] Runnig nmap to find ports"
    ports=$(sudo nmap -v -p- --min-rate=1000 -T4 -Pn $1 -oN $2-all-ports.txt | grep ^[0-9] | cut -d '/' -f1 | tr '\n' ',' | sed s/,$//)
    sleep 2
    echo "[+] Running full scan now ==========="
    sudo nmap -v -sV -sC -Pn -O -p $ports $1 -oA $2-details
fi
