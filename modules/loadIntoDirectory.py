# loadIntoDirectory.py
import sys,os
import curses
import subprocess

def makeFolder(slotPath):
    basepath = slotPath + "/bases"
    command = 'mkdir -p ' + slotPath + ' && mkdir -p ' + basepath
    p = subprocess.Popen(command, shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)
    out = str(p.stdout.read())
    err = str(p.stderr.read())
    
def downloadServer(slotPath):
    command = 'cd ' + slotPath + ' && wget --no-check-certificate https://pilot.ascon.ru/release/pilot-server.zip'
    subprocess.Popen(command, shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)
    #out = str(p.stdout.read())
    #err = str(p.stderr.read())

def downloadBase(slotPath):
    basepath = slotPath + "/bases"
    command = 'cd ' + basepath + ' && wget --no-check-certificate https://pilot.ascon.ru/release/Databases.zip'
    subprocess.Popen(command, shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)
    #out = str(p.stdout.read())
    #err = str(p.stderr.read())
    
def unzipServer(slotPath):
    command = 'cd ' + slotPath + ' && unzip pilot-server.zip'
    subprocess.Popen(command, shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)

def unzipBase(slotPath):
    basepath = slotPath + "/bases"
    command = 'cd ' + basepath + ' && unzip Databases.zip'
    subprocess.Popen(command, shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)
