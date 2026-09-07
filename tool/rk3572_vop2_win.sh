#!/system/bin/sh
CONN=`cat /sys/kernel/debug/dri/0/state  | grep " HDMI-A-1" | awk -F '[][]' '{print $2}'`
CRTC=`cat /sys/kernel/debug/dri/0/state  | grep " video_port0" | awk -F '[][]' '{print $2}'`
C0=`cat /sys/kernel/debug/dri/0/state  | grep " Cluster0-win0" | awk -F '[][]' '{print $2}'`
C1=`cat /sys/kernel/debug/dri/0/state  | grep " Cluster1-win0" | awk -F '[][]' '{print $2}'`
E0=`cat /sys/kernel/debug/dri/0/state  | grep " Esmart0-win0" | awk -F '[][]' '{print $2}'`
E1=`cat /sys/kernel/debug/dri/0/state  | grep " Esmart1-win0" | awk -F '[][]' '{print $2}'`
M0=`cat /sys/kernel/debug/dri/0/state  | grep " Msmart0-win0" | awk -F '[][]' '{print $2}'`
M1=`cat /sys/kernel/debug/dri/0/state  | grep " Msmart1-win0" | awk -F '[][]' '{print $2}'`
MODE="1920x1080"
CRTC_W=1920
CRTC_H=1080
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
modetest -M rockchip -s $CONN@$CRTC:${CRTC_W}x${CRTC_H}
elif [ "$1" = "0" ]; then
modetest -M rockchip -s $CONN@$CRTC:${CRTC_W}x${CRTC_H}
elif [ "$1" = "1" ]; then
/data/ovltest -M rockchip -s $CONN@$CRTC:${CRTC_W}x${CRTC_H} -P $C1@$CRTC:1920x1080@AB24@afbc32x8 -F /data/1920x1088_AB24_AFBC32x8_dangbei.bin
elif [ "$1" = "2" ]; then
/data/ovltest -M rockchip -s $CONN@$CRTC:${CRTC_W}x${CRTC_H} -P $C1@$CRTC:1920x1080@AB24 -F /data/1920x1080-ABGR8888-Boxlanuncher.bin 
elif [ "$1" = "3" ]; then
/data/ovltest -M rockchip -s $CONN@$CRTC:${CRTC_W}x${CRTC_H} -P $C1@$CRTC:960x540@AB24 -F /data/wukong_z0_960x540_XB24.bin 
elif [ "$1" = "4" ]; then
/data/ovltest -M rockchip -s $CONN@$CRTC:${CRTC_W}x${CRTC_H} -P $C1@$CRTC:960x540:1920x1080@XB24 -F /data/wukong_z0_960x540_XB24.bin 
elif [ "$1" = "5" ]; then
/data/ovltest -M rockchip -s $CONN@$CRTC:${CRTC_W}x${CRTC_H} -P $C1@$CRTC:1920x1080@NV12 -F /data/1920x1080_yuv420-flower.bin 
elif [ "$1" = "6" ]; then
/data/ovltest -M rockchip -s $CONN@$CRTC:${CRTC_W}x${CRTC_H} -P $C1@$CRTC:1280x720@BG24 -F /data/1280x720-RGB888-flower.bin 
elif [ "$1" = "7" ]; then
/data/ovltest -M rockchip -s $CONN@$CRTC:${CRTC_W}x${CRTC_H} -P $C1@$CRTC:3840x2160:960x540@AB24@afbc32x8 -F /data/3840x2160_AB24_AFBC32x8_ALauncher.bin 
elif [ "$1" = "8" ]; then
/data/ovltest -M rockchip -s $CONN@$CRTC:${CRTC_W}x${CRTC_H} -P $C1@$CRTC:3840x2160:1920x1080@AB24@afbc32x8 -F /data/3840x2160_AB24_AFBC32x8_ALauncher.bin 
elif [ "$1" = "9" ]; then
/data/ovltest -M rockchip -s $CONN@$CRTC:${CRTC_W}x${CRTC_H} -P $C1@$CRTC:4096x2160:1024x540@BG24 -F /data/4096x2160_RBG888_roulette.bin 
elif [ "$1" = "10" ]; then
/data/ovltest -M rockchip -s $CONN@$CRTC:${CRTC_W}x${CRTC_H} -P $C1@$CRTC:4096x2160:1920x1080@BG24 -F /data/4096x2160_RBG888_roulette.bin 
elif [ "$1" = "11" ]; then
/data/ovltest -M rockchip -s $CONN@$CRTC:${CRTC_W}x${CRTC_H} -P $C1@$CRTC:3840x2160:1920x1080@AB24 -F /data/3840x2160_AB24_ASettings.bin 
elif [ "$1" = "12" ]; then
/data/ovltest -M rockchip -s $CONN@$CRTC:${CRTC_W}x${CRTC_H} -P $C1@$CRTC:4096x2160:1920x1080@RG16 -F /data/4096x2160_RGB565_roulette.bin 
elif [ "$1" = "13" ]; then
:
elif [ "$1" = "14" ]; then
:
elif [ "$1" = "15" ]; then
/data/ovltest -M rockchip -s $CONN@$CRTC:${CRTC_W}x${CRTC_H} -P $C0@$CRTC:1920x1080@AB24@afbc32x8 -F /data/1920x1088_AB24_AFBC32x8_dangbei.bin
elif [ "$1" = "16" ]; then
/data/ovltest -M rockchip -s $CONN@$CRTC:${CRTC_W}x${CRTC_H} -P $C0@$CRTC:1920x1080@AB24 -F /data/1920x1080-ABGR8888-Boxlanuncher.bin 
elif [ "$1" = "17" ]; then
/data/ovltest -M rockchip -s $CONN@$CRTC:${CRTC_W}x${CRTC_H} -P $C0@$CRTC:960x540@AB24 -F /data/wukong_z0_960x540_XB24.bin 
elif [ "$1" = "18" ]; then
/data/ovltest -M rockchip -s $CONN@$CRTC:${CRTC_W}x${CRTC_H} -P $C0@$CRTC:960x540:1920x1080@XB24 -F /data/wukong_z0_960x540_XB24.bin 
elif [ "$1" = "19" ]; then
/data/ovltest -M rockchip -s $CONN@$CRTC:${CRTC_W}x${CRTC_H} -P $C0@$CRTC:1920x1080@NV12 -F /data/1920x1080_yuv420-flower.bin 
elif [ "$1" = "20" ]; then
/data/ovltest -M rockchip -s $CONN@$CRTC:${CRTC_W}x${CRTC_H} -P $C0@$CRTC:1280x720@BG24 -F /data/1280x720-RGB888-flower.bin 
elif [ "$1" = "21" ]; then
:	
elif [ "$1" = "22" ]; then
/data/ovltest -M rockchip -s $CONN@$CRTC:${CRTC_W}x${CRTC_H} -P $C1@$CRTC:3840x2160:1920x1080@AB24@afbc32x8 -F /data/3840x2160_AB24_AFBC32x8_ALauncher.bin
elif [ "$1" = "23" ]; then
/data/ovltest -M rockchip -s $CONN@$CRTC:${CRTC_W}x${CRTC_H} -P $C1@$CRTC:4096x2048:1920x1080@AR24@afbc -F /data/4096x2048_ARGB8888_afbc.bin 
elif [ "$1" = "24" ]; then
/data/ovltest -M rockchip -s $CONN@$CRTC:${CRTC_W}x${CRTC_H} -P $C1@$CRTC:4096x2160:1920x1080@RB24 -F /data/4096x2160_RBG888_roulette.bin 
elif [ "$1" = "25" ]; then
/data/ovltest -M rockchip -s $CONN@$CRTC:${CRTC_W}x${CRTC_H} -P $C1@$CRTC:3840x2160:1920x1080@AB24 -F /data/3840x2160_AB24_ASettings.bin 
elif [ "$1" = "26" ]; then
/data/ovltest -M rockchip -s $CONN@$CRTC:${CRTC_W}x${CRTC_H} -P $C1@$CRTC:4096x2160:1920x1080@RG16 -F /data/4096x2160_RGB565_roulette.bin 
elif [ "$1" = "27" ]; then
/data/ovltest -M rockchip -s $CONN@$CRTC:${CRTC_W}x${CRTC_H} -P $C0@$CRTC:1920x1080@XB24 -P $C1@$CRTC:1920x1080@AB24@afbc32x8 -F /data/wukong2_z0_1920x1080_XB24.bin -F /data/wukong2_z1_1920x1088_AB24_AFBC32x8.bin  
elif [ "$1" = "28" ]; then
/data/ovltest -M rockchip -s $CONN@$CRTC:${CRTC_W}x${CRTC_H} -P $C0@$CRTC:960x540:1920x1080@XB24 -P $C1@$CRTC:1920x1080@AB24@afbc32x8  -F /data/wukong_z0_960x540_XB24.bin -F /data/wukong_z1_1920x1088_AB24_AFBC32x8.bin
elif [ "$1" = "29" ]; then
modetest -M rockchip -s $CONN@$CRTC:${CRTC_W}x${CRTC_H} -P $E0@$CRTC:1920x1080@XB30
elif [ "$1" = "30" ]; then
/data/ovltest -M rockchip -s $CONN@$CRTC:${CRTC_W}x${CRTC_H} -P $E0@$CRTC:1920x1080@AB24 -F /data/1920x1080-ABGR8888-Boxlanuncher.bin 
elif [ "$1" = "31" ]; then
/data/ovltest -M rockchip -s $CONN@$CRTC:${CRTC_W}x${CRTC_H} -P $E0@$CRTC:960x540:1920x1080@XB24 -F /data/wukong_z0_960x540_XB24.bin 
elif [ "$1" = "32" ]; then
/data/ovltest -M rockchip -s $CONN@$CRTC:${CRTC_W}x${CRTC_H} -P $E0@$CRTC:1920x1080@NV12 -F /data/1920x1080_yuv420-flower.bin 
elif [ "$1" = "33" ]; then
/data/ovltest -M rockchip -s $CONN@$CRTC:${CRTC_W}x${CRTC_H} -P $E0@$CRTC:1280x720@BG24 -F /data/1280x720-RGB888-flower.bin 
elif [ "$1" = "34" ]; then
/data/ovltest -M rockchip -s $CONN@$CRTC:${CRTC_W}x${CRTC_H} -P $E0@$CRTC:4096x2160:1920x1080@RG16 -F /data/4096x2160_RGB565_roulette.bin 
elif [ "$1" = "35" ]; then
/data/ovltest -M rockchip -s $CONN@$CRTC:${CRTC_W}x${CRTC_H} -P $E0@$CRTC:1920x1080@AB30 -F /data/1920x1080_AB30_Sun.bin 
elif [ "$1" = "36" ]; then
/data/ovltest -M rockchip -s $CONN@$CRTC:${CRTC_W}x${CRTC_H} -P $E0@$CRTC:3840x2160:1920x1080@AB30 -F /data/3840x2160_AB30_NBA.bin 
elif [ "$1" = "37" ]; then
/data/ovltest -M rockchip -s $CONN@$CRTC:${CRTC_W}x${CRTC_H} -P $E0@$CRTC:4096x2160:1920x1080@AB30 -F /data/4096x2160_AB30_roulette.bin
elif [ "$1" = "38" ]; then
/data/ovltest -M rockchip -s $CONN@$CRTC:${CRTC_W}x${CRTC_H} -P $E0@$CRTC:640x360@NV12 -F /data/640x360_NV12_car.bin
elif [ "$1" = "39" ]; then
modetest -M rockchip -s $CONN@$CRTC:${CRTC_W}x${CRTC_H} -P $M0@$CRTC:1920x1080@XB30
elif [ "$1" = "40" ]; then
/data/ovltest -M rockchip -s $CONN@$CRTC:${CRTC_W}x${CRTC_H} -P $M0@$CRTC:1920x1080@AB24 -F /data/1920x1080-ABGR8888-Boxlanuncher.bin 
elif [ "$1" = "41" ]; then
/data/ovltest -M rockchip -s $CONN@$CRTC:${CRTC_W}x${CRTC_H} -P $M0@$CRTC:960x540:1920x1080@XB24 -F /data/wukong_z0_960x540_XB24.bin 
elif [ "$1" = "42" ]; then
/data/ovltest -M rockchip -s $CONN@$CRTC:${CRTC_W}x${CRTC_H} -P $M0@$CRTC:1920x1080@NV12 -F /data/1920x1080_yuv420-flower.bin 
elif [ "$1" = "43" ]; then
/data/ovltest -M rockchip -s $CONN@$CRTC:${CRTC_W}x${CRTC_H} -P $M0@$CRTC:1280x720@BG24 -F /data/1280x720-RGB888-flower.bin 
elif [ "$1" = "44" ]; then
/data/ovltest -M rockchip -s $CONN@$CRTC:${CRTC_W}x${CRTC_H} -P $M0@$CRTC:4096x2160:1920x1080@RG16 -F /data/4096x2160_RGB565_roulette.bin 
elif [ "$1" = "45" ]; then
/data/ovltest -M rockchip -s $CONN@$CRTC:${CRTC_W}x${CRTC_H} -P $M0@$CRTC:1920x1080@AB30 -F /data/1920x1080_AB30_Sun.bin 
elif [ "$1" = "46" ]; then
/data/ovltest -M rockchip -s $CONN@$CRTC:${CRTC_W}x${CRTC_H} -P $M0@$CRTC:3840x2160:1920x1080@AB30 -F /data/3840x2160_AB30_NBA.bin 
elif [ "$1" = "47" ]; then
/data/ovltest -M rockchip -s $CONN@$CRTC:${CRTC_W}x${CRTC_H} -P $M0@$CRTC:4096x2160:1920x1080@AB30 -F /data/4096x2160_AB30_roulette.bin 
elif [ "$1" = "48" ]; then
/data/ovltest -M rockchip -s $CONN@$CRTC:${CRTC_W}x${CRTC_H} -P $E0@$CRTC:640x360@NV12 -F /data/640x360_NV12_car.bin
elif [ "$1" = "49" ]; then
/data/ovltest -M rockchip -s $CONN@$CRTC:${CRTC_W}x${CRTC_H} -P $M0@$CRTC:1920x1080:960x540@NV12 -F /data/1920x1080_yuv420-flower.bin 
else
/data/ovltest -M rockchip -s $CONN@$CRTC:${CRTC_W}x${CRTC_H} -P $C0@$CRTC:800x1280@AB24@afbc -F /data/800x1280-AB24_afbc_Alauncher-z1.bin 
fi
