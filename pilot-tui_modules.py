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
import json
import purge
import where
import getPic
import configure
import loadIntoDirectory
import setUp
import testServer
import buildComplex
import connectDemoBases
import renderImage
import bar
import helpPage
import renderWindow
import initColor
from modules import switchSelect


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
    softpath = '/opt/pilot-server'
    Ftitle = " No selection "
    MenuState = 0
    stringaz = ""
    whatkey = "left"
    colA = 4
    colB = 3
    #Status = 0 - installation mode
    Status = 0
    #Status = 12 - normal mode
    #Status = 12
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

    # server slots matrix
    # [selected, installed, launched, autostart, version]
    serverSlot1 = [False, True, True, False, False]
    serverSlot2 = [False, False, False, True, False]
    serverSlot3 = [False, True, False, False, False]
    serverSlot4 = [False, False, True, False, False]
    serverSlots = [False, serverSlot1, serverSlot2, serverSlot3, serverSlot4]
    
    # Declaration of about strings
    B = '\U00002588'
    title = "Terminal User Interface for Linux"
    subtitle = "Made with Python3 Curses"
    keystr = "bileyg | Sankt-Peterburg"

    # Existance
    direxists, fileexists = where.existance()
    
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
        
        if installed == True:
            if k == curses.KEY_F1:
                ScreenN = 1
            if k == curses.KEY_F2:
                ScreenN = 2
            if k == curses.KEY_F3:
                ScreenN = 3
            if k == curses.KEY_F4:
                ScreenN = 4
            if k == curses.KEY_F5:
                ScreenN = 5
            if k == curses.KEY_F6:
                ScreenN = 6
            if k == curses.KEY_F7:
                StatusN = 7
            if k == curses.KEY_F8:
                StatusN = 8
            if k == curses.KEY_F9:
                StatusN = 9
            
        ## END OF DEFINITION OF F-KEYS #################################

        ################################################################
        # MENUSTATE = 0 ################################################
        ################################################################
        
        #if MenuState == 0:
            #showWindow = False

        # Status 0
        with open("./Scenery/Scenery_" + str(Status) + ".json", 'r') as j:
            json_data = json.load(j)
            functions = json_data['functions']
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
                    if k == ord('s'):
                        Status = 1
                    if firsttime == True:
                        firsttime = False
                    else:
                        renderWindow.windowStart(center_x, center_y, k)

                if funcName == "Switchselect":
                    serverSlots
                    if k == ord('1'):
                        selServ = 1
                    if k == ord('2'):
                        selServ = 2
                    if k == ord('3'):
                        selServ = 3
                    if k == ord('4'):
                        selServ = 4

                    for ss in range(1,5):
                        serverSlots[ss][0] = False
                    serverSlots[selServ][0] = True

                    if k == curses.KEY_F3:
                        serverSlots[selServ][2] = not serverSlots[selServ][2]
                    if k == curses.KEY_F4:
                        serverSlots[selServ][3] = not serverSlots[selServ][3]

                    time.sleep(0.1)
                    switchSelect.serverSelect(center_x, center_y, serverSlots, B, serverON)
        
        #cursor move works if right before the refresh()
        #stdscr.move(cursor_y, cursor_x)
        
        # Refresh the screen
        stdscr.refresh()
        
        firsttime = False

        # Wait for next input
        k = stdscr.getch()
        

def main():
    curses.wrapper(draw_menu, getPic.loadImage(), configure.loadConfig(), configure.configMatrix(configure.loadConfig()),configure.doneMatrix())
    #curses.wrapper(draw_menu)

if __name__ == "__main__":
    main()
