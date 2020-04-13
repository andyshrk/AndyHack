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

    bs = ec.getBreakpointService().setBreakpoint("0xc039ae98")
    ec.getExecutionService().resume()

    ec.getExecutionService().waitForStop(0)
    sp = ec.getRegisterService().getValue("sp")
    debugger.removeAllBreakpoints()
    ec = debugger.getCurrentExecutionContext()
    psp= '*' + str(sp)
    cond = psp + '==0xc014f60c'
    print 'psp %s' % psp
    wp = ec.getBreakpointService().setWriteWatchpoint(sp)
    wp.setCondition(cond)
    wp.enable()
    ec.getExecutionService().resume()
    ec.getExecutionService().waitForStop(0)

if __name__ == '__main__' :
    main()
