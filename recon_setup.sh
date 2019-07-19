#!/bin/bash

Tools_dir='/root/Tools'

echo "=======This is to setup all the tools required for recon ======"

echo "+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++"
echo "+                            Amass                                  +"
echo "+      https://github.com/OWASP/Amass/blob/master/doc/install.md    +"
echo "+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++"
sudo apt install snapd
sudo snap install amass
sudo systemctl start snapd
sudo systemctl enable snapd
sudo systemctl start apparmor
sudo systemctl enable apparmor
echo "export PATH=$PATH:/snap/bin" >> ~/.bashrc
sleep 5
echo "+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++"
echo "+                            MassDNS                                +"
echo "+     https://github.com/blechschmidt/massdns                       +"
echo "+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++"

git clone https://github.com/blechschmidt/massdns.git $Tools_dir
cd $Tools_dir/massdns && make
echo 'alias massdns="/root/Tools/massdns/bin/massdns"' >> ~/.bashrc

echo "+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++"
echo "+                            Masscan                                +"
echo "+    https://github.com/robertdavidgraham/masscan                   +"
echo "+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++"

sudo apt-get install git gcc make libpcap-dev
git clone https://github.com/robertdavidgraham/masscan $Tools_dir
cd $Tools_dir/masscan && make
cp $Tools_dir/masscan/bin/masscan /usr/local/bin

echo "+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++"
echo "+              SecLists and filter-resolved                         +"
echo "+        https://github.com/danielmiessler/SecLists                 +"
echo "+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++"

git clone https://github.com/danielmiessler/SecLists.git $Tools_dir
go get github.com/tomnomnom/hacks/filter-resolved
echo "export PATH=$PATH:/root/go/bin" >> ~/.bashrc

