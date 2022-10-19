#!/usr/bin/env python

import sys, getopt

SYS_BASE = 0
OVL_BASE = 0x600
VP0_BASE = 0xC00
VP1_BASE = 0xD00
VP2_BASE = 0xE00
VP3_BASE = 0xF00
CLUSTER0_BASE = 0x1000
CLUSTER1_BASE = 0x1200
CLUSTER2_BASE = 0x1400
CLUSTER3_BASE = 0x1600

RK3568_VP0_DSP_CTRL = 0xC00
RK3568_VP0_PRE_SCAN_HTIMING = 0xC30
RK3568_VP0_POST_DSP_HACT_INFO   = 0xC34
RK3568_VP0_POST_DSP_VACT_INFO   = 0xC38
RK3568_VP0_POST_SCL_FACTOR_YRGB	= 0xC3C
RK3568_VP0_POST_SCL_CTRL    = 0xC40
RK3568_VP0_POST_DSP_VACT_INFO_F1    = 0xC44
RK3568_VP0_DSP_HTOTAL_HS_END    = 0xC48
RK3568_VP0_DSP_HACT_ST_END  = 0xC4C
RK3568_VP0_DSP_VTOTAL_VS_END = 0xC50
RK3568_VP0_DSP_VACT_ST_END  = 0xC54
RK3568_VP0_DSP_VS_ST_END_F1 = 0xC58
RK3568_VP0_DSP_VACT_ST_END_F1   = 0xC5C

RK3568_CLUSTER0_WIN0_CTRL0 = 0x1000

RK3568_CLUSTER0_WIN0_YRGB_MST = 0x1010
RK3568_CLUSTER0_WIN0_CBR_MST = 0x1014
RK3568_CLUSTER0_WIN0_VIR    = 0x1018
RK3568_CLUSTER0_WIN0_ACT_INFO = 0x1020
RK3568_CLUSTER0_WIN0_DSP_INFO = 0x1024
RK3568_CLUSTER0_WIN0_DSP_ST = 0x1028

RK3568_CLUSTER0_WIN0_AFBCD_CTRL = 0x106C
RK3568_CLUSTER0_WIN0_AFBCD_HDR_PTR = 0x1058
RK3568_CLUSTER0_WIN0_AFBCD_VIR_WIDTH = 0x105C
RK3568_CLUSTER0_WIN0_AFBCD_PIC_SIZE = 0x1060
RK3568_CLUSTER0_WIN0_AFBCD_PIC_OFFSET = 0x1064
RK3568_CLUSTER0_WIN0_AFBCD_DSP_OFFSET = 0x1068
RK3568_CLUSTER0_WIN0_AFBCD_CTRL = 0x106C

RK3568_CLUSTER0_CTRL = 0x1100

RK3568_ESMART0_REGION0_CTRL = 0x1810
RK3568_ESMART0_REGION0_YRGB_MST = 0x1814
RK3568_ESMART0_REGION0_CBR_MST = 0x1818
RK3568_ESMART0_REGION0_VIR = 0x181C
RK3568_ESMART0_REGION0_ACT_INFO = 0x1820
RK3568_ESMART0_REGION0_DSP_INFO = 0x1824
RK3568_ESMART0_REGION0_DSP_ST = 0x1828
RK3568_ESMART0_REGION0_SCL_CTRL = 0x1830
YRGB_XSCL_MODE_MASK = 0x3
YRGB_XSCL_MODE_SHIFT    = 0
YRGB_XSCL_FILTER_MODE_MASK  = 0x3
YRGB_XSCL_FILTER_MODE_SHIFT = 2
YRGB_YSCL_MODE_MASK = 0x3
YRGB_YSCL_MODE_SHIFT    = 0x4
YRGB_YSCL_FILTER_MODE_MASK  = 0x3
YRGB_YSCL_FILTER_MODE_SHIFT = 6

