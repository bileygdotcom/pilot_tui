# load-into-directory.py
import sys,os
import curses
import subprocess

def makeFolder(softpath):
    command = 'mkdir ' + softpath
    p = subprocess.Popen(command, shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)
    out = str(p.stdout.read())
    err = str(p.stderr.read())
    
def download(softpath):
    command = 'cd ' + softpath + ' && wget --no-check-certificate https://pilot.ascon.ru/release/pilot-server.zip && unzip pilot-server.zip'
    #command = 'cd ' + softpath + ' && cp /home/bileyg/pilot-serv/beta/pilot-server.zip /opt/pilot-server/ && unzip -o pilot-server.zip'
    p = subprocess.Popen(command, shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)
    out = str(p.stdout.read())
    err = str(p.stderr.read())
