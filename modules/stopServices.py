#purge.py
import subprocess

def stopPilotServer(selServ):
    command = 'sudo /bin/systemctl stop pilot-server'+str(selServ)+'.service'
    
    p = subprocess.Popen(command, shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)
    out = str(p.stdout.read())
    err = str(p.stderr.read())
    #err = 'systemd services pilot-server & pilot-update have been stopped.'


def stopPilotUpdate(selServ):
    command = 'sudo /bin/systemctl stop pilot-update'+str(selServ)+'.service'

    p = subprocess.Popen(command, shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                         universal_newlines=True)
    out = str(p.stdout.read())
    err = str(p.stderr.read())
    # err = 'systemd services pilot-server & pilot-update have been stopped.'
    
def disablePilotServices(selServ):
    command1 = 'sudo /bin/systemctl disable pilot-server'+str(selServ)+'.service'
    command2 = '/bin/systemctl disable pilot-update'+str(selServ)+'.service'
    command3 = '/bin/systemctl daemon-reload'
    command = command1 + ' && ' + command2 + ' && ' + command3
    
    p = subprocess.Popen(command, shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)
    out = str(p.stdout.read())
    err = str(p.stderr.read())
    #err = 'systemd services pilot-server & pilot-update have been disabled.'
