#!/bin/bash

echo "----------MENU------------"
echo "1. Use fast scan"
echo "2. use the python scanner to knwo by hostname"
echo "3. use advanced scanner with gui"
echo "4. use scanner to discover hostnames ,mac address etc."
read choice

if [ $choice -eq 1 ]; then
	./net_strt.sh
elif [ $choice -eq 2 ]; then
	python3 scanner.py
elif [ $choice -eq 3 ]; then
	python mp.py
elif [ $choice -eq 3 ]; then
	python ./python-network-scanner/main.py
fi



