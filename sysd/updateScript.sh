#!/bin/bash
updatePath=$1
currentPath=$2
serviceName=$3
updateService=$4

echo "=========Script starts here=========" >> update.log
date >> update.log
echo "Start update... Try to stop $serviceName" >> update.log
sudo systemctl stop $serviceName
rm -rf $updatePath/*.msi >> update.log 2>> update.log
rm -rf $updatePath/Source >> update.log 2>> update.log

echo "Unzip whole package" >> update.log
unzip -j -o $updatePath/Pilot-update*.zip -d $updatePath >> update.log 2>> update.log
rm $updatePath/Pilot-update*.zip >> update.log 2>> update.log

echo "Unzip update package" >> update.log
unzip $updatePath/*.zip -d $updatePath/pilot-server/ >> update.log 2>> update.log

if [ -e "settings.xml" ]
then
	rm -f $updatePath/pilot-server/settings.xml >> update.log 2>> update.log
	echo "Settings were removed!" >> update.log
fi
if [ -e "ldapServerSettings.xml" ]
then
	rm -f $updatePath/pilot-server/ldapServerSettings.xml >> update.log 2>> update.log
	echo "LDAPServerSettings were removed!" >> update.log
fi

echo "Copy files" >> update.log
cp $updatePath/pilot-server/* "$currentPath" -R >> update.log 2>> update.log
rm $updatePath/*.zip >> update.log 2>> update.log
rm -rf $updatePath/pilot-server >> update.log 2>> update.log

echo "Try to start $serviceName" >> update.log
sudo systemctl start $serviceName
echo "Try to stop $updateService" >> update.log
sudo systemctl stop $updateService

echo "=========Script ends here=========" >> update.log