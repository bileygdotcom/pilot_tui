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
import sys,os
import curses
import subprocess
import resource
from getpass import getpass
import time
#modules in folder
sys.path.insert(1, './modules')
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

def draw_menu(stdscr, tilist, conflist, Fconf, F_Done):
        
    def serverState():
        # Help screen
        
        def srvNum(y,col,num):
            if servSelect1 == True:
                tw1.addstr(5,4," >>> ")
            else:
                tw1.addstr(5,4, "    ")
            if servSelect2 == True:
                tw1.addstr(7,4," >>> ")
            else:
                tw1.addstr(7,4, "    ")
            if servSelect3 == True:
                tw1.addstr(9,4," >>> ")
            else:
                tw1.addstr(9,4, "    ")
            if servSelect4 == True:
                tw1.addstr(11,4," >>> ")
            else:
                tw1.addstr(11,4, "    ")

            tw1.attron(curses.color_pair(col))
            tw1.addstr(y,4+6,"  "+str(num)+"  ")
            tw1.attroff(curses.color_pair(col))
            tw1.addstr(y,13+6,"O ")
            tw1.addstr(y,21+6,"  I")
            tw1.addstr(y,28+6,"O ")
            tw1.addstr(y,36+6,"  I")
            tw1.addstr(y,43+6,"out")
            
        def srvSwitcher(y,px):
            tw1.attron(curses.color_pair(21))
            tw1.attron(curses.A_BOLD)
            tw1.addstr(y,butx+px,B+B+B)
            tw1.attroff(curses.A_BOLD)
            tw1.addstr(y,butx+3+px,B)
            tw1.attroff(curses.color_pair(21))
            tw1.attron(curses.color_pair(7))
            tw1.attron(curses.A_BOLD)
            tw1.addstr(y,blcx+px,B+B+B)
            tw1.attroff(curses.A_BOLD)
            tw1.attroff(curses.color_pair(7))
            
        #outpt = testServer.url()
        #out = str(outpt)[1:]
        tw1 = curses.initscr()
        wdh = 72
        hgt = 16
        WX = (center_x - (wdh)//2)
        WY = (center_y - hgt//2)
        CP = 21
        SP = 1
        tw1 = curses.newwin(hgt, wdh, WY, WX)
        
        if serverON == False:
            butx = 15+6
            blcx = 19+6
        else:
            butx = 18+6
            blcx = 15+6
            
        tw1.attron(curses.color_pair(3))
        tw1.attron(curses.A_BOLD)
        tw1.addstr(3,4," Sel  Serv#      Launched      Autostart     Version            ")
        tw1.attroff(curses.color_pair(3))
        tw1.attroff(curses.A_BOLD)
            
        srvNum(5,6,1)
        srvSwitcher(5,0)
        srvSwitcher(5,15)
        srvNum(7,6,2)
        srvSwitcher(7,0)
        srvSwitcher(7,15)
        srvNum(9,6,3)
        srvSwitcher(9,0)
        srvSwitcher(9,15)
        srvNum(11,6,4)
        srvSwitcher(11,0)
        srvSwitcher(11,15)
        
        tw1.border()
        tw1.refresh()
        #time.sleep(0.5)
        # Label
        tw2 = curses.initscr()
        wdh = 16
        hgt = 3
        WX = (center_x - (wdh)//2)
        WY = WY-1
        CP = 5
        tw2 = curses.newwin(hgt, wdh, WY, WX)
        tw2.attron(curses.color_pair(CP))
        tw2.addstr(1,1,"    STATUS    ")
        tw2.attroff(curses.color_pair(CP))
        tw2.border()
        tw2.refresh()


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
    servSelect1 = False
    servSelect2 = False
    servSelect3 = False
    servSelect4 = False
    
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
    
    # Start colors in curses
    curses.start_color()
    curses.init_pair(1, curses.COLOR_CYAN, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)
    curses.init_pair(3, curses.COLOR_BLACK, curses.COLOR_WHITE)
    curses.init_pair(4, curses.COLOR_BLACK, curses.COLOR_CYAN)
    curses.init_pair(5, curses.COLOR_BLACK, curses.COLOR_YELLOW)
    curses.init_pair(6, curses.COLOR_WHITE, curses.COLOR_MAGENTA)
    curses.init_pair(7, curses.COLOR_BLACK, curses.COLOR_BLUE)
    curses.init_pair(8, curses.COLOR_WHITE, curses.COLOR_GREEN)
    curses.init_pair(9, curses.COLOR_WHITE, curses.COLOR_BLACK)
    curses.init_pair(10, curses.COLOR_BLUE, curses.COLOR_BLACK)
    
    #colors for logo. 
    curses.init_pair(20, curses.COLOR_BLACK,  curses.COLOR_WHITE)
    curses.init_pair(21, curses.COLOR_RED,    curses.COLOR_WHITE)
    curses.init_pair(22, curses.COLOR_GREEN,  curses.COLOR_WHITE)
    curses.init_pair(23, curses.COLOR_YELLOW, curses.COLOR_WHITE)
    curses.init_pair(24, curses.COLOR_BLUE,   curses.COLOR_WHITE)
    curses.init_pair(25, curses.COLOR_MAGENTA,curses.COLOR_WHITE)
    curses.init_pair(26, curses.COLOR_CYAN,   curses.COLOR_WHITE)
    curses.init_pair(27, curses.COLOR_WHITE,  curses.COLOR_BLACK)
    curses.init_pair(28, curses.COLOR_BLACK,  curses.COLOR_WHITE)
    curses.init_pair(29, curses.COLOR_RED,    curses.COLOR_WHITE)
    curses.init_pair(30, curses.COLOR_GREEN,  curses.COLOR_WHITE)
    curses.init_pair(31, curses.COLOR_YELLOW, curses.COLOR_WHITE)
    curses.init_pair(32, curses.COLOR_BLUE,   curses.COLOR_WHITE)
    curses.init_pair(33, curses.COLOR_MAGENTA,curses.COLOR_WHITE)
    curses.init_pair(34, curses.COLOR_CYAN,   curses.COLOR_WHITE)
    curses.init_pair(35, curses.COLOR_WHITE,  curses.COLOR_BLACK)

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

        # It's all about cursor
        #if k == curses.KEY_DOWN:
            #cursor_y = cursor_y + 1
        #elif k == curses.KEY_UP:
            #cursor_y = cursor_y - 1
        #elif k == curses.KEY_RIGHT:
            #cursor_x = cursor_x + 1
        #elif k == curses.KEY_LEFT:
            #cursor_x = cursor_x - 1
        #cursor_x = max(0, cursor_x)
        #cursor_x = min(width-1, cursor_x)
        #cursor_y = max(0, cursor_y)
        #cursor_y = min(height-1, cursor_y)
        
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
            
            ## Digits KEYS ##
            if ScreenN == 2:
                if k == ord('1'):
                    servSelect1 = True
                    servSelect2 = False
                    servSelect3 = False
                    servSelect4 = False
                if k == ord('2'):
                    servSelect1 = False
                    servSelect2 = True
                    servSelect3 = False
                    servSelect4 = False
                if k == ord('3'):
                    servSelect1 = False
                    servSelect2 = False
                    servSelect3 = True
                    servSelect4 = False
                if k == ord('4'):
                    servSelect1 = False
                    servSelect2 = False
                    servSelect3 = False
                    servSelect4 = True
            
        ## END OF DEFINITION OF F-KEYS #################################
        
 
              
        ################################################################
        # MENUSTATE = 0 ################################################
        ################################################################
        
        # Render Status Bar
        bar.renderStatusBar(stdscr, Status, height, width)
        
        
        if MenuState == 0:
            
            showWindow = False
            
        # Status 0. Logo
        if Status == 0:
            tilist = getPic.loadImage2("./image/00_pilottui-logo.ti")
            bar.renderTopper(stdscr, width)
            renderImage.renderImage(stdscr, height, width, tilist, center_x, center_y, B)
            bar.renderSubtitle(stdscr, start_y, start_x_title, title)
            bar.renderStatusBar(stdscr, Status, height, width)
            if firsttime == False:
                Status = renderWindow.windowStart(center_x, center_y, k)
                
        # Status 1. Check
        if Status == 1:
            tilist = getPic.loadImage2("./image/00_pilottui-logo.ti")
            bar.renderTopper(stdscr, width)
            renderImage.renderImage(stdscr, height, width, tilist, center_x, center_y, B)
            bar.renderSubtitle(stdscr, start_y, start_x_title, title)
            bar.renderStatusBar(stdscr, Status, height, width)
            #Status = renderWindowOverLogo()
            if direxists == True and fileexists == True:
                outstring1 = " STATUS:  "
                exstatus = True
            else:
                outstring1 = " WARNING! "
                exstatus = False 
            if direxists == True:
                outstring2 = " Pilot-Server's default directory was found. "
                if fileexists == True:
                    outstring3 = " It was installed with Pilot-TUI. All's ok!"
                    statusNext = 10
                    statusPres = 1
                    labelColor = 8
                else:
                    outstring3 = " Pilot-Server was installed without Pilot-TUI."
                    statusNext = 2
                    statusPres = 1
                    labelColor = 5
            else:
                outstring2 = " Directory /opt/pilot-server is apsent."
                outstring3 = " Another location or not installed at all."
                statusNext = 4
                statusPres = 1
                labelColor = 4
            wWidth = 66
            wHeight = 6
            Ypos = 3
            btn = 'n'
            btnText = "'N' -  Next step  "
            Status = renderWindow.renderWindowUpperCommon(k, center_x, center_y, outstring1, outstring2, outstring3, wWidth, wHeight,Ypos,btn,btnText,statusNext,statusPres,labelColor)
            
        
        # Status 2. Distrakt. Pilot-Server was set without Pilot-TUI
        if Status == 2:
            tilist = getPic.loadImage2("./image/04_Distrakt.ti")
            bar.renderTopper(stdscr, width)
            renderImage.renderImage(stdscr, height, width, tilist, center_x, center_y, B)
            bar.renderStatusBar(stdscr, Status, height, width)
            #renderWindow.renderWindowUpperCommon(k, center_x, center_y, outstring1, outstring2, outstring3, wWidth, wHeight,Ypos,btn,btnText)
            outstring1 = " WARNING! "
            outstring2 = "  Pilot-Server was installed without Pilot-TUI."
            outstring3 = "  It should be purged and reinstalled. "
            wWidth = 66
            wHeight = 6
            Ypos = -12
            btn = 'p'
            btnText = "'P' -  PURGE  "
            statusNext = 3
            statusPres = 2
            labelColor = 5
            Status = renderWindow.renderWindowUpperCommon(k, center_x, center_y, outstring1, outstring2, outstring3, wWidth, wHeight,Ypos,btn,btnText,statusNext,statusPres,labelColor)
            
        # Status 3. Purging.
        if Status == 3:
            tilist = getPic.loadImage2("./image/03_Purging.ti")
            bar.renderTopper(stdscr, width)
            renderImage.renderImage(stdscr, height, width, tilist, center_x, center_y, B)
            bar.renderStatusBar(stdscr, Status, height, width)
            if firstPurge == True:
                purge.stopPilotServer()
                renderWindow.smallWindow(center_x, center_y, "Services are stopped.",0)
                purge.disablePilotServices()
                renderWindow.smallWindow(center_x, center_y, "Services are disabled.",3)
                purge.removePilotDirectory()
                renderWindow.smallWindow(center_x, center_y, "Directory is removed.",6)
                firstPurge = False
            outstring1 = "  Well,  "
            outstring2 = "  Pilot-Server has been stopped, disabled & purged."
            outstring3 = "  Press 'N' to move to next step. "
            wWidth = 66
            wHeight = 6
            Ypos = -12
            btn = 'n'
            btnText = "'N' -  NEXT  "
            statusNext = 4
            statusPres = 3
            labelColor = 3
            Status = renderWindow.renderWindowUpperCommon(k, center_x, center_y, outstring1, outstring2, outstring3, wWidth, wHeight,Ypos,btn,btnText,statusNext,statusPres,labelColor)
            
        # Status 4. All's clear.
        if Status == 4:
            tilist = getPic.loadImage2("./image/05_AllsClear.ti")
            bar.renderTopper(stdscr, width)
            renderImage.renderImage(stdscr, height, width, tilist, center_x, center_y, B)
            bar.renderStatusBar(stdscr, Status, height, width)
            outstring1 = "  Clear,  "
            outstring2 = "  All's ready to build up fresh Pilot-Server."
            outstring3 = "  Press 'S' to start installation. "
            wWidth = 66
            wHeight = 6
            Ypos = -12
            btn = 's'
            btnText = "'S' -  Start  "
            statusNext = 5
            statusPres = 4
            labelColor = 3
            Status = renderWindow.renderWindowUpperCommon(k, center_x, center_y, outstring1, outstring2, outstring3, wWidth, wHeight,Ypos,btn,btnText,statusNext,statusPres,labelColor)
            
            
        # Status 5. Downloading.
        if Status == 5:
            tilist = getPic.loadImage2("./image/01_Downloading.ti")
            bar.renderTopper(stdscr, width)
            renderImage.renderImage(stdscr, height, width, tilist, center_x, center_y, B)
            bar.renderStatusBar(stdscr, Status, height, width)
            if firstLoad == True:
                loadIntoDirectory.makeFolder(softpath)
                renderWindow.smallWindow(center_x, center_y, "The folder was created.",0)
                renderWindow.smallWindow(center_x, center_y, "Downloading archive....",3)
                loadIntoDirectory.download(softpath)
                renderWindow.smallWindow(center_x, center_y, "Archive was downloaded.",3)
                firstLoad = False
            outstring1 = " ARRIVED "
            outstring2 = "  Pilot-Server was downloaded."
            outstring3 = "  Press 'U' to unzip package. "
            wWidth = 66
            wHeight = 6
            Ypos = -12
            btn = 'u'
            btnText = "'U' - Unzip  "
            statusNext = 6
            statusPres = 5
            labelColor = 3
            Status = renderWindow.renderWindowUpperCommon(k, center_x, center_y, outstring1, outstring2, outstring3, wWidth, wHeight,Ypos,btn,btnText,statusNext,statusPres,labelColor)

        # Status 6. Unpacking.
        if Status == 6:
            tilist = getPic.loadImage2("./image/02_Unpacking.ti")
            bar.renderTopper(stdscr, width)
            renderImage.renderImage(stdscr, height, width, tilist, center_x, center_y, B)
            bar.renderStatusBar(stdscr, Status, height, width)
            if firstUnpac == True:
                loadIntoDirectory.unzip(softpath)
                firstUnpac = False
            outstring1 = " UNZIP "
            outstring2 = "  Pilot-Server archive was unzipped"
            outstring3 = "  Press 'S' to set up the server. "
            wWidth = 66
            wHeight = 6
            Ypos = -12
            btn = 's'
            btnText = "'S' - Set up  "
            statusNext = 7
            statusPres = 6
            labelColor = 4
            Status = renderWindow.renderWindowUpperCommon(k, center_x, center_y, outstring1, outstring2, outstring3, wWidth, wHeight,Ypos,btn,btnText,statusNext,statusPres,labelColor)
        
        # Status 7. Construction.
        if Status == 7:
            tilist = getPic.loadImage2("./image/06_Construction.ti")
            bar.renderTopper(stdscr, width)
            renderImage.renderImage(stdscr, height, width, tilist, center_x, center_y, B)
            bar.renderStatusBar(stdscr, Status, height, width)
            if firstAuth == True:
                login = renderWindow.inputWindow(center_x, center_y, "Enter login: ",0)
                passw = renderWindow.inputWindow(center_x, center_y, "Enter passw: ",3)
                setUp.rights(softpath,login,passw)
                renderWindow.smallWindow(center_x, center_y, "Pilot-Server is set.",6)
                firstAuth = False
            #renderWindow.smallWindow(center_x, center_y, "Services are stopped.",0)
            outstring1 = " SET UP "
            outstring2 = "  Pilot-Server archive was set up. Time to test it!"
            outstring3 = "  Press 'L' to launch server for test. "
            wWidth = 66
            wHeight = 6
            Ypos = -12
            btn = 'l'
            btnText = "'L' - Launch  "
            statusNext = 8
            statusPres = 7
            labelColor = 5
            Status = renderWindow.renderWindowUpperCommon(k, center_x, center_y, outstring1, outstring2, outstring3, wWidth, wHeight,Ypos,btn,btnText,statusNext,statusPres,labelColor)
        
        # Status 8. Test Launch.
        if Status == 8:
            tilist = getPic.loadImage2("./image/07_Launch.ti")
            bar.renderTopper(stdscr, width)
            renderImage.renderImage(stdscr, height, width, tilist, center_x, center_y, B)
            bar.renderStatusBar(stdscr, Status, height, width)
            if firstLaunch == True:
                testServer.launch(softpath)
                time.sleep(1.5)
                outpt = testServer.url()
                out = str(outpt)[1:]
                #renderWindow.smallWindow(center_x, center_y, out,6)
                firstLaunch = False
            outstring1 = " TEST "
            outstring2 = " " + out + " was launched."
            outstring3 = "  Press 'M' to make service from server. "
            wWidth = 66
            wHeight = 6
            Ypos = -12
            btn = 'm'
            btnText = "'M' - make it "
            statusNext = 9
            statusPres = 8
            labelColor = 3
            Status = renderWindow.renderWindowUpperCommon(k, center_x, center_y, outstring1, outstring2, outstring3, wWidth, wHeight,Ypos,btn,btnText,statusNext,statusPres,labelColor)
        
        # Status 9. Build a Complex.
        if Status == 9:
            tilist = getPic.loadImage2("./image/08_System.ti")
            bar.renderTopper(stdscr, width)
            renderImage.renderImage(stdscr, height, width, tilist, center_x, center_y, B)
            bar.renderStatusBar(stdscr, Status, height, width)
            if firstBuild == True:
                buildComplex.adduser(softpath)
                renderWindow.smallWindow(center_x, center_y, "User 'pilotuser' was added.",0)
                time.sleep(0.5)
                buildComplex.service(softpath)
                renderWindow.smallWindow(center_x, center_y, "Pilot-Server is Service now.",3)
                time.sleep(0.5)
                buildComplex.service(softpath)
                renderWindow.smallWindow(center_x, center_y, "Automatization complete.",6)
                time.sleep(0.5)
                firstBuild = False
            outstring1 = " SERVICE "
            outstring2 = "  Pilot-Server was set as automatized service."
            outstring3 = "  Press 'F' to finish installation process. "
            wWidth = 66
            wHeight = 6
            Ypos = -12
            btn = 'f'
            btnText = "'F' - Finish  "
            statusNext = 10
            statusPres = 9
            labelColor = 3
            Status = renderWindow.renderWindowUpperCommon(k, center_x, center_y, outstring1, outstring2, outstring3, wWidth, wHeight,Ypos,btn,btnText,statusNext,statusPres,labelColor)
        
        
        # Status 10. Complete.
        if Status == 10:
            tilist = getPic.loadImage2("./image/09_Complete.ti")
            bar.renderTopper(stdscr, width)
            renderImage.renderImage(stdscr, height, width, tilist, center_x, center_y, B)
            bar.renderStatusBar(stdscr, Status, height, width)
            outstring1 = " READY "
            outstring2 = "  Pilot-Server is ready to work & needs databases."
            outstring3 = "  Press 'C' to connect it with databases. "
            wWidth = 66
            wHeight = 6
            Ypos = -12
            btn = 'c'
            btnText = "'C' - Connect  "
            statusNext = 11
            statusPres = 10
            labelColor = 3
            Status = renderWindow.renderWindowUpperCommon(k, center_x, center_y, outstring1, outstring2, outstring3, wWidth, wHeight,Ypos,btn,btnText,statusNext,statusPres,labelColor)
        
        # Status 11. Connect.
        if Status == 11:
            tilist = getPic.loadImage2("./image/10_Connect.ti")
            bar.renderTopper(stdscr, width)
            renderImage.renderImage(stdscr, height, width, tilist, center_x, center_y, B)
            bar.renderStatusBar(stdscr, Status, height, width)
            if firstConnect == True:
                #connectDemoBases.download(softpath)
                renderWindow.smallWindow(center_x, center_y, "Demobases were downloaded & unzipped",0)
                time.sleep(1.0)
                #connectDemoBases.unzip(softpath)
                #renderWindow.smallWindow(center_x, center_y, "... & unzipped.",3)
                #time.sleep(0.5)
                connectDemoBases.attach(softpath)
                renderWindow.smallWindow(center_x, center_y, "Demobases were connected.",6)
                time.sleep(0.5)
                firstConnect = False
            outstring1 = " BASES "
            outstring2 = "  Demobases were downloaded & connected"
            outstring3 = "  Press 'M' to go to main menu. "
            wWidth = 66
            wHeight = 6
            Ypos = -12
            btn = 'm'
            btnText = "'M' - Main menu  "
            statusNext = 12
            statusPres = 11
            labelColor = 3
            Status = renderWindow.renderWindowUpperCommon(k, center_x, center_y, outstring1, outstring2, outstring3, wWidth, wHeight,Ypos,btn,btnText,statusNext,statusPres,labelColor)
        
        # Status 12. FRONT.
        if Status == 12:
            installed = True
            tilist = getPic.loadImage2("./image/00_pilottui-logo.ti")
            bar.renderTopper(stdscr, width)
            renderImage.renderImage(stdscr, height, width, tilist, center_x, center_y, B)
            #renderImage()
            bar.renderSubtitle(stdscr, start_y, start_x_title, title)
            bar.renderStatusBar(stdscr, Status, height, width)
        
        # Status 13. UPDATE.
        if Status == 13:
            tilist = getPic.loadImage2("./image/11_Update.ti")
            bar.renderTopper(stdscr, width)
            renderImage.renderImage(stdscr, height, width, tilist, center_x, center_y, B)
            bar.renderStatusBar(stdscr, Status, height, width)
            outstring1 = " SYSTEM "
            outstring2 = "  Pilot-Server archive was downloaded"
            outstring3 = "  Press 'U' to unzip package. "
            wWidth = 66
            wHeight = 6
            Ypos = -12
            btn = 'u'
            btnText = "'U' - Unzip  "
            statusNext = 1
            statusPres = 13
            labelColor = 3
            Status = renderWindow.renderWindowUpperCommon(k, center_x, center_y, outstring1, outstring2, outstring3, wWidth, wHeight,Ypos,btn,btnText,statusNext,statusPres,labelColor)
        
        #Control SCREENS
        
        # Screen 1. HELP
        if ScreenN == 1:
            time.sleep(0.1)
            helpPage.screenHelp(center_x, center_y)
        
        # Screen 2. SRVS
        if ScreenN == 2:
            time.sleep(0.1)
            serverState()
        
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
