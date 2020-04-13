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


def main():
    # Debugger object for accessing the debugger
    debugger = Debugger()

    # Initialisation command
    ec = debugger.getCurrentExecutionContext()

    ec.getExecutionService().stop()
    ec.getExecutionService().waitForStop()

    bs = ec.getBreakpointService().setBreakpoint("0xc039ae58")
    bs1 = ec.getBreakpointService().setBreakpoint("0xc039ae98")
    bs2 = ec.getBreakpointService().setBreakpoint("0xc039af30")
    ec.getExecutionService().resume()

    while(1):
        ec.getExecutionService().waitForStop(0)
        sp = ec.getRegisterService().getValue("SP")
        value = ec.getMemoryService().readMemory32(str(sp))
        wp = ec.getBreakpointService().setWriteWatchpoint(sp)
        ec.getExecutionService().resume()
        ec.getExecutionService().waitForStop(0)
        value1 = ec.getMemoryService().readMemory32(str(sp))
        print 'sp %s %x %x' % (str(sp), value, value1)
        wp.remove()
        ec.getExecutionService().resume()
 

if __name__ == '__main__' :
    main()
