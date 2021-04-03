#loadUrl.py
import os
import urllib.request
import zipfile

def makeFolder(slotPath):
    os.makedirs(slotPath + '/bases')

def downloadServer(slotPath):
    url = 'https://pilot.ascon.ru/release/pilot-server.zip'
    urllib.request.urlretrieve(url, slotPath + '/pilot-server.zip')

def downloadBase(slotPath):
    basePath = slotPath + "/bases"
    url = 'https://pilot.ascon.ru/release/Databases.zip'
    urllib.request.urlretrieve(url, basePath + '/Databases.zip')
    
def unzipServer(slotPath):
    os.chdir(slotPath)
    z = zipfile.ZipFile('pilot-server.zip', 'r')
    z.extractall()

def unzipBase(slotPath):
    basePath = slotPath + "/bases"
    os.chdir(basePath)
    z = zipfile.ZipFile('Databases.zip', 'r')
    z.extractall()
