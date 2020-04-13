import sys
from arm_ds.debugger_v1 import Debugger
from arm_ds.internal import Breakpoint, BreakpointService, MemoryService
from __builtin__ import len

# Debugger object for accessing the debugger
debugger = Debugger()

# Ensure that the target is stopped
ec = debugger.getCurrentExecutionContext()
ec.getExecutionService().stop()

wp = ec.getBreakpointService().setWriteWatchpoint("0xceecfc48")

#Resume the system
#ec.getExecutionService().resume()

