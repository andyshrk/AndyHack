#!/bin/sh
for i in ./*;do
  echo ${i##*/}
done

find c_hack/* -type f ! -name *.c
