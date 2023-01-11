#!/bin/sh
reg00="00001291"
reg04="00000007"
reg08="00000000"
reg10="00001249"
reg14="00000049"
reg20="0000ffff"
reg80="00005555"
reg90="0000aaaa"
chipid="00002201"

l_reg00="00001291"
l_reg04="0000003f"
l_reg08="00000000"
l_reg10="00001249"
l_reg14="00000049"
l_reg20="0000ffff"
l_reg80="00005555"
l_reg90="0000aaaa"


j=1
jmax=200000000
while [ $j -lt $jmax ];
do
	cat /sys/kernel/debug/rkserdes/1-0055/remote0/registers/grf > /data/i2c_dump.txt
	line=`grep -r 0x0000: /data/i2c_dump.txt`
	r_reg00=`echo ${line} | awk '{print $2}'`
	r_reg04=`echo ${line} | awk '{print $3}'`
	r_reg08=`echo ${line} | awk '{print $4}'`
	line=`grep -r 0x0010: /data/i2c_dump.txt`
	r_reg10=`echo ${line} | awk '{print $2}'`
	r_reg14=`echo ${line} | awk '{print $3}'`
	line=`grep -r 0x0020: /data/i2c_dump.txt`
	r_reg20=`echo ${line} | awk '{print $2}'`
	line=`grep -r 0x0080: /data/i2c_dump.txt`
	r_reg80=`echo ${line} | awk '{print $2}'`
	line=`grep -r 0x0090: /data/i2c_dump.txt`
	r_reg90=`echo ${line} | awk '{print $2}'`
	line=`grep -r 0x0400: /data/i2c_dump.txt`
	r_chipid=`echo ${line} | awk '{print $2}'`

	if [ "$reg00" != "$r_reg00" ]; then
		echo "remote reg00 i2c read err"
		break
	elif [ "$reg04" != "$r_reg04" ]; then
		echo "remote reg04 i2c read err"
		break
	elif [ "$reg08" != "$r_reg08" ]; then
		echo "remote reg08 i2c read err"
		break
	elif [ "$reg10" != "$r_reg10" ]; then
		echo "remote reg10 i2c read err"
		break
	elif [ "$reg14" != "$r_reg14" ]; then
		echo "remote reg14 i2c read err"
		break
	elif [ "$reg20" != "$r_reg20" ]; then
		echo "remote reg20 i2c read err"
		break
	elif [ "$reg80" != "$r_reg80" ]; then
		echo "remote reg80 i2c read err"
		break
	elif [ "$reg90" != "$r_reg90" ]; then
		echo "remote reg90 i2c read err"
		break
	elif [ "$chipid" != "$r_chipid" ]; then
		echo "remote chipid i2c read err"
		break
	else
		echo "Remote Success: ${j}"
	fi

	cat /sys/kernel/debug/rkserdes/1-0055/local/registers/grf > /data/i2c_dump.txt
	line=`grep -r 0x0000: /data/i2c_dump.txt`
	r_reg00=`echo ${line} | awk '{print $2}'`
	r_reg04=`echo ${line} | awk '{print $3}'`
	r_reg08=`echo ${line} | awk '{print $4}'`
	line=`grep -r 0x0010: /data/i2c_dump.txt`
	r_reg10=`echo ${line} | awk '{print $2}'`
	r_reg14=`echo ${line} | awk '{print $3}'`
	line=`grep -r 0x0020: /data/i2c_dump.txt`
	r_reg20=`echo ${line} | awk '{print $2}'`
	line=`grep -r 0x0080: /data/i2c_dump.txt`
	r_reg80=`echo ${line} | awk '{print $2}'`
	line=`grep -r 0x0090: /data/i2c_dump.txt`
	r_reg90=`echo ${line} | awk '{print $2}'`

	if [ "$l_reg00" != "$r_reg00" ]; then
		echo "Local reg00 i2c read err"
		break
	elif [ "$l_reg04" != "$r_reg04" ]; then
		echo "Local reg04 i2c read err"
		break
	elif [ "$l_reg08" != "$r_reg08" ]; then
		echo "Local reg08 i2c read err"
		break
	elif [ "$l_reg10" != "$r_reg10" ]; then
		echo "Local reg10 i2c read err"
		break
	elif [ "$l_reg14" != "$r_reg14" ]; then
		echo "Local reg14 i2c read err"
		break
	elif [ "$l_reg20" != "$r_reg20" ]; then
		echo "Local reg20 i2c read err"
		break
	elif [ "$l_reg80" != "$r_reg80" ]; then
		echo "Local reg80 i2c read err"
		break
	elif [ "$l_reg90" != "$r_reg90" ]; then
		echo "Local reg90 i2c read err"
		break
	else
		echo "Local Success: ${j}"
	fi

	j=$((j+1))
done