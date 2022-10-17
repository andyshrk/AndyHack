#!/usr/bin/env python2

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
ESMART0_BASE = 0x1800
ESMART1_BASE = 0x1A00
SMART0_BASE = 0x1C00
SMART1_BASE = 0x1E00
BLOCK_LEN = 0x100

REGS = []
REG_LEN = (SMART1_BASE + BLOCK_LEN) / 4

def set_reg(line, base, offset):
    global REGS
    index = (base + offset)/ 4
    if index >= len(REGS):
        return
    line_base = '%08x:' % offset
    regs4 =  line.split(line_base)[1]
    regs4 = regs4.strip()
    regs4 = regs4.split(' ')
    REGS[index], REGS[index + 1], REGS[index + 2], REGS[index + 3] = regs4[0], regs4[1], regs4[2], regs4[3]
    print  REGS[index], REGS[index + 1], REGS[index + 2], REGS[index +3]
    return


def main(argv):
    global REGS
    logfile =  argv[0]
    regbase = 0
    block = 'SYSTEM'
    offset = 0

    cnt = 0
    while cnt < REG_LEN:
        REGS.append(0)
        cnt += 1

    print 'reglen: ', len(REGS)
    print 'logfile: ', logfile
    with open(logfile,'r') as f:
        for line in f:
            if line.find('SYS:') != -1:
                print 'SYSTEM:'
            elif line.find('OVL:') != -1:
                print 'OVL:'
            elif line.find('VP0:') != -1:
                print 'VP0:'
                block = 'VP0'
                offset = 0;
            elif line.find('VP1:') != -1:
                print 'VP1:'
                block = 'VP1'
                offset = 0;
            elif line.find('VP2:') != -1:
                print 'VP2:'
                block = 'VP2'
                offset = 0;
            elif line.find('VP3:') != -1:
                print 'VP3:'
                block = 'VP3'
                offset = 0;
            elif line.find('Cluster0:') != -1:
                print 'Cluster0:'
                block = 'C0'
                offset = 0;
            elif line.find('Cluster1:') != -1:
                print 'Cluster1:'
                block = 'C1'
                offset = 0;
            elif line.find('Cluster2:') != -1:
                print 'Cluster2:'
                block = 'C2'
                offset = 0;
            elif line.find('Cluster3:') != -1:
                print 'Cluster3:'
                block = 'C3'
                offset = 0;
            elif line.find('Esmart0:') != -1:
                print 'Esmart0:'
                block = 'E0'
                offset = 0;
            elif line.find('Esmart1:') != -1:
                print 'Esmart1:'
                block = 'E1'
                offset = 0;
            elif line.find('Smart0:') != -1:
                print 'Esmart2:'
                block = 'E2'
                offset = 0;
            elif line.find('Smart1:') != -1:
                print 'Esmart3:'
                block = 'E3'
                offset = 0;
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

if __name__ == "__main__":
    main(sys.argv[1:])
