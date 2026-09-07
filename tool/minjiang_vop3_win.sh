#!/bin/sh
CONN=`cat /sys/kernel/debug/dri/0/state  | grep " DPI-1" | awk -F '[][]' '{print $2}'`
CRTC=`cat /sys/kernel/debug/dri/0/state  | grep " video_port0" | awk -F '[][]' '{print $2}'`
C0=`cat /sys/kernel/debug/dri/0/state  | grep " Cluster0-win0" | awk -F '[][]' '{print $2}'`
C1=`cat /sys/kernel/debug/dri/0/state  | grep " Cluster1-win0" | awk -F '[][]' '{print $2}'`
E0=`cat /sys/kernel/debug/dri/0/state  | grep " Esmart0-win0" | awk -F '[][]' '{print $2}'`
E1=`cat /sys/kernel/debug/dri/0/state  | grep " Esmart1-win0" | awk -F '[][]' '{print $2}'`
M0=`cat /sys/kernel/debug/dri/0/state  | grep " Msmart0-win0" | awk -F '[][]' '{print $2}'`
M1=`cat /sys/kernel/debug/dri/0/state  | grep " Msmart1-win0" | awk -F '[][]' '{print $2}'`
MODE="800x1280"
CRTC_W=800
CRTC_H=1280

dump_summary_later()
{
    (
        sleep "${1:-1}"
        cat /sys/kernel/debug/dri/0/summary
    ) &
}

echo "Conn: $CONN"
echo "Mode: $MODE"
echo "RGB: $RGB"
echo "DSI: $DSI"
echo "VP: $CRTC"
echo "Cluster0: $C0"
echo "Cluster1: $C1"
echo "Esmart0: $E0"
echo "Esmart1: $E1"
echo "Msmart0: $M0"
echo "Msmart1: $M1"

