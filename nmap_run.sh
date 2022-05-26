#!/usr/bin/bash

if [ $# -lt 2 ]
then
    echo "usage: $0 target_IP file_name"
else
    echo "[+] Runnig nmap to find ports"
    ports=$(sudo nmap -v -p- --min-rate=1000 -T4 $1 -oN $2-all-ports.txt | grep ^[0-9] | cut -d '/' -f1 | tr '\n' ',' | sed s/,$//)
    echo "[+] Running full scan now ==========="
    sudo nmap -v -sV -sC -O -p $ports $1 -oN $2-details.txt
    echo "[+] Running for UDP scan ============"
    sudo nmap -v -sU --top-ports 1000 -T4 $1 -oN $2-udp-ports.txt
fi
