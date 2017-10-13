#!/bin/sh
LOCALVERSION="3.10"
echo "emptstr:$EMPTSTR"
echo "${LOCALVERSION}"
echo "ver:${LOCALVERSION+set}"
echo "emptstr+set:${EMPTSTR+set}"
EMPTSTR="linux-4.4"
echo "emptstr:$EMPTSTR"
echo "emptstr+set:${EMPTSTR+set}"
