#!/bin/bash
DEF="a b c d"
RES="1 2 3 4"
index=0
for i in $(seq $1 $2)
do
echo $i
done

for def in ${DEF};do
let index++
res=`echo ${RES} | awk -v idx=${index} '{print $idx}'`
echo $def $res
done