echo "W $CRTC_Wx"
if [ $# -eq 0 ]; then
dump_summary_later
modetest -M rockchip -s $CONN@$CRTC:${CRTC_W}x${CRTC_H}
elif [ "$1" = "0" ]; then
dump_summary_later
modetest -M rockchip -s $CONN@$CRTC:${CRTC_W}x${CRTC_H}
elif [ "$1" = "1" ]; then
dump_summary_later
/data/ovltest -M rockchip -s $CONN@$CRTC:${CRTC_W}x${CRTC_H} -P $C0@$CRTC:800x1280@RG24@afbc32x8split -F /data/800x1280_RGB888_AFBC32x8_TVtest.bin
elif [ "$1" = "2" ]; then
dump_summary_later
/data/ovltest -M rockchip -s $CONN@$CRTC:${CRTC_W}x${CRTC_H} -P $C0@$CRTC:800x1280@AB24 -F /data/800x1280-AB24-Alauncher-blue.bin 
elif [ "$1" = "3" ]; then
dump_summary_later
/data/ovltest -M rockchip -s $CONN@$CRTC:${CRTC_W}x${CRTC_H} -P $C0@$CRTC:960x540:800x540@AB24 -F /data/wukong_z0_960x540_XB24.bin 
elif [ "$1" = "4" ]; then
dump_summary_later
/data/ovltest -M rockchip -s $CONN@$CRTC:${CRTC_W}x${CRTC_H} -P $C0@$CRTC:960x540:600x500@XB24 -F /data/wukong_z0_960x540_XB24.bin 
elif [ "$1" = "5" ]; then
dump_summary_later
/data/ovltest -M rockchip -s $CONN@$CRTC:${CRTC_W}x${CRTC_H} -P $C0@$CRTC:1920x1080:800x600@NV12 -F /data/1920x1080_yuv420-flower.bin 
elif [ "$1" = "6" ]; then
dump_summary_later
/data/ovltest -M rockchip -s $CONN@$CRTC:${CRTC_W}x${CRTC_H} -P $C0@$CRTC:1280x720:800x500@BG24 -F /data/1280x720-RGB888-flower.bin 
elif [ "$1" = "7" ]; then
dump_summary_later 2
/data/ovltest -M rockchip -s $CONN@$CRTC:${CRTC_W}x${CRTC_H} -P $C0@$CRTC:3840x2160:800x1280@AB24@afbc32x8split -F /data/3840x2160_AB24_AFBC32x8_ALauncher.bin 
elif [ "$1" = "8" ]; then
dump_summary_later
/data/ovltest -M rockchip -s $CONN@$CRTC:${CRTC_W}x${CRTC_H} -P $C0@$CRTC:800x1280:400x640@RG24@afbc32x8split -F /data/800x1280_RGB888_AFBC32x8_TVtest.bin 
elif [ "$1" = "9" ]; then
dump_summary_later
/data/ovltest -M rockchip -s $CONN@$CRTC:${CRTC_W}x${CRTC_H} -P $C0@$CRTC:1920x1080:400x360@AB24@afbc32x8split -F /data/1920x1088_AB24_AFBC32x8_dangbei.bin
elif [ "$1" = "10" ]; then
dump_summary_later 2
/data/ovltest -M rockchip -s $CONN@$CRTC:${CRTC_W}x${CRTC_H} -P $C0@$CRTC:3840x2160:800x600@NV12 -F /data/3840x2160_NV12_valley.bin 
elif [ "$1" = "11" ]; then
dump_summary_later 2
/data/ovltest -M rockchip -s $CONN@$CRTC:${CRTC_W}x${CRTC_H} -P $C0@$CRTC:3840x2160:800x500@AB24 -F /data/3840x2160_AB24_ASettings.bin 
elif [ "$1" = "12" ]; then
dump_summary_later 2
/data/ovltest -M rockchip -s $CONN@$CRTC:${CRTC_W}x${CRTC_H} -P $C0@$CRTC:4096x2160:800x500@RG16 -F /data/4096x2160_RGB565_roulette.bin 
elif [ "$1" = "13" ]; then
dump_summary_later
/data/ovltest -M rockchip -s $CONN@$CRTC:${CRTC_W}x${CRTC_H} -P $C0@$CRTC:1920x1080:800x540@AB24@afbc32x8split -F /data/wukong_z1_1920x1088_AB24_AFBC32x8.bin 
elif [ "$1" = "14" ]; then
dump_summary_later
/data/ovltest -M rockchip -s $CONN@$CRTC:${CRTC_W}x${CRTC_H} -P $C0@$CRTC:800x1280@AB24 -F /data/800x1280-AB24-App-white.bin  
elif [ "$1" = "15" ]; then
dump_summary_later
/data/ovltest -M rockchip -s $CONN@$CRTC:${CRTC_W}x${CRTC_H} -P $C0@$CRTC:1920x1080:800x640@AB24@afbc32x8split -F /data/1920x1088_AB24_AFBC32x8_dangbei.bin
elif [ "$1" = "16" ]; then
dump_summary_later
/data/ovltest -M rockchip -s $CONN@$CRTC:${CRTC_W}x${CRTC_H} -P $C0@$CRTC:1920x1080:800x540@AB24 -F /data/1920x1080-ABGR8888-Boxlanuncher.bin 
elif [ "$1" = "17" ]; then
dump_summary_later
/data/ovltest -M rockchip -s $CONN@$CRTC:${CRTC_W}x${CRTC_H} -P $C0@$CRTC:960x540:800x400@AB24 -F /data/wukong_z0_960x540_XB24.bin 
elif [ "$1" = "18" ]; then
dump_summary_later
/data/ovltest -M rockchip -s $CONN@$CRTC:${CRTC_W}x${CRTC_H} -P $C0@$CRTC:960x540:200x140@AB24 -F /data/wukong_z0_960x540_XB24.bin 
elif [ "$1" = "19" ]; then
/data/ovltest -M rockchip -s $CONN@$CRTC:${CRTC_W}x${CRTC_H} -P $C0@$CRTC:960x540:480x270@AB24 -F /data/wukong_z0_960x540_XB24.bin 
elif [ "$1" = "19" ]; then
dump_summary_later
/data/ovltest -M rockchip -s $CONN@$CRTC:${CRTC_W}x${CRTC_H} -P $C0@$CRTC:1920x1080:800x540@NV12 -F /data/1920x1080_yuv420-flower.bin 
elif [ "$1" = "20" ]; then
dump_summary_later
/data/ovltest -M rockchip -s $CONN@$CRTC:${CRTC_W}x${CRTC_H} -P $C0@$CRTC:1280x720:640x320@BG24 -F /data/1280x720-RGB888-flower.bin 
elif [ "$1" = "21" ]; then
dump_summary_later
/data/ovltest -M rockchip -s $CONN@$CRTC:${CRTC_W}x${CRTC_H} -P $C0@$CRTC:1920x1080:800x540@AB24@afbc32x8split -F /data/wukong2_z1_1920x1088_AB24_AFBC32x8.bin 
elif [ "$1" = "22" ]; then
dump_summary_later 2
/data/ovltest -M rockchip -s $CONN@$CRTC:${CRTC_W}x${CRTC_H} -P $C0@$CRTC:3840x2160:1920x1080@AB24@afbc32x8 -F /data/3840x2160_AB24_AFBC32x8_ALauncher.bin
elif [ "$1" = "23" ]; then
dump_summary_later 2
/data/ovltest -M rockchip -s $CONN@$CRTC:${CRTC_W}x${CRTC_H} -P $C0@$CRTC:4096x2048:1920x1080@AR24@afbc -F /data/4096x2048_ARGB8888_afbc.bin 
elif [ "$1" = "24" ]; then
dump_summary_later 2
/data/ovltest -M rockchip -s $CONN@$CRTC:${CRTC_W}x${CRTC_H} -P $C0@$CRTC:4096x2160:800x500@BG24 -F /data/4096x2160_RBG888_roulette.bin 
elif [ "$1" = "25" ]; then
dump_summary_later 2
/data/ovltest -M rockchip -s $CONN@$CRTC:${CRTC_W}x${CRTC_H} -P $C0@$CRTC:3840x2160:800x540@AB24 -F /data/3840x2160_AB24_ASettings.bin 
elif [ "$1" = "26" ]; then
dump_summary_later 2
/data/ovltest -M rockchip -s $CONN@$CRTC:${CRTC_W}x${CRTC_H} -P $C0@$CRTC:3840x2160:800x540@AB30 -F /data/3840x2160_AB30_NBA.bin 
elif [ "$1" = "27" ]; then
dump_summary_later
/data/ovltest -M rockchip -s $CONN@$CRTC:${CRTC_W}x${CRTC_H} -P $E0@$CRTC:1920x1080:800x640@XB24 -P $C0@$CRTC:1920x1080:800x640@AB24@afbc32x8split -F /data/wukong2_z0_1920x1080_XB24.bin -F /data/wukong2_z1_1920x1088_AB24_AFBC32x8.bin  
elif [ "$1" = "28" ]; then
dump_summary_later
/data/ovltest -M rockchip -s $CONN@$CRTC:${CRTC_W}x${CRTC_H} -P $E0@$CRTC:960x540:800x500@XB24 -P $C0@$CRTC:1920x1080:800x500@AB24@afbc32x8split  -F /data/wukong_z0_960x540_XB24.bin -F /data/wukong_z1_1920x1088_AB24_AFBC32x8.bin
elif [ "$1" = "29" ]; then
dump_summary_later
modetest -M rockchip -s $CONN@$CRTC:${CRTC_W}x${CRTC_H} -P $E0@$CRTC:800x1280@XB30
elif [ "$1" = "30" ]; then
dump_summary_later
/data/ovltest -M rockchip -s $CONN@$CRTC:${CRTC_W}x${CRTC_H} -P $E0@$CRTC:1920x1080:800x640@AB24 -F /data/1920x1080-ABGR8888-Boxlanuncher.bin 
elif [ "$1" = "31" ]; then
dump_summary_later
/data/ovltest -M rockchip -s $CONN@$CRTC:${CRTC_W}x${CRTC_H} -P $E0@$CRTC:960x540:800x600@XB24 -F /data/wukong_z0_960x540_XB24.bin 
elif [ "$1" = "32" ]; then
dump_summary_later
/data/ovltest -M rockchip -s $CONN@$CRTC:${CRTC_W}x${CRTC_H} -P $E0@$CRTC:1920x1080:800x540@NV12 -F /data/1920x1080_yuv420-flower.bin 
elif [ "$1" = "33" ]; then
dump_summary_later
/data/ovltest -M rockchip -s $CONN@$CRTC:${CRTC_W}x${CRTC_H} -P $E0@$CRTC:1280x720:800x600@BG24 -F /data/1280x720-RGB888-flower.bin 
elif [ "$1" = "34" ]; then
dump_summary_later 2
/data/ovltest -M rockchip -s $CONN@$CRTC:${CRTC_W}x${CRTC_H} -P $E0@$CRTC:4096x2160:800x500@RG16 -F /data/4096x2160_RGB565_roulette.bin 
elif [ "$1" = "35" ]; then
dump_summary_later
/data/ovltest -M rockchip -s $CONN@$CRTC:${CRTC_W}x${CRTC_H} -P $E0@$CRTC:1920x1080:800x540@AB30 -F /data/1920x1080_AB30_Sun.bin 
elif [ "$1" = "36" ]; then
dump_summary_later 2
/data/ovltest -M rockchip -s $CONN@$CRTC:${CRTC_W}x${CRTC_H} -P $E0@$CRTC:3840x2160:800x540@AB30 -F /data/3840x2160_AB30_NBA.bin 
elif [ "$1" = "37" ]; then
dump_summary_later 2
/data/ovltest -M rockchip -s $CONN@$CRTC:${CRTC_W}x${CRTC_H} -P $E0@$CRTC:640x360:800x500@NV12 -F /data/640x360_NV12_car.bin
elif [ "$1" = "38" ]; then
dump_summary_later
/data/ovltest -M rockchip -s $CONN@$CRTC:${CRTC_W}x${CRTC_H} -P $E0@$CRTC:640x360@NV12 -F /data/640x360_NV12_car.bin
elif [ "$1" = "39" ]; then
dump_summary_later
/data/ovltest -M rockchip -s $CONN@$CRTC:${CRTC_W}x${CRTC_H} -P $E0@$CRTC:640x360:800x720@NV12 -F /data/640x360_NV12_car.bin
elif [ "$1" = "40" ]; then
dump_summary_later
/data/ovltest -M rockchip -s $CONN@$CRTC:${CRTC_W}x${CRTC_H} -P $M0@$CRTC:1920x1080:800x600@AB24 -F /data/1920x1080-ABGR8888-Boxlanuncher.bin 
elif [ "$1" = "41" ]; then
dump_summary_later
/data/ovltest -M rockchip -s $CONN@$CRTC:${CRTC_W}x${CRTC_H} -P $M0@$CRTC:960x540:800x500@XB24 -F /data/wukong_z0_960x540_XB24.bin 
elif [ "$1" = "42" ]; then
dump_summary_later
/data/ovltest -M rockchip -s $CONN@$CRTC:${CRTC_W}x${CRTC_H} -P $M0@$CRTC:1920x1080:600x360@NV12 -F /data/1920x1080_yuv420-flower.bin 
elif [ "$1" = "43" ]; then
dump_summary_later
/data/ovltest -M rockchip -s $CONN@$CRTC:${CRTC_W}x${CRTC_H} -P $M0@$CRTC:1280x720:800x500@BG24 -F /data/1280x720-RGB888-flower.bin 
elif [ "$1" = "44" ]; then
dump_summary_later 2
/data/ovltest -M rockchip -s $CONN@$CRTC:${CRTC_W}x${CRTC_H} -P $M0@$CRTC:4096x2160:800x500@RG16 -F /data/4096x2160_RGB565_roulette.bin 
elif [ "$1" = "45" ]; then
dump_summary_later
/data/ovltest -M rockchip -s $CONN@$CRTC:${CRTC_W}x${CRTC_H} -P $M0@$CRTC:1920x1080:800x540@AB30 -F /data/1920x1080_AB30_Sun.bin 
elif [ "$1" = "46" ]; then
dump_summary_later 2
/data/ovltest -M rockchip -s $CONN@$CRTC:${CRTC_W}x${CRTC_H} -P $M0@$CRTC:3840x2160:800x540@AB30 -F /data/3840x2160_AB30_NBA.bin 
elif [ "$1" = "47" ]; then
dump_summary_later 2
/data/ovltest -M rockchip -s $CONN@$CRTC:${CRTC_W}x${CRTC_H} -P $M0@$CRTC:4096x2160:800x400@AB30 -F /data/4096x2160_AB30_roulette.bin 
elif [ "$1" = "48" ]; then
dump_summary_later
/data/ovltest -M rockchip -s $CONN@$CRTC:${CRTC_W}x${CRTC_H} -P $E0@$CRTC:640x360@NV12 -F /data/640x360_NV12_car.bin
elif [ "$1" = "49" ]; then
dump_summary_later
/data/ovltest -M rockchip -s $CONN@$CRTC:${CRTC_W}x${CRTC_H} -P $M0@$CRTC:1920x1080:800x540@NV12 -F /data/1920x1080_yuv420-flower.bin 
elif [ "$1" = "50" ]; then
dump_summary_later
/data/ovltest -M rockchip -s $CONN@$CRTC:${CRTC_W}x${CRTC_H} -P $C0@$CRTC:1920x1080:800x1080@XR24@afrc16scan -F /data/1920x1080-ARGB8888-AFRC16-SCAN-flower.bin
elif [ "$1" = "51" ]; then
dump_summary_later
/data/ovltest -M rockchip -s $CONN@$CRTC:${CRTC_W}x${CRTC_H} -P $C0@$CRTC:1920x1080:800x1080@XR24@afrc24scan -F /data/1920x1080-ARGB8888-AFRC24-SCAN-flower.bin
elif [ "$1" = "52" ]; then
dump_summary_later
/data/ovltest -M rockchip -s $CONN@$CRTC:${CRTC_W}x${CRTC_H} -P $C0@$CRTC:1920x1080:800x1080@XR24@afrc32scan -F /data/1920x1080-ARGB8888-AFRC32-SCAN-flower.bin
elif [ "$1" = "53" ]; then
dump_summary_later
/data/ovltest -M rockchip -s $CONN@$CRTC:${CRTC_W}x${CRTC_H} -P $C0@$CRTC:1920x1080:800x1080@RG24@afrc16scan -F /data/1920x1080-RGB888-AFRC16-SCAN-flower.bin
elif [ "$1" = "54" ]; then
dump_summary_later
/data/ovltest -M rockchip -s $CONN@$CRTC:${CRTC_W}x${CRTC_H} -P $C0@$CRTC:1920x1080:800x1080@RG24@afrc24scan -F /data/1920x1080-RGB888-AFRC24-SCAN-flower.bin
elif [ "$1" = "55" ]; then
dump_summary_later
/data/ovltest -M rockchip -s $CONN@$CRTC:${CRTC_W}x${CRTC_H} -P $C0@$CRTC:1920x1080:800x1080@RG24@afrc32scan -F /data/1920x1080-RGB888-AFRC32-SCAN-flower.bin
else
dump_summary_later
/data/ovltest -M rockchip -s $CONN@$CRTC:${CRTC_W}x${CRTC_H} -P $C0@$CRTC:800x1280@AB24@ -F /data/800x1280-AB24-Alockscreen-z0.bin 
fi
