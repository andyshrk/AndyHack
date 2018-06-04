#!/bin/sh
awk '{if (NR > 1) {addr=strtonum("0x"$1); for(i=2; i <= NF; i++) {printf("%x: \t %s \n", addr, $i); addr +=4}} }' d.S 
