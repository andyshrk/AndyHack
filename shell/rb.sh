#!/bin/bash
# Written by Andy Yan <andyshrk@gmail.com>
RESULT=""
JOB=`sed -n "N;/processor/p" /proc/cpuinfo|wc -l`
build_board()
{
	local defconfig toolchain subdir dstdir 
	defconfig=$1
	subdir=`echo ${defconfig} | awk -F [_-] '{if(NF==3) print $2; if(NF==2) print $1}'`
	dstdir=rockdev/${subdir}
	if [ ! -d ${dstdir} ]; then
		mkdir -p ${dstdir}
	fi
	make ${defconfig} O=${dstdir}/out
	if grep  -q '^CONFIG_ARM64=y' ${dstdir}/out/.config ; then
		echo "ARM64"
		toolchain=aarch64-linux-gnu-
	else
		echo "ARM32"
		toolchain=arm-linux-gnueabi-
	fi
	make  CROSS_COMPILE=${toolchain} all  --jobs=${JOB} O=${dstdir}/out
	if [ $? -eq 0 ]; then
		RESULT=${RESULT}"Success "
	else
		RESULT=${RESULT}"Failed "
	fi
}

show_result()
{
	local index
	index=0
	echo ${RESULT} | awk '{print NF}'
	for i in ${DEFCONFIGS}; do
		let index++
		echo ${RESULT} | awk '{printf "%-50s %s\n", board, $idx}' board=${i} idx=${index}
	done
}

make distclean
DEFCONFIGS=`grep -lr CONFIG_ARCH_ROCKCHIP configs/* | awk -F / '{print $2}'`
for i in ${DEFCONFIGS}; do
build_board ${i}
done
show_result