RK3568_ESMART0_REGION0_SCL_FACTOR_YRGB = 0x1834
RK3568_ESMART0_REGION0_SCL_FACTOR_CBR	= 0x1838
RK3568_ESMART0_REGION0_SCL_OFFSET = 0x183C
RK3568_ESMART0_REGION1_CTRL = 0x1840


RK3568_ESMART0_REGION1_YRGB_MST = 0x1844
RK3568_ESMART0_REGION1_CBR_MST = 0x1848
RK3568_ESMART0_REGION1_VIR = 0x184C
RK3568_ESMART0_REGION1_ACT_INFO = 0x1850
RK3568_ESMART0_REGION1_DSP_INFO = 0x1854
RK3568_ESMART0_REGION1_DSP_ST = 0x1858
RK3568_ESMART0_REGION1_SCL_CTRL = 0x1860
RK3568_ESMART0_REGION1_SCL_FACTOR_YRGB = 0x1864
RK3568_ESMART0_REGION1_SCL_FACTOR_CBR = 0x1868
RK3568_ESMART0_REGION1_SCL_OFFSET = 0x186C
RK3568_ESMART0_REGION2_CTRL = 0x1870
RK3568_ESMART0_REGION2_YRGB_MST = 0x1874
RK3568_ESMART0_REGION2_CBR_MST = 0x1878
RK3568_ESMART0_REGION2_VIR = 0x187C
RK3568_ESMART0_REGION2_ACT_INFO = 0x1880
RK3568_ESMART0_REGION2_DSP_INFO = 0x1884
RK3568_ESMART0_REGION2_DSP_ST = 0x1888
RK3568_ESMART0_REGION2_SCL_CTRL = 0x1890
RK3568_ESMART0_REGION2_SCL_FACTOR_YRGB = 0x1894
RK3568_ESMART0_REGION2_SCL_FACTOR_CBR = 0x1898
RK3568_ESMART0_REGION2_SCL_OFFSET = 0x189C
RK3568_ESMART0_REGION3_CTRL = 0x18A0
RK3568_ESMART0_REGION3_YRGB_MST = 0x18A4
RK3568_ESMART0_REGION3_CBR_MST = 0x18A8
RK3568_ESMART0_REGION3_VIR = 0x18AC
RK3568_ESMART0_REGION3_ACT_INFO	 = 0x18B0
RK3568_ESMART0_REGION3_DSP_INFO = 0x18B4
RK3568_ESMART0_REGION3_DSP_ST = 0x18B8
RK3568_ESMART0_REGION3_SCL_CTRL = 0x18C0
RK3568_ESMART0_REGION3_SCL_FACTOR_YRGB = 0x18C4
RK3568_ESMART0_REGION3_SCL_FACTOR_CBR = 0x18C8
RK3568_ESMART0_REGION3_SCL_OFFSET = 0x18CC

RK3568_OVL_LAYER_SEL = 0x604
LAYER_SEL_MASK = 0xf
RK3568_OVL_PORT_SEL = 0x608

ESMART0_BASE = 0x1800
ESMART1_BASE = 0x1A00
SMART0_BASE = 0x1C00
SMART1_BASE = 0x1E00
BLOCK_LEN = 0x100

RK3568_LAYER_CNT = 6
RK3588_LAYER_CNT = 8

RK3588_VOP_VERSION = 0x40176786
RK3568_VOP_VERSION = 0x40158023
VOP_VERSION = 0x3588

REG_LEN = (SMART1_BASE + BLOCK_LEN) >> 2
REGS = [0] * REG_LEN

def parse_reg_val(base):
    index = base >> 2
    return int(REGS[index], 16)

def parse_soc():
    global VOP_VERSION
    ver_reg = parse_reg_val(4)
    if ver_reg == RK3588_VOP_VERSION:
        VOP_VERSION = 0x3588
    elif ver_reg == RK3568_VOP_VERSION:
        VOP_VERSION = 0x3568
    else:
        VOP_VERSION = 0

    print ("SOC: %x" % VOP_VERSION)

