# Cortex-A17 L1 Cache Dump script for DS-5
# Copyright (c) 2007-2013 ARM, Inc.  All rights reserved.

import sys

from arm_ds.debugger_v1 import Debugger
from arm_ds.debugger_v1 import DebugException
from math import log
import csv
from java.lang import String as javastring
import StringIO

version = '0.1'

L1_D_CSSELR = 0x0
L1_I_CSSELR = 0x1
L2_CSSELR   = 0x2

# Default configuration
config = {'command':    0,
          'file':       0,
          'mode':       0,
          'param':      0,
          'valid':      0,
          'csv':        0,
          'gui':        0 }

class CacheInfo :
    def __init__(self, ec, csselr_id):
        ec.getRegisterService().setValue('CP15_CSSELR', csselr_id)
        self.data = long(ec.getRegisterService().getValue('CP15_CCSIDR'))
    
    def is_write_through(self):
        return get_bits(self.data, 31, 31)
    
    def is_write_back(self):
        return get_bits(self.data, 30, 30)
    
    def is_read_allocate(self):
        return get_bits(self.data, 29, 29)
    
    def is_write_allocate(self):
        return get_bits(self.data, 28, 28)
    
    def get_sets_count(self):
        return get_bits(self.data, 27, 13) + 1
    
    def get_ways_count(self):
        return 2**bit_count(get_bits(self.data, 12, 3))
    
    def get_line_size(self):
        return 2**(get_bits(self.data, 2, 0) + 2)
    
    def get_size_kb(self):
        return self.get_size_b()/1024
    
    def get_size_b(self):
        return self.get_sets_count()*self.get_line_size()*self.get_ways_count()*4
    
    def get_set_index_range(self):
        return int(log(self.get_size_b()/4, 2))

def hex2(n, bit_width=32):
    ''' A variant of hex() that returns a hex string of width bit_width '''
    hex_string = '%X' % n
    return '%s' % hex_string.zfill(bit_width/4)

def bit_count(n):
    ''' Counts the number of ones in n '''
    count = 0
    while n > 0:
        count = count + 1
        n = n & (n-1)
    return count

def get_bits(number, msb, lsb=0):
    ''' Retrieves the bits from msb to lsb in number '''
    width = msb-lsb+1
    mask = 0
    for i in xrange(width):
        mask = (mask << 1) | 1
    return (number >> lsb) & mask

def build_instruction_address(tag, set, doubleword=0):
    ''' Builds the instruction address given the tag and set '''
    return tag << 12 | set << 5 | doubleword << 2

def build_data_address(tag, set, doubleword=0):
    ''' Builds the address given the tag, set, and doubleword '''
    return tag << 11 | set << 6 | doubleword << 3

def decode_address(address):
    return {'tag' : get_bits(address, 39, 11),
            'set' : get_bits(address, 10, 6),
            'doubleword': get_bits(address, 5, 3)}

def decode_tag_state(state):
    ''' Decode the Tag State for an L1 Data Tag '''
    if state == 0:
        return 'Invalid'
    elif state == 1:
        return 'Exclusive'
    elif state == 2:
        return 'Modified'
    elif state == 3:
        return 'Shared'
    else :
        raise ValueError('Invalid State: %s' % hex(state))

def decode_instruction_set(is_id):
    ''' Decode the Instruction Set from a given id'''
    if is_id == 0:
        return 'ARM'
    elif is_id == 1:
        return 'Thumb'
    else :
        raise ValueError('Invalid Instruction Set: %s' % hex(is_id))
    
def read_L1I_tag(ec, way, set):
    ''' Reads an L1 Instruction Tag Entry '''
    reg_data = way << 31 | set << 5
    ec.getRegisterService().setValue('CP15_CDBGICT', reg_data)
    
    data0 = long(ec.getRegisterService().getValue('CP15_CDBGDR0'))
    return {'valid': get_bits(data0, 30, 30),
            'is_mode': get_bits(data0, 29, 29),
            'ns': get_bits(data0, 28, 28),
            'tag': get_bits(data0, 27) }

def dump_L1I_tag(ec, way):
    ''' Dumps the L1 Instruction Tag Entries '''
    
    csv = config['csv']
    if csv :
        csv.writerow(('address', 'tag', 'set', 'instruction set', 'valid', 'ns'))
        
    cache_info = CacheInfo(ec, L1_I_CSSELR)
    
    for set in xrange(cache_info.get_sets_count()) :
        tag_data = read_L1I_tag(ec, way, set)
        address = build_instruction_address(tag_data['tag'], set)
        if not config['valid'] or (config['valid'] and tag_data['valid'] != 0):
            vals = ['0x'+hex2(address, 40),
                    '0x'+hex2(tag_data['tag'], 28),
                    '0x'+hex2(set, int(log(cache_info.get_sets_count(), 2))),
                    decode_instruction_set(tag_data['is_mode']), 
                    tag_data['valid'],
                    tag_data['ns']]
            if csv :
                csv.writerow(vals)
            else :
                print javastring.format('address=%s tag=%s set=%s instruction set=%s valid=%s ns=%s', *vals)

