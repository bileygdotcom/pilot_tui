# setUp.py
import sys,os
import curses
import subprocess

def rights(softpath,login,passw):
    login = str(login)
    passw = str(passw)
    command = 'cd ' + softpath + ' && chmod +x Ascon.Pilot.Daemon && ./Ascon.Pilot.Daemon --admin ./settings.xml ' + login + ' ' + passw
    p = subprocess.Popen(command, shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)
    out = str(p.stdout.read())
    err = str(p.stderr.read())
