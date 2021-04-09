#loadUrl.py
import os
import urllib.request
import zipfile
import time

def makeCustom(softpath):
    custom = softpath + 'custom/'
    if os.path.isdir(custom) == False:
        os.mkdir(custom)

def makeFolder(slotPath):
    os.makedirs(slotPath + '/bases')

def downloadServer(slotPath, serverVersionUrl):
    url = serverVersionUrl
    #print(url)
    time.sleep(2.0)
    headers = {'User-Agent': 'Mozilla/5.0'}
    urllib.request.urlretrieve(url, slotPath + '/pilot-server.zip')

def downloadBase(slotPath):
    basePath = slotPath + "/bases"
    url = 'https://pilot.ascon.ru/release/Databases.zip'
    urllib.request.urlretrieve(url, basePath + '/Databases.zip')
    
def unzipServer(slotPath):
    dir = os.path.abspath(os.curdir)
    os.chdir(slotPath)
    z = zipfile.ZipFile('pilot-server.zip', 'r')
    z.extractall()
    os.chdir(dir)

def unzipBase(slotPath):
    dir = os.path.abspath(os.curdir)
    basePath = slotPath + "/bases"
    os.chdir(basePath)
    z = zipfile.ZipFile('Databases.zip', 'r')
    z.extractall()
    os.chdir(dir)
