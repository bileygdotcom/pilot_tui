#purge.py
import shutil

def removePilotDirectory(slotPath):
    shutil.rmtree(slotPath, ignore_errors=True)
