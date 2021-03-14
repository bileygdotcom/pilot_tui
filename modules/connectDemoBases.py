# connectDemoBases.py
import sys,os
import curses
import subprocess

#def download(softpath):
    #basepath = softpath + "/bases"
    #command1 = 'sudo mkdir ' + basepath
    #command2 = 'cd ' + basepath
    #command3 = 'wget --no-check-certificate https://pilot.ascon.ru/release/Databases.zip'
    #command4 = 'unzip Databases.zip'
    #command = command1 + ' && ' + command2 + ' && ' + command3 + ' && ' + command4
    #p = subprocess.Popen(command, shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)
    
#def unzip(softpath):
    #basepath = softpath + '/bases'
    #command = 'cd ' + basepath + ' && sudo unzip Databases.zip'
    #p = subprocess.Popen(command, shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)
    
def attach(softpath):
    basepath = softpath + '/bases'
    command = 'sudo ' + softpath + '/Ascon.Pilot.Daemon --db ' + softpath + '/settings.xml pilot-ice_ru ' + basepath + '/pilot-ice_ru/base.dbp pilot-ice_ru ' + basepath + '/pilot-ice_ru/FileArchive'
    p = subprocess.Popen(command, shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)
    
