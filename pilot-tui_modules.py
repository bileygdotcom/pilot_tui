#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
#  pilot-tui_modules.py
#  
#  Copyright 2020 bileyg <bileyg@bodhi>
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#  
#  
import sys
import curses
import time
#modules in folder
sys.path.insert(1, './modules')
import os
import json
import purge
import where
import getPic
import configure
import connectDemoBases
import renderImage
import bar
import helpPage
import renderWindow
import initColor
from modules import switchSelect
import loadUrl
import stopServices
import selectServerVersion
import setUp
import chmodX
import buildComplex
import pickle
import connectBase
import testServer
import portSetting


def draw_menu(stdscr, tilist, conflist, Fconf, F_Done):

    #k - is the pressed key variable. set it on 0
    k = 0
    cursor_x = 0
    cursor_y = 0
    
    #some preliminary vars
    tuiQuit = False
    firsttime = True
    showWindow = True
    out = "currently no comands"
    err = "no messages yet"
    softpath = '/opt/pilot-servers/'
    Ftitle = " No selection "
    MenuState = 0
    stringaz = ""
    whatkey = "left"
    colA = 4
    colB = 3
    Status = 0
    firstPurge = True
    firstLoad = True
    firstUnpac = True
    firstAuth = True
    firstLaunch = True
    firstBuild = True
    firstConnect = True
    installed = False
    ScreenN = 0
    serverON = True
    servSelect = False
    sel = False
    selServ = 1
    go = False
    serverVersion = [0,'no server','no server','no server','no server']

    # server slots matrix
    # [selected, installed, launched, autostart, version]
    if os.path.isfile('./saves/serverslots'):
        save = open('./saves/serverslots', 'rb')
        serverSlots = pickle.load(save)
        save.close()

    else:
        serverSlot1 = [False, False, False, False, False]
        serverSlot2 = [False, False, False, False, False]
        serverSlot3 = [False, False, False, False, False]
        serverSlot4 = [False, False, False, False, False]
        serverSlots = [False, serverSlot1, serverSlot2, serverSlot3, serverSlot4]
        save = open('./saves/serverslots', 'wb')
        pickle.dump(serverSlots, save)
        save.close()

    for sss in range(1,5):
        if os.path.isfile(softpath+'slot_'+str(sss)):
            serverSlots[sss][1] = True
        else:
            serverSlots[sss][1] = False

    
    # Declaration of about strings
    B = '\U00002588'
    title = "Terminal User Interface for Linux"
    subtitle = "Made with Python3 Curses"
    keystr = "bileyg | Sankt-Peterburg"

    # Existance
    #direxists, fileexists = where.existance()
    
    #number text
    N_text1 = " 1 "
    N_text2 = " 2 "
    N_text3 = " 3 "
    N_text4 = " 4 "
    N_text5 = " 5 "

    # init curses colors and colorpairs
    initColor.initPairs()

    # Clear and refresh the screen for a blank canvas
    stdscr.erase()
    stdscr.refresh()

    
    ##############################################
    # Loop where k is the last character pressed #
    ##############################################
        
    while (k != curses.KEY_F12 or tuiQuit == True):

        # Existance
        for sli in range(1,5):
            slotPath = softpath + 'slot_' + str(sli)
            direx, filex = where.existance(slotPath)
            if direx == True and filex == True:
                serverSlots[sli][1] = True
                #get server version
                serverVersion[sli] = testServer.url(sli)[13:]

        # Initialization
        stdscr.erase()
        height, width = stdscr.getmaxyx()

        # Centering calculations
        start_x_title = int((width // 2) - (len(title) // 2) - len(title) % 2)
        start_x_subtitle = int((width // 2) - (len(subtitle) // 2) - len(subtitle) % 2)
        start_x_keystr = int((width // 2) - (len(keystr) // 2) - len(keystr) % 2)

        start_x_logo = int((width // 2) - (len(tilist[0]) // 2) - len(tilist[0]) % 2) - 2
        start_y = int((height // 2) - 2)

        center_y = int((height// 2))
        center_x = int((width // 2))

        ################################################################
        ## DEFINITION OF KEYS   ########################################
        ################################################################
        
        ## F-KEYS ##

        if Status == 0:
            if k == ord('s'):
                Status = 1

        if Status == 1:
            if k == curses.KEY_F1:
                Status = 2

        if Status == 2:
            if k == curses.KEY_F2:
                Status = 1

        if Status == 3:
            if k == curses.KEY_F9:
                Status = 5

        if Status == 1 or Status == 2:
            if k == curses.KEY_F9:
                Status = 3
            if k == curses.KEY_F8:
                Status = 4
            if k == curses.KEY_F2:
                Status = 6
            if k == curses.KEY_F5:
                Status = 8
            if k == curses.KEY_F7:
                buildComplex.chownPS()
            
        ## END OF DEFINITION OF F-KEYS renderWindow.smallWindow(center_x, center_y, "DB connected. Press a key", -39, 6)#################################

        ################################################################
        # SCENERY PROCESSOR ############################################
        ################################################################

        # open next scenery
        with open("./Scenery/Scenery_" + str(Status) + ".json", 'r') as j:
            json_data = json.load(j)
            functions = json_data['functions']

        # run around all functions in scenery
        for n in range(len(functions)):
            function = functions[n]
            funcName = function["function"]

            if funcName == "Image":
                tilist = getPic.loadImage2(function["imagePath"])
                renderImage.renderImage(stdscr, height, width, tilist, center_x, center_y, B)

            if funcName == "Topper":
                bar.renderTopper(stdscr, width)

            if funcName == "Subtitle":
                bar.renderSubtitle(stdscr, start_y, start_x_title, title)

            if funcName == "Statusbar":
                statusbarstr1 = function["statusbarstr1"]
                statusbarstr2 = function["statusbarstr2"]
                bar.renderStatusBar(stdscr, Status, height, width, statusbarstr1, statusbarstr2)

            if funcName == "Windowstart":
                #if k == ord('s'):
                    #Status = 1
                if firsttime == True:
                    firsttime = False
                else:
                    renderWindow.windowStart(center_x, center_y, k)

            if funcName == "Helppage":
                helpPage.screenHelp(center_x, center_y)
                Status = 1

            if funcName == "Switchselect":
                #serverSlots select with keys 1-4
                if k == ord('1'):
                    selServ = 1
                if k == ord('2'):
                    selServ = 2
                if k == ord('3'):
                    selServ = 3
                if k == ord('4'):
                    selServ = 4

                servN = str(selServ)

                # to move arrows
                for ss in range(1,5):
                    serverSlots[ss][0] = False
                serverSlots[selServ][0] = True

                # F3, F4 to move switchers
                if serverSlots[selServ][1] == True:
                    if k == curses.KEY_F3:
                        serverSlots[selServ][2] = not serverSlots[selServ][2]
                    if k == curses.KEY_F4:
                        serverSlots[selServ][3] = not serverSlots[selServ][3]
                    # start & stop service
                    if serverSlots[selServ][2] == True:
                        buildComplex.serviceStart(servN)
                    else:
                        buildComplex.serviceStop(servN)
                    # enable & disable service
                    if serverSlots[selServ][3] == True:
                        buildComplex.serviceEnable(servN)
                    else:
                        buildComplex.serviceDisable(servN)

                # launch renderer
                time.sleep(0.1)
                switchSelect.serverSelect(center_x, center_y, serverSlots, B, serverON, serverVersion)

                #switchselector end

            if funcName == "Selectserverversion":
                move = False
                selectServerVersion.window(center_x, center_y, selServ)
                if k == ord('1'):
                    move = True
                    serverVersionUrl = 'https://pilot.ascon.ru/release/pilot-server.zip'
                if k == ord('2'):
                    serverVersionUrl = 'https://pilot.ascon.ru/beta/pilot-server.zip'
                    move = True
                if k == ord('3'):
                    serverVersionUrl = 'https://pilot.ascon.ru/alpha/pilot-server.zip'
                    move = True
                if k == ord('4'):
                    #inputWindow(center_x, center_y, promtText, moveX, moveY, lenght, gap)
                    inputUrl = renderWindow.inputWindow(center_x, center_y, "Input URL:", -39, 3, 77, 13)
                    serverVersionUrl = inputUrl
                    #renderWindow.smallWindow(center_x, center_y, "Got it! Press a key.", 9)
                    move = True
                if move == True:
                    time.sleep(0.2)
                    Status = 5
                    renderWindow.smallWindow(center_x, center_y, "  Got it! Press a key.", -13, 6)

            if funcName == "Construction":
                slotPath = softpath + 'slot_' + str(selServ)
                direx, filex = where.existance(slotPath)
                if direx == True:
                    renderWindow.smallWindow(center_x, center_y, "Server exists", -39, 0)
                else:
                    loadUrl.makeFolder(slotPath)
                    renderWindow.smallWindow(center_x, center_y, "Construction process:", -39, -6)
                    renderWindow.smallWindow(center_x, center_y, "The folder was created.", -39, -3)
                    renderWindow.smallWindow(center_x, center_y, "Downloading server....", -39, 0)
                    loadUrl.downloadServer(slotPath, serverVersionUrl)
                    renderWindow.smallWindow(center_x, center_y, "Server was downloaded.", -39, 0)
                    renderWindow.smallWindow(center_x, center_y, "Downloading bases....", -39, 3)
                    loadUrl.downloadBase(slotPath)
                    renderWindow.smallWindow(center_x, center_y, "Bases were downloaded.", -39, 3)
                    loadUrl.unzipServer(slotPath)
                    renderWindow.smallWindow(center_x, center_y, "Server was unzipped.", -39, 0)
                    chmodX.setX(slotPath)
                    renderWindow.smallWindow(center_x, center_y, "chmod Ascon.Pilot.Daemon", -39, 0)
                    loadUrl.unzipBase(slotPath)
                    renderWindow.smallWindow(center_x, center_y, "Bases were unzipped.", -39, 3)
                    portSetting.setSlot(slotPath, selServ)
                    renderWindow.smallWindow(center_x, center_y, "Ready. Press a key.", -39, 6)
                Status = 6

            if funcName == "Setadmin":
                slotPath = softpath + 'slot_' + str(selServ)
                renderWindow.smallWindow(center_x, center_y, "Add Administrator.", -39, -6)
                #inputWindow(center_x, center_y, promtText, moveX, moveY, lenght, gap)
                login = renderWindow.inputWindow(center_x, center_y, "Enter login: ", -39, -3, 27, 15)
                passw = renderWindow.inputWindow(center_x, center_y, "Enter passw: ", -39, 0, 27, 15)
                setUp.rights(slotPath, login, passw)
                time.sleep(1.5)
                renderWindow.smallWindow(center_x, center_y, "Got it!...", -39, 3)
                Status = 7

            if funcName == "Purge":
                slotPath = softpath + 'slot_' + str(selServ)
                direx, filex = where.existance(slotPath)
                if direx == False:
                    renderWindow.smallWindow(center_x, center_y, "Server doesn't exist", -39, 0)
                else:
                    if serverSlots[selServ][2] == True:
                        stopServices.stopPilotServer(selServ)
                        renderWindow.smallWindow(center_x, center_y, "Services are stopped.", -39, -3)
                        serverSlots[selServ][2] = False
                    else:
                        renderWindow.smallWindow(center_x, center_y, "Services were stopped.", -39, -3)
                    if serverSlots[selServ][3] == True:
                        stopServices.stopPilotUpdate(selServ)
                        renderWindow.smallWindow(center_x, center_y, "Update is stopped.", -39, -3)
                        serverSlots[selServ][3] = False
                    else:
                        renderWindow.smallWindow(center_x, center_y, "Update was stopped.", -39, -3)

                    if serverSlots[selServ][0] == True:
                        stopServices.disablePilotServices(selServ)
                        renderWindow.smallWindow(center_x, center_y, "Services are disabled.", -39, 0)
                    else:
                        renderWindow.smallWindow(center_x, center_y, "Services were disabled.", -39, 0)

                    purge.removePilotDirectory(slotPath)
                    serverSlots[selServ][1] = False
                    renderWindow.smallWindow(center_x, center_y, "Directory is removed.", -39, 3)
                    renderWindow.smallWindow(center_x, center_y, "Purged. Press a key.", -39, 6)
                Status = 1

            if funcName == "System":
                ServN = str(selServ)
                slotPath = softpath + 'slot_' + ServN
                direx, filex = where.existance(slotPath)
                if direx == False:
                    renderWindow.smallWindow(center_x, center_y, "Server doesn't exist", -39, 0)
                else:
                    buildComplex.adduser(slotPath)
                    renderWindow.smallWindow(center_x, center_y, "User 'pilotuser' was added.", -39, -3)
                    time.sleep(0.5)
                    buildComplex.service(slotPath, ServN)
                    renderWindow.smallWindow(center_x, center_y, "Pilot-Server is Service now.", -39, 0)
                    time.sleep(0.5)
                    buildComplex.sudoers()
                    time.sleep(0.5)
                    buildComplex.chownPS()
                    renderWindow.smallWindow(center_x, center_y, "Rights were set.", -39, 3)
                    time.sleep(0.5)
                    renderWindow.smallWindow(center_x, center_y, "Ready! Press a key.", -39, 6)

                    # write filex
                    check = open(slotPath + '/pilot-tui', 'w')
                    check.write(str(1))
                    check.close()
                Status = 1

            if funcName == "Baseconnect":
                slotPath = softpath + 'slot_' + str(selServ)
                direx, filex = where.existance(slotPath)
                if direx == False:
                    renderWindow.smallWindow(center_x, center_y, "Server doesn't exist", -39, 0)
                    Status = 1
                else:
                    renderWindow.smallWindow(center_x, center_y, "Connect Databases:", -39, -6)
                    renderWindow.smallWindow(center_x, center_y, "Input 'demo' for demo DB", -39, -3)
                    renderWindow.smallWindow(center_x, center_y, "Or input full path to DB", -39, 0)
                    renderWindow.smallWindow(center_x, center_y, "Or 'no' to quit this", -39, 3)

                    input = renderWindow.inputWindow(center_x, center_y, "Input:", -39, 6, 77, 13)

                    if input == 'demo':
                        connectDemoBases.attach(slotPath)
                        #Status = 1
                    elif input == 'no':
                        Status = 1
                    else:
                        name = renderWindow.inputWindow(center_x, center_y, "DB name:", -39, 6, 77, 13)
                        connectBase.attach(slotPath, input, name)
                        #Status = 1
                buildComplex.chownPS()
                Status = 1






        #cursor move works if right before the refresh()
        #stdscr.move(cursor_y, cursor_x)
        
        # Refresh the screen
        stdscr.refresh()
        
        firsttime = False

        # Wait for next input
        k = stdscr.getch()

    #saving the serverslot matrix on F12 exit
    save = open('./saves/serverslots', 'wb')
    pickle.dump(serverSlots, save)
    save.close()

        

def main():
    curses.wrapper(draw_menu, getPic.loadImage(), configure.loadConfig(), configure.configMatrix(configure.loadConfig()),configure.doneMatrix())
    #curses.wrapper(draw_menu)

if __name__ == "__main__":
    main()