def read_L1I_data(ec, way, addr):
    ''' Read the L1 Instruction Data Ram '''

    base_reg = way << 31 | get_bits(addr, 30)
    ec.getRegisterService().setValue('CP15_CDBGICD', base_reg)
    
    return [long(ec.getRegisterService().getValue('CP15_CDBGDR0')), 
            long(ec.getRegisterService().getValue('CP15_CDBGDR1'))]
        
def dump_L1I_data(ec, way):
    ''' Read the L1 Instruction Data Cache '''
    
    csv = config['csv']
    if csv :
        cols = ['base address', 'tag', 'set', 'is mode', 'valid', 'ns'] + ['data[%s]' % x for x in xrange(16)]
        csv.writerow(cols)
        
    cache_info = CacheInfo(ec, L1_I_CSSELR)
    
    for set in xrange(cache_info.get_sets_count()) :
        tag_data = read_L1I_tag(ec, way, set)
        if config['valid'] and tag_data['valid'] == 0: continue
        
        vals = ['0x'+hex2(build_instruction_address(tag_data['tag'], set), 40),
                '0x'+hex2(tag_data['tag'], 28),
                '0x'+hex2(set, int(log(cache_info.get_sets_count(), 2))),
                decode_instruction_set(tag_data['is_mode']),
                tag_data['valid'], 
                tag_data['ns']]
        
        set_info = ['virtual base address=%s' % vals[0],
                    'tag=%s set=%s' % (vals[1], vals[2]),
                    javastring.format('is mode=%s valid=%s ns=%s', *vals[3:]),
                    '']
        
        all_the_words = []
        
        for dw_4_3 in xrange(4):
            quadword = []
            for dw_2 in xrange(2):
                doubleword = dw_4_3 << 1 | dw_2
                address = build_instruction_address(tag_data['tag'], set, doubleword)
                data = read_L1I_data(ec, way, address)
                quadword += [hex2(data[0]), hex2(data[1])]
            
            if csv :
                all_the_words += quadword
            else :
                print '%s%s' % (set_info[dw_4_3].ljust(35), ' '.join(quadword))
        if csv :
            csv.writerow(vals + ['0x%s' % s for s in all_the_words])
        else :
            print
            
def read_L1D_tag(ec, cache_info, way, set):
    ''' Reads an L1 Data Tag Entry '''
    
    reg_data = way << 30 | set << 6
    
    ec.getRegisterService().setValue('CP15_CDBGDCT', reg_data)
    
    data0 = long(ec.getRegisterService().getValue('CP15_CDBGDR0'))
    data1 = long(ec.getRegisterService().getValue('CP15_CDBGDR1'))
    
    #from trm -- bottom N bits not valid where N is log2(cache size/8kb)
    invalid_bottom = int(log(cache_info.get_size_kb()/8, 2))
    
    #print 'invalid_bottom=%s, actual=%s' % (invalid_bottom, log(cache_info.get_size_kb()/8, 2))
    #print 'unaltered tag=%s' % hex2(get_bits(data1, 28), 32)
    return {'attrs' : get_bits(data0, 4, 2),
            'dirty_moesi' : get_bits(data0, 1, 0),
            'tag_moesi' : get_bits(data1, 31, 30),
            'ns' : get_bits(data1, 29, 29),
            'tag': get_bits(data1, 28, invalid_bottom) << invalid_bottom }

def dump_L1D_tag(ec, way):
    ''' Dumps the L1 Tag Data Cache '''
    
    csv = config['csv']
    if csv :
        keys = ['address', 'tag', 'set', 'ns', 'state', 'decoded state']
        csv.writerow(keys)    
    cache_info = CacheInfo(ec, L1_D_CSSELR)
    
    for set in xrange(cache_info.get_sets_count()) :
        tag_data = read_L1D_tag(ec, cache_info, way, set)
        address = build_data_address(tag_data['tag'], set)
        if not config['valid'] or (config['valid'] and tag_data['state'] != 0):
            
            vals = ['0x'+hex2(address, 40),
                    '0x'+hex2(tag_data['tag'], 29),
                    '0x'+hex2(set, int(log(cache_info.get_sets_count(), 2))),
                    tag_data['ns'], 
                    '0x'+hex2(tag_data['tag_moesi'],2), 
                    decode_tag_state(tag_data['tag_moesi'])]
            if csv :
                csv.writerow(vals)
            else :
                print javastring.format('address=%s tag=%s set=%s ns=%s state=%s (%s)', *vals)

