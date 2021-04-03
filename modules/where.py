# where.py
import os

def existance(softpath):
    #softpath = '/opt/pilot-server'
    if os.path.isdir(softpath):
        direx = True
        if os.path.isfile(softpath+'/pilot-tui'):
            filex = True
        else:
            filex = False
    else:
        direx = False
        filex = False
    #return direx, filex
    return direx
