#!/bin/sh
VRES=1280
VBP=11
VFP=22
VSYNC=4
HRES=720
HBP=40
HFP=40
HSYNC=10
HTOTAL=`expr $HBP + $HSYNC + $HRES + $HFP`
VTOTAL=`expr $VBP + $VSYNC + $VRES + $VFP`
VADJ=100
NVBP=`expr $VBP + $VADJ`
VTOTAL=`expr $VTOTAL + $VADJ`
LVREG=`expr $VTOTAL \* 65536 + $VSYNC`
VTOTALREG=`printf "0x%x" $LVREG`
VST=`expr $VBP + $VSYNC + $VADJ`
LVST=`expr $VST \* 65536 + $VST + $VRES`
VSTREG=`printf "0x%x" $LVST`
echo $VTOTALREG
echo $VSTREG

while true 
do
#io -w -4 0xff450058 $NVBP
io -w -4 0xff460108 $VTOTALREG
#io -w -4 0xff46010c $VSTREG
io -w -4 0xff460000 1
sleep 5
#io -w -4 0xff450058 0xb
io -w -4 0xff460108 0x5250004
#io -w -4 0xff46010c 0x000f050f
io -w -4 0xff460000 1
sleep 5
done
