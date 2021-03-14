#getPic.py

import sys,os

def loadImage():

    #get terminal image
    tifile = open("./image/00_pilottui-logo.ti","r")
    tilist = tifile.readlines()
    tifile.close()
    return tilist
    
def loadImage2(imageName):

    #get terminal image
    tifile = open(imageName,"r")
    tilist = tifile.readlines()
    tifile.close()
    return tilist
