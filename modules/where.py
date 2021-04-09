# where.py
import os

def existance(slotPath):
    #softpath = '/opt/pilot-server'
    if os.path.isdir(slotPath):
        direx = True
        if os.path.isfile(slotPath+'/pilot-tui'):
            filex = True
        else:
            filex = False
    else:
        direx = False
        filex = False
    return direx, filex
    #return direx