def parse_smart_win_format(reg):
    val = (parse_reg_val(reg) >> 1) & 0x1f
    if val == 0:
        return 'XR24', 32
    elif val == 1:
        return 'RG24', 24
    elif val == 2:
        return 'RG16', 16
    elif val == 4:
        return 'NV12', 12
    elif val == 5:
        return 'NV16', 16
    elif val == 6:
        return 'NV24', 24
    elif val == 0x14:
        return 'NV15', 15
    elif val == 0x15:
        return 'NV20', 20
    elif val == 0x16:
        return 'NV30', 30
    else:
        raise ValueError('Unknow format')

def parse_cluster_win_afbc_format(reg):
    val = (parse_reg_val(reg) >> 2) & 0xf
    if val == 0:
        return 'RG16', 16
    elif val == 2:
        return 'XR30', 32
    elif val == 3:
        return 'YU10', 15
    elif val == 4:
        return 'RG24', 24
    elif val == 5:
        return 'XR24', 32
    elif val == 9:
        return 'YU08', 12
    elif val == 0xb:
        return 'YVYU', 16
    elif val == 0xe:
        return 'Y210', 20
    else:
        raise ValueError('Unknow format')

def parse_cluster_win_format(reg):
    val = (parse_reg_val(reg) >> 1) & 0x1f
    if val == 0:
        return 'XR24', 32
    elif val == 1:
        return 'RG24', 24
    elif val == 2:
        return 'RG16', 16
    elif val == 4:
        return 'NV12', 12
    elif val == 5:
        return 'NV16', 16
    elif val == 6:
        return 'NV24', 24
    elif val == 0x14:
        return 'NV15', 15
    elif val == 0x15:
        return 'NV20', 20
    elif val == 0x16:
        return 'NV30', 30
    else:
        raise ValueError('Unknow format')


def is_smart_win(id):
    if VOP_VERSION == 0x3568:
        if id >= 2:
            return True
        else:
            return False
    elif VOP_VERSION == 0x3588:
        if id >= 4:
            return True
        else:
            return False
    else:
        raise ValueError('Unknow soc')

def smart_win_port_sel_shift(id):
    if VOP_VERSION == 0x3588:
        return 24 + (id - 4) * 2
    elif VOP_VERSION == 0x3568:
        return  24 + (id -2) * 2
    else:
         raise ValueError('Unknow soc')


def cluster_win_port_sel_shift(id):
        return  16 + id * 2

def parse_win_rect(reg):
    val = parse_reg_val(reg)
    return (val & 0xfff) + 1, ((val >> 16) & 0xfff) + 1

def parse_smart_win(id):
    if VOP_VERSION == 0x3588:
        win_id = id - 4
    else:
        win_id  = id - 2
    offset = win_id * 0x200
    for i in range(3):
        area_offset = 0x30 * i
        win_ctrl = parse_reg_val(RK3568_ESMART0_REGION0_CTRL + offset + area_offset)
        if (win_ctrl & 0x1) == 0:
            continue
        else:
            format, bpp = parse_smart_win_format(RK3568_ESMART0_REGION0_CTRL + offset + area_offset)
            yrgb_mst =  parse_reg_val(RK3568_ESMART0_REGION0_YRGB_MST + offset + area_offset)
            uv_mst = parse_reg_val(RK3568_ESMART0_REGION0_CBR_MST + offset + area_offset)
            stride = parse_reg_val(RK3568_ESMART0_REGION0_VIR + offset + area_offset) & 0xffff
            uv_stride = parse_reg_val(RK3568_ESMART0_REGION0_VIR + offset + area_offset) >> 16
            src_w, src_h = parse_win_rect(RK3568_ESMART0_REGION0_ACT_INFO + offset + area_offset)
            dst_w, dst_h = parse_win_rect(RK3568_ESMART0_REGION0_DSP_INFO + offset + area_offset)
            fb_size = stride * 4 * src_h
            fb_end = yrgb_mst + fb_size
            print ("Esmart%d-win%d:" %(win_id, i))
            print ("    format: %s" % format)
            print ("    src: rect[%d x %d]" %(src_w, src_h))
            print ("    dst: rect[%d x %d]" %(dst_w, dst_h))
            print ("    buf[0]: addr: 0x%08x  end: 0x%08x pitch: %d" %(yrgb_mst, fb_end, stride * 4))