def read_L1D_data(ec, way, base_address):
    ''' Reads an L1 Data Data Entry '''
    
    #base_address = get_bits(base_address, si_range+5, 3) << 3
    reg_data = way << 30 | get_bits(base_address, 29)
    
    #print "reg data=%s si range=%s" % (hex2(reg_data, 32), si_range)
    ec.getRegisterService().setValue('CP15_CDBGDCD', reg_data)
    
    return [long(ec.getRegisterService().getValue('CP15_CDBGDR0')),
            long(ec.getRegisterService().getValue('CP15_CDBGDR1'))]
    
def dump_L1D_data(ec, way):
    ''' Dump the L1 Data RAM '''
    
    csv = config['csv']
    if csv :
        keys = ['address', 'tag', 'set', 'ns', 'state', 'decoded state'] + ['data[%s]' % x for x in xrange(16)]
        csv.writerow(keys)
    
    cache_info = CacheInfo(ec, L1_D_CSSELR)
    
    for set in xrange(cache_info.get_sets_count()) :
        tag_data = read_L1D_tag(ec, cache_info, way, set)
        if config['valid'] and tag_data['tag_moesi'] != 0: continue
        
        vals = [hex2(build_data_address(tag_data['tag'], set), 40),
                hex2(tag_data['tag'], 29),
                hex2(set, int(log(cache_info.get_sets_count(), 2))),
                hex2(tag_data['ns']),
                hex2(tag_data['tag_moesi'],2), 
                decode_tag_state(tag_data['tag_moesi'])]
                     
        set_info = ['base address=0x%s' % vals[0],
                    'tag=0%s set=0x%s' % (vals[1], vals[2]),
                    javastring.format('ns=%s state=0x%s (%s)', *vals[3:]),
                    '']

        all_the_words = []
        for dw_2_1 in xrange(4):
            quadword = []
            for dw_0 in xrange(2):
                doubleword = dw_2_1 << 1 | dw_0
                address = build_data_address(tag_data['tag'], set, doubleword)
                data = read_L1D_data(ec, way, address)
                quadword += [hex2(data[0]), hex2(data[1])]
            if csv :
                all_the_words += quadword
            else :
                print '%s%s' % (set_info[dw_2_1].ljust(35), ' '.join(quadword))
        
        if csv :
            csv.writerow(vals + ['0x%s' % s for s in all_the_words])
        else :
            print

def check_L1I(ec, address):
    ''' Check if an address is in the L1 Instruction Ram '''
    
    cache_info = CacheInfo(ec, L1_I_CSSELR)
    
    address = decode_address(address)
    
    for way in xrange(cache_info.get_ways_count()):
        tag_data = read_L1I_tag(ec, way, address['set'])
        if tag_data['tag'] == address['tag'] :
            base_address = build_data_address(address['tag'], address['set'], address['doubleword'])
            print 'Found address in way %s: ' % way
            print '%s %s' % ('base address:'.ljust(15), hex2(base_address, 40))
            print '%s 0x%s 0x%s' % ('Data:'.ljust(10),hex2(data[0], 32), hex2(data[1], 32))
            for (key, val) in tag_data.items() :
                if val >= 2 :
                    val = hex(val)
                print '%s %s' % ((key+':').ljust(10), val)
            return
        
    print 'could not find address'

def check_L1D(ec, address):
    ''' Check if an address is in the L1 Data Ram '''
    
    cache_info = CacheInfo(ec, L1_D_CSSELR)
    
    address = decode_address(address)
    
    for way in xrange(cache_info.get_ways_count()):
        tag_data = read_L1D_tag(ec, cache_info, way, address['set'])
        if tag_data['tag'] == address['tag'] :
            base_address = build_data_address(address['tag'], address['set'], address['doubleword'])
            print 'Found address in way %s: ' % way
            print '%s %s' % ('base address:'.ljust(15), hex2(base_address, 40))
            data = read_L1I_data(ec, way, get_bits(base_address, 13, 3))
            print '%s 0x%s 0x%s' % ('data:'.ljust(15),hex2(data[0], 32), hex2(data[1], 32))
            for (key, val) in tag_data.items() :
                if val >= 2 :
                    val = hex(val)
                print '%s %s' % ((key+':').ljust(15), val)
            return
        
    print 'could not find address'

