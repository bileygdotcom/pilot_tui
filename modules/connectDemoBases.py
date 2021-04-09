# connectDemoBases.py
import subprocess

def attach(slotPath):
    basepath = slotPath + '/bases'
    demoBases = ['pilot-ice_ru']
    #for n in range(0,len(demoBases)):
    n = 0
    command = 'sudo ' + slotPath + '/Ascon.Pilot.Daemon --db ' + slotPath + '/settings.xml '+demoBases[n]+' '+basepath+'/'+demoBases[n]+'/base.dbp '+basepath+'/'+demoBases[n]+'/FileArchive'
    subprocess.Popen(command, shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)