def parse_cluster_win(id):
    offset = id * 0x200
    for i in range(1):
        sub_offset = 0x80 * i
        win_ctrl = parse_reg_val(RK3568_CLUSTER0_WIN0_CTRL0 + offset + sub_offset)
        if (win_ctrl & 0x1) == 0:
            continue
        else:
            afbc_en = (parse_reg_val(RK3568_CLUSTER0_CTRL + offset) >> 1) & 0x1
            if afbc_en == 1:
                format, bpp = parse_cluster_win_afbc_format(RK3568_CLUSTER0_WIN0_AFBCD_CTRL + offset + sub_offset)
                yrgb_mst =  parse_reg_val(RK3568_CLUSTER0_WIN0_AFBCD_HDR_PTR + offset + sub_offset)
                pixel = parse_reg_val(RK3568_CLUSTER0_WIN0_AFBCD_VIR_WIDTH + offset + sub_offset) & 0xffff
                stride = pixel * bpp >> 3
                src_w, src_h = parse_win_rect(RK3568_CLUSTER0_WIN0_AFBCD_PIC_SIZE + offset + sub_offset)
                afbc = 'AFBC'
            else:
                format, bpp = parse_cluster_win_format(RK3568_CLUSTER0_WIN0_CTRL0 + offset + sub_offset)
                yrgb_mst =  parse_reg_val(RK3568_CLUSTER0_WIN0_YRGB_MST + offset + sub_offset)
                stride = parse_reg_val(RK3568_CLUSTER0_WIN0_VIR + offset + sub_offset) & 0xffff
                stride = stride * 4
                src_w, src_h = parse_win_rect(RK3568_CLUSTER0_WIN0_ACT_INFO + offset + sub_offset)
                afbc = ' '

            dst_w, dst_h = parse_win_rect(RK3568_CLUSTER0_WIN0_DSP_INFO + offset + sub_offset)
            fb_size = stride * 4 * src_h
            fb_end = yrgb_mst + fb_size

            print ("Cluster%d-win%d:" %(id, i))
            print ("    format: %s %s" % (format, afbc))
            print ("    src: rect[%d x %d]" %(src_w, src_h))
            print ("    dst: rect[%d x %d]" %(dst_w, dst_h))
            print ("    buf[0]: addr: 0x%08x  end: 0x%08x pitch: %d" %(yrgb_mst, fb_end, stride))


def parse_video_port(id):
    offset = id * 0x100;

    if VOP_VERSION == 0x3588:
        win_cnt = RK3588_LAYER_CNT
    elif VOP_VERSION == 0x3568:
        win_cnt = RK3568_LAYER_CNT
    else:
        win_cnt = 0

    dsp_ctrl = parse_reg_val(RK3568_VP0_DSP_CTRL + offset)
    ovl_port_sel =  parse_reg_val(RK3568_OVL_PORT_SEL)
    ovl_layer_sel =  parse_reg_val(RK3568_OVL_LAYER_SEL)

    if dsp_ctrl & 0x80000000 == 0x80000000:
        print ("Video_Port%d: DISABLED" % id)
    else:
        print ("Video_Port%d: ACTIVE" % id)
        for i in range(win_cnt):
            if is_smart_win(i) == True:
                shift = smart_win_port_sel_shift(i)
                if (ovl_port_sel >> shift) & 0x3 == id:
                    parse_smart_win(i)
            else:
                shift = 16 + i * 2
                if (ovl_port_sel >> shift) & 0x3 == id:
                    parse_cluster_win(i)

def set_reg(line, base, offset):
    global REGS
    index = (base + offset) >> 2
    if index >= len(REGS):
        return
    line_base = '%08x:' % offset
    regs4 =  line.split(line_base)[1]
    regs4 = regs4.strip()
    regs4 = regs4.split(' ')
    REGS[index], REGS[index + 1], REGS[index + 2], REGS[index + 3] = regs4[0], regs4[1], regs4[2], regs4[3]
    print ("%s %s %s %s" % (REGS[index], REGS[index + 1], REGS[index + 2], REGS[index +3]))

    return


