# chmodX.py
import sys,os
import curses
import subprocess

def setX(slotPath):
    command = 'sudo chmod +x ' + slotPath + '/Ascon.Pilot.Daemon'
    subprocess.Popen(command, shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)

    #out = str(p.stdout.read())
    #err = str(p.stderr.read())