def get_gui_title():
    ''' Retrieves a good gui title based on program arguments '''
    
    if config['command'] == '-l1it':
        return 'L1 Instruction Tag Ram for Way %s' % config['param']
    elif config['command'] == '-l1id':
        return 'L1 Instruction Data Ram for Way %s' % config['param']
    elif config['command'] == "-l1dt":
        return 'L1 Data Tag Ram for Way %s' % config['param']
    elif config['command'] == "-l1dd":
        return 'L1 Data Data Ram for Way %s' % config['param']
        
def print_help():
    '''Print the user help'''
    
    print "Cache Reader for Cortex-A17 V%s Copyright (C) 2013 ARM Limited. All rights reserved." % version
    print "Usage: read_cache_a17 [options]"
    print "Options:"
    print "-l1it way     dump L1-I tag RAM  (way: range 0-1, default 0)"
    print "-l1id way     dump L1-I data RAM (way: range 0-1, default 0)"
    print "-l1dt way     dump L1-D tag RAM  (way: range 0-3, default 0)"
    print "-l1dd way     dump L1-D data RAM (way: range 0-3, default 0)"
    print "-checki addr  checks i-side for address"
    print "-checkd addr  checks d-side for address"
    print "-f file       write data to a text file"
    print "-csv file     write csv file"
    print "-gui          write output to gui window (ignores -f and -csv)"
    print "-valid        exclude invalid cache lines"
    print "-h            print this help"


def parse_params(params):
    '''Look for parameters and set internal config'''
    global config
    i = 1
    
    if len(sys.argv) < 2:
        return 0
        
    for i in xrange(len(sys.argv)):
        temp = sys.argv[i]
        
        if temp[:2] == '-l' or temp[:6] == '-check':
            config['command'] = temp
            if i < (len(sys.argv)-1) and sys.argv[i+1][0:1] != '-':
                config['param'] = sys.argv[i+1]   
        elif temp == '-f': # write data to file
            if (i < (len(sys.argv)-1)) and sys.argv[i+1][0:1] != '-':
                config['file'] = sys.argv[i+1]
            else:
                return 0
        elif temp == '-csv':
            config['csv'] = True
        elif temp == '-gui':
            config['gui'] = True
        elif temp == '-h':
            return 0
        elif temp == '-valid':
            config['valid'] = True
    return 1 # success    

def main():
    # Debugger object for accessing the debugger
    debugger = Debugger()

    # Initialisation command
    ec = debugger.getCurrentExecutionContext()

    ec.getExecutionService().stop()
    ec.getExecutionService().waitForStop()

    # in case the execution context reference is out of date
    ec = debugger.getCurrentExecutionContext()
    
    #### Hardware check ####
    try:
        cpu = long(ec.getRegisterService().getValue("CP15_MIDR.Primary"))
        if cpu != 0xc0E: # Cortex-A17 ?
            print "CPU not supported!"
            return
    except:
        print "Error at detecting the CPU"
        return
    
    if (parse_params(sys.argv) == 0):
        print_help()
        return       
    if config['gui'] :
        config['gui'] = StringIO.StringIO()
        config['csv'] = csv.writer(config['gui'])
    else :
        if config['file'] != 0:
            print "Data will be exported to file: %s" %(config['file'])
            old_stdout = sys.stdout
        
            try:
                sys.stdout = open(config['file'], 'wb')
            except IOError:
                print "Error at creating file '%s': Permission denied" % config['file']
                return
        if config['csv']:
            config['csv'] = csv.writer(sys.stdout, dialect='excel', quoting=csv.QUOTE_ALL)
    
    if config['command'] == '-l1it':
        way = int(config['param'])
        dump_L1I_tag(ec,way)
    elif config['command'] == '-l1id':
        way = int(config['param'])
        dump_L1I_data(ec, way)
    elif config['command'] == "-l1dt":
        way = int(config['param'])
        dump_L1D_tag(ec, way)
    elif config['command'] == "-l1dd":
        way = int(config['param']) 
        dump_L1D_data(ec, way)
    elif config['command'] == "-checki":
        address = long(config['param'], 16)
        check_L1I(ec, address)
    elif config['command'] == '-checkd':
        address = long(config['param'], 16)
        check_L1D(ec, address)
    else:
        print "Unknown parameter"
        print_help()      
    
    if config['file']:
        sys.stdout.close()      # Close device
        sys.stdout = old_stdout # Restore console
    
    if config['gui']:
        import csv_viewer
        csv_viewer.createAndShowGUI(csv.reader(StringIO.StringIO(config['gui'].getvalue())), get_gui_title())
    
 

if __name__ == '__main__' :
    main()
