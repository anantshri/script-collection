#!/bin/bash
VBOX_LOC="Genymotion"
if [ -f "$HOME/Applications/Genymotion.app/Contents/MacOS/player" ]
then
	GENY_LOC="$HOME/Applications/Genymotion.app/Contents/MacOS/player"
else
	GENY_LOC="/Applications/Genymotion.app/Contents/MacOS/player"
fi
if [ $# -gt 1 ]
then

	if [ $1 == "start" ]
	then
		$GENY_LOC --vm-name "$2"
	fi

else
	echo "You need to pass arguments"
	echo "List of exisiting genymotion VM is listed for reference"
	echo " "
	VBoxManage list vms -l | grep ".vbox" | grep $VBOX_LOC | cut -f7 -d"/"
	echo " "
fi
