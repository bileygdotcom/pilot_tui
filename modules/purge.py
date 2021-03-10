#purge.py

def stopPilotServer():
    command1 = 'sudo /bin/systemctl stop pilot-server.service'
    command2 = '/bin/systemctl stop pilot-update.service'
    command = command1 + ' && ' + command2
    
    p = subprocess.Popen(command, shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)
    out = str(p.stdout.read())
    err = str(p.stderr.read())
    #err = 'systemd services pilot-server & pilot-update have been stopped.'
    
def disablePilotServices():
    command1 = 'sudo /bin/systemctl disable pilot-server.service'
    command2 = '/bin/systemctl disable pilot-update.service'
    command3 = '/bin/systemctl daemon-reload'
    command = command1 + ' && ' + command2 + ' && ' + command3
    
    p = subprocess.Popen(command, shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)
    out = str(p.stdout.read())
    err = str(p.stderr.read())
    #err = 'systemd services pilot-server & pilot-update have been disabled.'
            
def removePilotDirectory():
                
    command = 'sudo rm -r /opt/pilot-server'
    p = subprocess.Popen(command, shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)
    out = str(p.stdout.read())
    err = str(p.stderr.read())
    #err = 'Pilot-server purged.'
