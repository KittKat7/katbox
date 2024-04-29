#!/bin/bash

TEXT="
KatBox Installer
-----------------
This will install files into ~/opt/katbox/ and will add a file in ~/.local/bin to start the program.
"
echo "$TEXT"

read -p "Confirm? [Y/n]: " CONFIRM
if [ -z $CONFIRM ] || [ $CONFIRM == "y" ]
then
	mkdir ~/opt
	mkdir ~/opt/katbox
	mkdir ~/.local/bin

	git clone https://github.com/KittKat7/katbox.git ~/opt/katbox
	ln -s ~/opt/katbox/katbox.sh ~/.local/bin/katbox

	chmod +x ~/.local/bin/katbox

	echo "COMPLETE"
fi


