# connectDemoBases.py
import subprocess

def attach(slotPath, basepath, basename):
    command = 'sudo ' + slotPath + '/Ascon.Pilot.Daemon --db ' + slotPath + '/settings.xml '+basename+' '+basepath+'/base.dbp '+basepath+'/FileArchive'
    subprocess.Popen(command, shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)
    
