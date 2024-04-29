#!/bin/bash

TEXT="
KatBox Installer
-----------------
This will install files into ~/opt/katbox/ and will add a file in ~/.local/bin to start the program.

i: install
u: uninstall
c: cancel
"
echo "$TEXT"

read -p "Confirm? [I/u/c]: " CONFIRM
if [ -z $CONFIRM ] || [ $CONFIRM == "i" ]
then
	mkdir ~/opt
	mkdir ~/opt/katbox
	mkdir ~/.local/bin

	git clone https://github.com/KittKat7/katbox.git ~/opt/katbox
	ln -s ~/opt/katbox/katbox.sh ~/.local/bin/katbox

	chmod +x ~/.local/bin/katbox

	echo "COMPLETE"
elif [ $CONFIRM == "u" ]
then
	rm ~/opt/katbox
	unlink ~/.lical/bin/katbox
fi


