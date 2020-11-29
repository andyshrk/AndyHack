#!/system/bin/sh
echo "SYS:"
io -r -4 -l 0x100 0xfe040000
print
echo "OVL:"
io -r -4 -l 0x100 0xfe040600
print

STAT=`cat /sys/kernel/debug/dri/0/summary  | grep "Video Port0" | grep "ACTIVE"`
if  [ "$STAT" != "" ]; then
	echo "VP0:"
	io -r -4 -l 0x100 0xfe040c00
	print
fi

STAT=`cat /sys/kernel/debug/dri/0/summary  | grep "Video Port1" | grep "ACTIVE"`
if  [ "$STAT" != "" ]; then
	echo "VP1:"
	io -r -4 -l 0x100 0xfe040d00
	print
fi

STAT=`cat /sys/kernel/debug/dri/0/summary  | grep "Video Port2" | grep "ACTIVE"`
if  [ "$STAT" != "" ]; then
	echo "VP2:"
	io -r -4 -l 0x100 0xfe040e00
	print
fi

STAT=`cat /sys/kernel/debug/dri/0/summary  | grep "Video Port3" | grep "ACTIVE"`
if  [ "$STAT" != "" ]; then
	echo "VP3:"
	io -r -4 -l 0x100 0xfe040f00
	print
fi

STAT=`cat /sys/kernel/debug/dri/0/summary  | grep "Cluster0-win0" | grep "ACTIVE"`
if  [ "$STAT" != "" ]; then
	echo "Cluster0: "
	io -r -4 -l 0x130 0xfe041000
	print
fi

STAT=`cat /sys/kernel/debug/dri/0/summary  | grep "Cluster1-win0" | grep "ACTIVE"`
if  [ "$STAT" != "" ]; then
	echo "Cluster1: "
	io -r -4 -l 0x130 0xfe041200
	print
fi

STAT=`cat /sys/kernel/debug/dri/0/summary  | grep "Esmart0-win0" | grep "ACTIVE"`
if  [ "$STAT" != "" ]; then
	echo "Esmart0: "
	io -r -4 -l 0x100 0xfe041800
	print
fi

STAT=`cat /sys/kernel/debug/dri/0/summary  | grep "Esmart1-win0" | grep "ACTIVE"`
if  [ "$STAT" != "" ]; then
	echo "Esmart1: "
	io -r -4 -l 0x100 0xfe041a00
	print
fi

STAT=`cat /sys/kernel/debug/dri/0/summary  | grep "Smart0-win0" | grep "ACTIVE"`
if  [ "$STAT" != "" ]; then
	echo "Smart0: "
	io -r -4 -l 0x100 0xfe041c00
	print
fi

STAT=`cat /sys/kernel/debug/dri/0/summary  | grep "Smart1-win0" | grep "ACTIVE"`
if  [ "$STAT" != "" ]; then
	echo "Smart1: "
	io -r -4 -l 0x100 0xfe041e00
	print
fi

cat /sys/kernel/debug/dri/0/summary
