#!/bin/bash
if [ $# -lt 1 ]
then
	echo "Specific the application please"
else
echo "This program will remove codesign from the specified application"
echo "Proceed with Caution"
read -p "Press enter if you want to continue CTRL + C if you want to abort"
APP_NAME=$1
	if [ -d $HOME/Applications/$APP_NAME ]
	then
		echo "Application Found in Home Directory"
		echo "removing code sign for all"
		export IFS=$'\n'
		for i in $(find $HOME/Applications/$APP_NAME -name '*.app' -type d);
		do
			echo "$i"
		done
		read -p "above list of app will have code signing removed"
		for i in $(find $HOME/Applications/$APP_NAME -name '*.app' -type d);
		do
			codesign --remove-signature "$i"
		done
		echo "Code Signing is removed, if app stops working reinstall"
	else
		echo "Application not found"
	fi

fi
