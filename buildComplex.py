# buildComplex.py
import sys,os
import curses
import subprocess

def adduser(softpath):
    command = 'sudo adduser pilotuser --disabled-password --no-create-home --gecos username && echo "username:userpass" | chpasswd && chown pilotuser -Rv ' + softpath
    p = subprocess.Popen(command, shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)
    #out = str(p.stdout.read())
    #err = str(p.stderr.read())

def service(softpath):
    command1 = 'sudo mkdir '+softpath+'/bin/ && mkdir '+softpath+'/Update/ && cp '+softpath+'/updateScript.sh '+softpath+'/bin/'
    command2 = 'cp ./sysd/pilot-server.service /etc/systemd/system'
    command3 = 'cp ./sysd/pilot-update.service /etc/systemd/system'
    command4 = 'systemctl enable pilot-server.service && systemctl daemon-reload'
    command = command1 + ' && ' + command2 + ' && ' + command3 + ' && ' + command4
    p = subprocess.Popen(command, shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)
    
def sudoers(softpath):
    sudoers = '/etc/sudoers'
    check = open('sudoers-add','r')
    chq = str(check.read(1))
    check.close()
    if chq == str(0):
        sudoersline0 = '\n'
        sudoersline1 = 'Cmnd_Alias PIL_CMDS = /bin/systemctl start pilot-update.service, /bin/systemctl stop pilot-update.service, /bin/systemctl start pilot-service.service, /bin/systemctl stop pilot-service.service\n'
        sudoersline2 = '\n'
        sudoersline3 = 'pilotuser ALL=(ALL) NOPASSWD: PIL_CMDS\n'
        wri = open(sudoers,'a')
        wri.write(sudoersline0)
        wri.write(sudoersline1)
        wri.write(sudoersline2)
        wri.write(sudoersline3)
        wri.close()
        mess = 'sudoers was changed with pilotuser addition'
        check = open('sudoers-add','w')
        check.write(str(1))
        check.close()
    else:
        mess = 'sudoers was already changed by Pilot-TUI'
    return mess
                
