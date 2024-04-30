#!/bin/bash

TEXT="
KatBox Installer
-----------------
This will install files into ~/.local/opt/katbox/ and will add a file in ~/.local/bin to start the program.

i: install/update
r: remove from system
c: cancel
"
echo "$TEXT"

read -p "Confirm? [I/r/c]: " CONFIRM
if [ -z $CONFIRM ] || [ $CONFIRM == "i" ];
then
	if ! [ -d "~/.local/opt" ]; then mkdir ~/.local/opt; fi;
	if ! [ -d "~/.local/bin" ]; then mkdir ~/.local/bin; fi;
	
	if ! [ -d "~/.local/opt/katbox" ]; then
		mkdir ~/.local/opt/katbox;
		git clone https://github.com/KittKat7/katbox.git ~/.local/opt/katbox;
	else
		cd ~/.local/opt/katbox;
		git pull;
	fi;

	if ! [ -f "~/.local/bin/katbox" ]; then printf '#!/bin/bash\npython ~/.local/opt/katbox/katbox.py $@' > ~/.local/bin/katbox; fi;

	chmod +x ~/.local/bin/katbox

	echo "COMPLETE"
elif [ $CONFIRM == "r" ]
then
	rm -fr ~/.local/opt/katbox
	unlink ~/.local/bin/katbox
fi


