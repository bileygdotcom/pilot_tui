# setUp.py
import sys,os
import curses
import subprocess

def launch(slotPath):
    command1 = 'sudo' + slotPath + '/Ascon.Pilot.Daemon ' + slotPath + '/settings.xml'
    command = command1 + ' && screen ' + command1
    #command = 'cd ' + softpath + ' && screen ./Ascon.Pilot.Daemon ./settings.xml'
    subprocess.Popen(command, shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)
    #out = str(p.stdout.read())
    #err = str(p.stderr.read())

def url():
    from urllib.request import urlopen
    u = urlopen('http://localhost:5545').read()
    return u
