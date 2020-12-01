#!/bin/bash
figlet miniproject
# A lot has to be included with time 
# this is just the base skeleton
echo "the total number of adaptors connected to your device are as follows ->"
noadap=$(ifconfig | grep flags |cut -d " " -f 1 |cut -d ":" -f 1 |wc -l)
echo $noadap


echo " "
echo "the adaptors are as follows "
adaptors=$(ifconfig | grep flags |cut -d " " -f 1)
echo $adaptors

echo "enter the adaptor you want to use"
read adp
echo " "

adps=$(echo $adaptors | cut -d " " -f $adp)
echo  "$adps adaptor is in use"
echo " "

extract=$(ifconfig | grep netmask)

for (( i=1; i<=$adp; i++ ))
do
	if [ $i -eq $adp ]; then
		if [ $i -eq 2 ];
		then
			ips=$(echo $extract | cut -d " " -f 8);
			sub=$(echo $extract | cut -d " " -f 10);
			bda=NIL;
		elif [ $i -eq 1 ];
		then
			ips=$(echo $extract | cut -d " " -f 2);
			sub=$(echo $extract | cut -d " " -f 4);
			bda=$(echo $extract | cut -d " " -f 6);
		else 
			a=$((12+($i-3)*6));
			ips=$(echo $extract | cut -d " " -f $a);
			sub=$(echo $extract | cut -d " " -f $(($a+2)));
			bda=$(echo $extract | cut -d " " -f $(($a+4)));
		fi
	fi
done

net=$(echo $ips | cut -d "." -f 1,2,3)

echo "the ipaddress of the $adps adaptor is as follows ----->" 
echo $ips

echo "The subnet mask of the network connected to the $adps adaptor is as follows ----->"
echo $sub

echo "The broadcast address of the network is ---------->"
echo $bda

echo "=================================================="
echo "=============Starting the scan===================="
echo "=================================================="

for i in {1..254}
do
	ping -c 1 $net.$ip | grep "64 bytes" | cut -d " " -f 4 | tr -d ":" >> hosts.txt &
done

echo "Discovered hosts in local network are "
cat hosts.txt |sort > sorted_h.txt

echo "Do you want to discover open ports ? y/N"
read choice
if [ $choice =="y" ]; then
	nmap -iL sorted_h.txt | grep -v "Nmap"
elif [ $choice =="N" ]; then
	echo " "
else
	echo "Please enter a valid choice"
fi

figlet "thankyou for choosing us"

