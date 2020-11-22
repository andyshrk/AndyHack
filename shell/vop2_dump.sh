#!/system/bin/sh
io -r -4 -l 0x100 0xfe040000
print
io -r -4 -l 0x100 0xfe040600
print

STAT=`cat /sys/kernel/debug/dri/0/summary  | grep "Video Port0" | grep "ACTIVE"`
if  [ "$STAT" != "" ]; then
io -r -4 -l 0x100 0xfe040c00
print
fi

STAT=`cat /sys/kernel/debug/dri/0/summary  | grep "Video Port1" | grep "ACTIVE"`
if  [ "$STAT" != "" ]; then
io -r -4 -l 0x100 0xfe040d00
print
fi

STAT=`cat /sys/kernel/debug/dri/0/summary  | grep "Video Port2" | grep "ACTIVE"`
if  [ "$STAT" != "" ]; then
io -r -4 -l 0x100 0xfe040e00
print
fi

STAT=`cat /sys/kernel/debug/dri/0/summary  | grep "Video Port3" | grep "ACTIVE"`
if  [ "$STAT" != "" ]; then
io -r -4 -l 0x100 0xfe040f00
print
fi

IDS=`cat /sys/kernel/debug/dri/0/summary  | grep win_id | awk '{print $2}' | sort`

for i in $IDS; do
    if [ $i = 0 ]; then
        echo "Cluster0: "
        io -r -4 -l 0x130 0xfe041000
    elif [ $i = 1 ]; then
        echo "Cluster1:"
        io -r -4 -l 0x130 0xfe041200
    elif [ $i = 4 ]; then
        echo "Esmart0: "
        io -r -4 -l 0x100 0xfe041800
    elif [ $i = 5 ]; then
        echo "Esmart1:"
        io -r -4 -l 0x100 0xfe041a00
    elif [ $i = 6 ]; then
        echo "Smart0:"
        io -r -4 -l 0x100 0xfe041c00
    elif [ $i = 6 ]; then
        echo "Smart1:"
        io -r -4 -l 0x100 0xfe041e00
    fi
    print
done

cat /sys/kernel/debug/dri/0/summary
