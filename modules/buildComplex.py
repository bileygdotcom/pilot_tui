# buildComplex.py
import sys,os
import curses
import subprocess

def adduser(slotPath):
    command = 'sudo adduser pilotuser --disabled-password --no-create-home --gecos username && echo "username:userpass" | chpasswd && chown pilotuser -Rv ' + slotPath
    subprocess.Popen(command, shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)
    #out = str(p.stdout.read())
    #err = str(p.stderr.read())

def service(slotPath, ServN):
    command1 = 'sudo mkdir '+slotPath+'/bin/ && mkdir '+slotPath+'/Update/ && cp ./sysd/updateScript.sh '+slotPath+'/bin/'
    command2 = 'cp ./sysd/pilot-server_'+ServN+'.service /etc/systemd/system'
    command3 = 'cp ./sysd/pilot-update_'+ServN+'.service /etc/systemd/system'
    command4 = 'systemctl enable pilot-server_'+ServN+'.service && systemctl daemon-reload'
    command = command1 + ' && ' + command2 + ' && ' + command3 + ' && ' + command4
    subprocess.Popen(command, shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)
    
def sudoers():
    sudoers = '/etc/sudoers'
    check = open('sudoers-add','r')
    chq = str(check.read(1))
    check.close()
    if chq == str(0):
        sudoersline0 = '\n'

        sudoersline1 = 'Cmnd_Alias PIL_CMDS1 = /bin/systemctl start pilot-update_1.service, /bin/systemctl stop pilot-update_1.service, /bin/systemctl start pilot-service_1.service, /bin/systemctl stop pilot-service_1.service\n'
        sudoersline2 = 'Cmnd_Alias PIL_CMDS2 = /bin/systemctl start pilot-update_2.service, /bin/systemctl stop pilot-update_2.service, /bin/systemctl start pilot-service_2.service, /bin/systemctl stop pilot-service_2.service\n'
        sudoersline3 = 'Cmnd_Alias PIL_CMDS3 = /bin/systemctl start pilot-update_3.service, /bin/systemctl stop pilot-update_3.service, /bin/systemctl start pilot-service_3.service, /bin/systemctl stop pilot-service_3.service\n'
        sudoersline4 = 'Cmnd_Alias PIL_CMDS4 = /bin/systemctl start pilot-update_4.service, /bin/systemctl stop pilot-update_4.service, /bin/systemctl start pilot-service_4.service, /bin/systemctl stop pilot-service_4.service\n'

        sudoersline5 = '\n'
        sudoersline6 = 'pilotuser ALL=(ALL) NOPASSWD: PIL_CMDS1, PIL_CMDS2, PIL_CMDS3, PIL_CMDS4\n'
        wri = open(sudoers,'a')
        wri.write(sudoersline0)
        wri.write(sudoersline1)
        wri.write(sudoersline2)
        wri.write(sudoersline3)
        wri.write(sudoersline4)
        wri.write(sudoersline5)
        wri.write(sudoersline6)

        wri.close()
        mess = 'sudoers was changed with pilotuser addition'
        check = open('sudoers-add','w')
        check.write(str(1))
        check.close()
    else:
        mess = 'sudoers was already changed by Pilot-TUI'
    return mess
                
