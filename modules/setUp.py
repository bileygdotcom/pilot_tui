# setUp.py
import sys,os
import curses
import subprocess

def rights(slotPath,login,passw):
    login = str(login)
    passw = str(passw)
    command = 'sudo ' + slotPath + '/Ascon.Pilot.Daemon --admin ' + slotPath + '/settings.xml ' + login + ' ' + passw
    subprocess.Popen(command, shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)
    #out = str(p.stdout.read())
    #err = str(p.stderr.read())
