# loadIntoDirectory.py
import sys,os
import curses
import subprocess

def makeFolder(softpath):
    basepath = softpath + "/bases"
    command = 'mkdir ' + softpath + ' && mkdir ' + basepath
    p = subprocess.Popen(command, shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)
    out = str(p.stdout.read())
    err = str(p.stderr.read())
    
def download(softpath):
    basepath = softpath + "/bases"
    #command = 'cd ' + softpath + ' && wget --no-check-certificate https://pilot.ascon.ru/release/pilot-server.zip'
    #command = 'cd ' + softpath + ' && cp /home/bileyg/ASCON/pilot-server.zip /opt/pilot-server/
    command1 = 'cp /home/bileyg/ASCON/pilot-server.zip ' + softpath
    command2 = 'cd ' + basepath + ' && wget --no-check-certificate https://pilot.ascon.ru/release/Databases.zip' 
    command = command1 + ' && ' + command2
    p = subprocess.Popen(command, shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)
    out = str(p.stdout.read())
    err = str(p.stderr.read())
    
def unzip(softpath):
    basepath = softpath + "/bases"
    command1 = 'cd ' + softpath + ' && sudo unzip pilot-server.zip'
    command2 = 'cd ' + basepath + ' && sudo unzip Databases.zip'
    command = command1 + ' && ' + command2
    p = subprocess.Popen(command, shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)
    out = str(p.stdout.read())
    err = str(p.stderr.read())
