#!/bin/sh
# am patchs from pwclient;
only_get=false
IDS=`pwclient list -p uboot -w "philipp.tomsich@theobroma-systems.com" | sed -n '/8238/p' | awk '{print $1}'`
echo "commits id: ${IDS}"
for i in ${IDS}; do
if $only_get; then
	pwclient get -p uboot $i
else
	pwclient git-am -p uboot $i
	if [ $? != 0 ]; then
		only_get=true
		pwclient get -p uboot $i
	fi
fi
done