def main(argv):
    global REGS
    logfile =  argv[0]
    regbase = 0
    block = 'SYSTEM'
    offset = 0

    print ('reglen: %d'  % len(REGS))
    print ('logfile: %s' % logfile)
    with open(logfile,'r') as f:
        for line in f:
            if line.find('SYS:') != -1:
                print ('SYSTEM:')
                block = 'SYS'
                offset = 0
            elif line.find('OVL:') != -1:
                print ('OVL:')
                block = 'OVL'
                offset = 0
            elif line.find('VP0:') != -1:
                print ('VP0:')
                block = 'VP0'
                offset = 0;
            elif line.find('VP1:') != -1:
                print ('VP1:')
                block = 'VP1'
                offset = 0;
            elif line.find('VP2:') != -1:
                print ('VP2:')
                block = 'VP2'
                offset = 0;
            elif line.find('VP3:') != -1:
                print ('VP3:')
                block = 'VP3'
                offset = 0;
            elif line.find('Cluster0:') != -1:
                print ('Cluster0:')
                block = 'C0'
                offset = 0;
            elif line.find('Cluster1:') != -1:
                print ('Cluster1:')
                block = 'C1'
                offset = 0;
            elif line.find('Cluster2:') != -1:
                print ('Cluster2:')
                block = 'C2'
                offset = 0;
            elif line.find('Cluster3:') != -1:
                print ('Cluster3:')
                block = 'C3'
                offset = 0;
            elif line.find('Esmart0:') != -1:
                print ('Esmart0:')
                block = 'E0'
                offset = 0;
            elif line.find('Esmart1:') != -1:
                print ('Esmart1:')
                block = 'E1'
                offset = 0;
            elif line.find('Smart0:') != -1:
                print ('Esmart2:')
                block = 'E2'
                offset = 0;
            elif line.find('Smart1:') != -1:
                print ('Esmart3:')
                block = 'E3'
                offset = 0;
            elif line.find('HDR:') != -1:
                break
            elif block == 'SYS':
                set_reg(line, SYS_BASE, offset)
                offset += 0x10
            elif block == 'OVL':
                set_reg(line, OVL_BASE, offset)
                offset += 0x10
            elif block == 'VP0':
                set_reg(line, VP0_BASE, offset)
                offset += 0x10;
            elif block == 'VP1':
                set_reg(line, VP1_BASE, offset)
                offset += 0x10;
            elif block == 'VP2':
                set_reg(line, VP2_BASE, offset)
                offset += 0x10;
            elif block == 'VP3':
                set_reg(line, VP3_BASE, offset)
                offset += 0x10;
            elif block == 'OVL':
                set_reg(line, OVL_BASE, offset)
                offset += 0x10;
            elif block == 'C0':
                set_reg(line, CLUSTER0_BASE, offset)
                offset += 0x10;
            elif block == 'C1':
                set_reg(line, CLUSTER1_BASE, offset)
                offset += 0x10;
            elif block == 'C2':
                set_reg(line, CLUSTER2_BASE, offset)
                offset += 0x10;
            elif block == 'C3':
                set_reg(line, CLUSTER3_BASE, offset)
                offset += 0x10;
            elif block == 'E0':
                set_reg(line, ESMART0_BASE, offset)
                offset += 0x10;
            elif block == 'E1':
                set_reg(line, ESMART1_BASE, offset)
                offset += 0x10;
            elif block == 'E2':
                set_reg(line, SMART0_BASE, offset)
                offset += 0x10;
            elif block == 'E3':
                set_reg(line, SMART1_BASE, offset)
                offset += 0x10;
    parse_soc()
    parse_video_port(0)
    parse_video_port(1)
    parse_video_port(2)
    parse_video_port(3)

if __name__ == "__main__":
    main(sys.argv[1:])
