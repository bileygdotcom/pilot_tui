#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  pilot-tui.py
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
import purge
import where
import getPic
import configure

def draw_menu(stdscr,tilist,conflist,Fconf,F_Done):
    
    def renderImage():
        # Rendering logo
        # from the terminal image strings
        PixelMatrix = []
        PixelString = []
        PixelColors = ['0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F']
        if height >= 23 and width >= 80:
            for j in range(3,22):
                PixelString = tilist[j]
                for i in range(3,82):
                    Pixel = tilist[j][i]
                    PColor = PixelColors.index(Pixel)
                    stdscr.attron(curses.color_pair(20+PColor))
                    if PColor > 7:
                        stdscr.attron(curses.A_BOLD)
                    XX = (center_x - (len(PixelString)-4)//2)
                    YY = (center_y - 11)
                    stdscr.addstr(j-1+YY, i-3+XX, B)
                    #stdscr.addstr(start_y+j-11, start_x_logo+i, 'B')
                    if PColor > 7:
                        stdscr.attroff(curses.A_BOLD)
                    stdscr.attroff(curses.color_pair(20+PColor))
    
    def renderSubtitle():
        # Rendering subtitle
        stdscr.attron(curses.color_pair(1))
        stdscr.attron(curses.A_BOLD)
        stdscr.addstr(start_y+3, start_x_title+15, title)
        stdscr.attroff(curses.color_pair(2))
        stdscr.attroff(curses.A_BOLD)
            
    def renderTopper():
        # Topper showing the coordinates
        #whstr = "W-H: [{},{}]".format(width, height)
        #topperstr1 = whstr
        topperstr1 = ' \U00002297' + '  Pilot TUI v.2'
        topperstr2 = ' \U00002297' + '  terminal interface for Pilot-Server'
        topperstr3 = " "
        
        # Render topper1
        stdscr.attron(curses.color_pair(7))
        stdscr.addstr(0, 0, topperstr1)
        stdscr.addstr(0, len(topperstr1), " " * (width - len(topperstr1) - 1))
        stdscr.attroff(curses.color_pair(7))
        
        # Render topper2
        stdscr.attron(curses.color_pair(4))
        stdscr.addstr(1, 0, topperstr2)
        stdscr.addstr(1, len(topperstr2), " " * (width - len(topperstr2) - 1))
        stdscr.attroff(curses.color_pair(4))
        
        # Render topper3
        stdscr.attron(curses.color_pair(9))
        stdscr.addstr(2, 0, topperstr3)
        stdscr.addstr(2, len(topperstr3), " " * (width - len(topperstr3) - 1))
        stdscr.attroff(curses.color_pair(9))
        
    #def pressAnyKey():
        
        
    def renderStatusBar():
        # Render 2 nether Status Bars
        sbpair1 = 9
        sbpair2 = 3
        
        #normalization of names for menu
        Fconf0names = []
        for i in range(1,13):
            Fconf0 = Fconf[i][0]
            scl = len(Fconf0)
            if scl > 10:
                sss = (Fconf0[0:10])
            elif scl == 10:
                sss = Fconf0
            else:
                ascl = 10 - scl
                sss = Fconf0[0:10] + ' '*ascl
            Fconf0names.append(sss)
        FCN = Fconf0names
            
        if height >= 23 and width >= 79:
            
            if Status == 0 or Status == 1 or Status == 2 or Status == 3 or Status == 4:
                statusbarstr2 = " "
                statusbarstr1 = " "
            else:
                #statusbar menu set
                statusbarstr2 = " "+FCN[0]+" | "+FCN[1]+" | "+FCN[2]+" | "+FCN[3]+" | "+FCN[4]+" | "+FCN[5]+" |"
                statusbarstr1 = " "+FCN[6]+" | "+FCN[7]+" | "+FCN[8]+" | "+FCN[9]+" | "+FCN[10]+" | "+FCN[11]+" |"
            
        else:
            statusbarstr2 = "Window size should be minimum 79x23 "
            statusbarstr1 = " "
            
        # Render status bar
        stdscr.attron(curses.color_pair(sbpair1))
        stdscr.addstr(height-1, 0, statusbarstr1)
        stdscr.addstr(height-1, len(statusbarstr1), " " * (width - len(statusbarstr1) - 1))
        stdscr.attroff(curses.color_pair(sbpair1))
        
        # Render top status bar
        stdscr.attron(curses.color_pair(sbpair2))
        stdscr.addstr(height-2, 0, statusbarstr2)
        stdscr.addstr(height-2, len(statusbarstr2), " " * (width - len(statusbarstr2) - 1))
        stdscr.attroff(curses.color_pair(sbpair2))
        
    def windowStart():
        #WINDOW over Logo
        tw1 = curses.initscr()
        #winn = curses.newwin(wHeight, wWidth, begin_y, begin_x)
        WX = (center_x - (34)//2+9)
        WY = (center_y+3)
        CP = 1
        tw1 = curses.newwin(4, 34, WY, WX)
        tw1.attron(curses.color_pair(CP))
        tw1.addstr(1,3,"Pilot TUI has been launched")
        tw1.attroff(curses.color_pair(CP))
        if k == ord('s'):
            colA = 5
            Status = 1
        else:
            colA = 6
            Status = 0
        tw1.attron(curses.color_pair(CP))
        tw1.addstr(2,6,"PRESS")
        tw1.attroff(curses.color_pair(CP))
        tw1.attron(curses.color_pair(colA))
        tw1.addstr(2,13," 'S' ")
        tw1.attroff(curses.color_pair(colA))
        tw1.attron(curses.color_pair(CP))
        tw1.addstr(2,19,"TO START")
        tw1.attroff(curses.color_pair(CP))
        tw1.border()
        tw1.refresh()
        time.sleep(0.5)
        return Status
        
    def smallWindow(funcText,moveY):
        tw1 = curses.initscr()
        WX = (center_x - 39)
        WY = (center_y-1+moveY)
        CP = 1
        tw1 = curses.newwin(3, 27, WY, WX)
        tw1.attron(curses.color_pair(CP))
        tw1.addstr(1,2,funcText)
        tw1.attroff(curses.color_pair(CP))
        tw1.border()
        tw1.refresh()
        time.sleep(0.5)
        
    def renderWindowOverLogo():
            
            if direxists == True and fileexists == True:
                outstring1 = " STATUS:  "
                exstatus = True
            else:
                outstring1 = " WARNING! "
                exstatus = False
            
            if direxists == True:
                outstring2 = " Pilot-Server's directory /opt/pilot-server was found. "
                if fileexists == True:
                    outstring3 = " Pilot-Server was set with Pilot-TUI. All's ok!"
                else:
                    outstring3 = " Pilot-Server was installed without Pilot-TUI."
            else:
                outstring2 = " Directory /opt/pilot-server is apsent."
                outstring3 = " Another location or not installed at all."
            
            #WINDOW over Logo
            tw1 = curses.initscr()
            #winn = curses.newwin(wHeight, wWidth, begin_y, begin_x)
            WX = (center_x - (66)//2)
            WY = (center_y+3)
            tw1 = curses.newwin(6, 66, WY, WX)
            if exstatus == True:
                excol = 1
            else:
                excol = 5
            tw1.attron(curses.color_pair(excol))
            tw1.addstr(1,1,outstring1)
            tw1.attroff(curses.color_pair(excol))
            tw1.addstr(1,11,outstring2)
            tw1.addstr(2,11,outstring3)
            if k == ord('n'):
                colA = 5
                colB = 6
                Status = 2
            else:
                colA = 6
                colB = 6
                Status = 1
            tw1.attron(curses.color_pair(colA))
            tw1.addstr(4,20,"'N' -  NEXT  ")
            tw1.attroff(curses.color_pair(colA))
            tw1.attron(curses.color_pair(colB))
            tw1.addstr(4,40,"'F12' -  QUIT  ")
            tw1.attroff(curses.color_pair(colB))
            tw1.border()
            tw1.refresh()
            time.sleep(0.5)
            return Status
        
    def renderWindowUpperCommon(outstring1, outstring2, outstring3, wWidth, wHeight,Ypos,btn,btnText,statusNext,statusPres,labelColor):

        tw1 = curses.initscr()
        WX = (center_x - (wWidth)//2)
        WY = (center_y+Ypos)
        tw1 = curses.newwin(wHeight, wWidth, WY, WX)
        tw1.attron(curses.color_pair(labelColor))
        tw1.addstr(1,1,outstring1)
        tw1.attroff(curses.color_pair(labelColor))
        tw1.addstr(1,11,outstring2)
        tw1.addstr(2,11,outstring3)
        if k == ord(btn):
            colA = 5
            colB = 6
            Status = statusNext
        else:
            colA = 6
            colB = 6
            Status = statusPres
        tw1.attron(curses.color_pair(colA))
        tw1.addstr(4,20,btnText)
        tw1.attroff(curses.color_pair(colA))
        tw1.attron(curses.color_pair(colB))
        tw1.addstr(4,40,"'F12' -  QUIT  ")
        tw1.attroff(curses.color_pair(colB))
        tw1.border()
        tw1.refresh()
        time.sleep(0.5)
        return Status
                
    def renderWindow():
        ################################################################
        ## WINDOW ######################################################
        ################################################################
        
        # The window stuff (inserting preliminary set "stringaz")
        
        if showWindow == True and height >= 22 and width >= 79:
            #center_y = int(height//2)
            #center_x = int(width //2)
            
            if height < 24:
                wHeight = height - 8
                begin_y = 4
            else:
                wHeight = 16
                begin_y = center_y - wHeight//2
                    
            if width <= 80:
                wWidth = width - 8
                begin_x = 4
            else:
                wWidth = 70
                begin_x = center_x - wWidth//2
            
            if height == 24 and width == 80:
                begin_x = 1; begin_y = 4
                wHeight = height - 7; wWidth = width - 2
        
            winn = curses.initscr()        
            winn = curses.newwin(wHeight, wWidth, begin_y, begin_x)
            
            if F_Done[MenuState][1] == False:
                cpair_1 = 6
            else:
                cpair_1 = 8
            winn.attron(curses.color_pair(cpair_1))
            winn.attron(curses.A_BOLD)
            winn.addstr(4,2,N_text1)
            winn.attroff(curses.A_BOLD)
            winn.attroff(curses.color_pair(cpair_1))
            
            if F_Done[MenuState][2] == False:
                cpair_2 = 6
            else:
                cpair_2 = 8            
            winn.attron(curses.color_pair(cpair_2))
            winn.attron(curses.A_BOLD)
            winn.addstr(6,2,N_text2)
            winn.attroff(curses.A_BOLD)
            winn.attroff(curses.color_pair(cpair_2))
            
            if F_Done[MenuState][3] == False:
                cpair_3 = 6
            else:
                cpair_3 = 8            
            winn.attron(curses.color_pair(cpair_3))
            winn.attron(curses.A_BOLD)
            winn.addstr(8,2,N_text3)
            winn.attroff(curses.A_BOLD)
            winn.attroff(curses.color_pair(cpair_3))
            
            if F_Done[MenuState][4] == False:
                cpair_4 = 6
            else:
                cpair_4 = 8
            winn.attron(curses.color_pair(cpair_4))
            winn.attron(curses.A_BOLD)
            winn.addstr(10,2,N_text4)
            winn.attroff(curses.A_BOLD)
            winn.attroff(curses.color_pair(cpair_4))
            
            if F_Done[MenuState][5] == False:
                cpair_5 = 6
            else:
                cpair_5 = 8
            winn.attron(curses.color_pair(cpair_5))
            winn.attron(curses.A_BOLD)
            winn.addstr(12,2,N_text5)
            winn.attroff(curses.A_BOLD)
            winn.attroff(curses.color_pair(cpair_5))
            
            #this section shows strings from .config after buttons with digits
            winn.addstr(4,7,Ftext_1_1)
            winn.addstr(6,7,Ftext_2_1)
            winn.addstr(8,7,Ftext_3_1)
            winn.addstr(10,7,Ftext_4_1)
            winn.addstr(12,7,Ftext_5_1)
            
            winn.border()
        
            winn.refresh()
        
            # label window
            ginn = curses.initscr()        
            ginn = curses.newwin(3, 18, begin_y, begin_x)
            ginn.attron(curses.color_pair(5))
            ginn.addstr(1,1,Ftitle)
            ginn.attroff(curses.color_pair(5))
            ginn.border()
            ginn.refresh()
        
            # terminal error windows
            
            tw1 = curses.initscr()
            tw1 = curses.newwin(4, wWidth-2, height-8, begin_x+1)
            tw1.attron(curses.color_pair(3))
            tw1.addstr(1,1," OUTPUT: ")
            tw1.attroff(curses.color_pair(3))
            tw1.addstr(1,11,"err")
            tw1.border()
            tw1.refresh()
         
        F_Done[5][3] = False
        F_Done[7][1] = False
    
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
    Status = 0
    firstPurge = True
    
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
        ## DEFINITION OF F-KEYS ########################################
        ################################################################
        
        if k == curses.KEY_F1:
            MenuState = 1
        if k == curses.KEY_F2:
            MenuState = 2
        if k == curses.KEY_F3:
            MenuState = 3
        if k == curses.KEY_F4:
            MenuState = 4
        if k == curses.KEY_F5:
            MenuState = 5
        if k == curses.KEY_F6:
            MenuState = 6
        if k == curses.KEY_F7:
            MenuState = 7
        if k == curses.KEY_F8:
            MenuState = 8
        if k == curses.KEY_F9:
            MenuState = 9
        if k == curses.KEY_F10:
            MenuState = 10
        if k == curses.KEY_F11:
            MenuState = 11
        if k == curses.KEY_F12:
            MenuState = 12
            
        ## END OF DEFINITION OF F-KEYS #################################
        
                
        ################################################################
        ##   MENUSTATE != 0 ############################################
        ################################################################
        
        if MenuState != 0:
            
            MS = MenuState
            stringaz = Fconf[MS][0]
            Ftitle = " "+Fconf[MS][0]+"         "
            showWindow = True

            Ftext_1_1 = Fconf[MS][1]
            Ftext_2_1 = Fconf[MS][3]
            Ftext_3_1 = Fconf[MS][5]
            Ftext_4_1 = Fconf[MS][7]
            Ftext_5_1 = Fconf[MS][9]            
            
            if k == ord('1') or k == ord('2') or k == ord('3') or k == ord('4') or k == ord('5'):
                if k == ord('1'):
                    key = 2
                    grn = 1
                if k == ord('2'):
                    key = 4
                    grn = 2
                if k == ord('3'):
                    key = 6
                    grn = 3
                if k == ord('4'):
                    key = 8
                    grn = 4
                if k == ord('5'):
                    key = 10
                    grn = 5
                    
                #Terminal = Fconf[13]
                #command = Terminal + ' -- ' + Fconf[MS][key]
                command = Fconf[MS][key]
                p = subprocess.Popen(command, shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)
                F_Done[MS][grn] = True
                
        ## END OF MENUSTATE != 0  ######################################
        
              
        ################################################################
        # MENUSTATE = 0 ################################################
        ################################################################
        
        # Render Status Bar
        renderStatusBar()
        
        
        if MenuState == 0:
            
            showWindow = False
            
        # Status 0. Logo
        if Status == 0:
            tilist = getPic.loadImage2("./image/00_pilottui-logo.ti")
            renderTopper()
            renderImage()
            renderSubtitle()
            renderStatusBar()
            if firsttime == False:
                Status = windowStart()
                
        # Status 1. Check
        if Status == 1:
            tilist = getPic.loadImage2("./image/00_pilottui-logo.ti")
            renderTopper()
            renderImage()
            renderSubtitle()
            renderStatusBar()
            Status = renderWindowOverLogo()
                
        # Status 2. Distrakt. Pilot-Server was set without Pilot-TUI
        if Status == 2:
            tilist = getPic.loadImage2("./image/04_Distrakt.ti")
            renderTopper()
            renderImage()
            renderStatusBar()
            #renderWindowUpperCommon(outstring1, outstring2, outstring3, wWidth, wHeight,Ypos,btn,btnText)
            outstring1 = " WARNING! "
            outstring2 = "  Pilot-Server was installed without Pilot-TUI usage."
            outstring3 = "  It should be purged and reinstalled. "
            wWidth = 66
            wHeight = 6
            Ypos = -11
            btn = 'p'
            btnText = "'P' -  PURGE  "
            statusNext = 3
            statusPres = 2
            labelColor = 5
            Status = renderWindowUpperCommon(outstring1, outstring2, outstring3, wWidth, wHeight,Ypos,btn,btnText,statusNext,statusPres,labelColor)
            
        # Status 3. Purging.
        if Status == 3:
            tilist = getPic.loadImage2("./image/03_Purging.ti")
            renderTopper()
            renderImage()
            renderStatusBar()
            if firstPurge == True:
                purge.stopPilotServer()
                smallWindow("Services are stopped.",0)
                purge.disablePilotServices()
                smallWindow("Services are disabled.",3)
                purge.removePilotDirectory()
                smallWindow("Directory is removed.",6)
                firstPurge = False
            outstring1 = "  Well,  "
            outstring2 = "  Pilot-Server has been stopped, disabled & purged."
            outstring3 = "  Press 'N' to move to next step. "
            wWidth = 66
            wHeight = 6
            Ypos = -11
            btn = 'n'
            btnText = "'N' -  NEXT  "
            statusNext = 4
            statusPres = 3
            labelColor = 3
            Status = renderWindowUpperCommon(outstring1, outstring2, outstring3, wWidth, wHeight,Ypos,btn,btnText,statusNext,statusPres,labelColor)
            
        # Status 4. All's clear.
        if Status == 4:
            tilist = getPic.loadImage2("./image/05_AllsClear.ti")
            renderTopper()
            renderImage()
            renderStatusBar()
            outstring1 = "  Clear,  "
            outstring2 = "  Pilot-Server has been stopped, disabled & purged."
            outstring3 = "  Press 'S' to start installation. "
            wWidth = 66
            wHeight = 6
            Ypos = -11
            btn = 's'
            btnText = "'S' -  Start  "
            statusNext = 5
            statusPres = 4
            labelColor = 3
            Status = renderWindowUpperCommon(outstring1, outstring2, outstring3, wWidth, wHeight,Ypos,btn,btnText,statusNext,statusPres,labelColor)
            
        # Status 5. Downloading.
        if Status == 5:
            tilist = getPic.loadImage2("./image/01_Downloading.ti")
            renderTopper()
            renderImage()
            renderStatusBar()
            outstring1 = " LOADING "
            outstring2 = "  Let's download and install Pilot-Server."
            outstring3 = "  Press 'L' to start loading process. "
            wWidth = 66
            wHeight = 6
            Ypos = -11
            btn = 'l'
            btnText = "'L' - Load  "
            statusNext = 6
            statusPres = 5
            labelColor = 3
            Status = renderWindowUpperCommon(outstring1, outstring2, outstring3, wWidth, wHeight,Ypos,btn,btnText,statusNext,statusPres,labelColor)

        # Status 6. Unpacking.
        if Status == 6:
            tilist = getPic.loadImage2("./image/02_Unpacking.ti")
            renderTopper()
            renderImage()
            renderStatusBar()
            outstring1 = " UNZIP "
            outstring2 = "  Pilot-Server archive was downloaded"
            outstring3 = "  Press 'U' to unzip package. "
            wWidth = 66
            wHeight = 6
            Ypos = -11
            btn = 'u'
            btnText = "'U' - Unzip  "
            statusNext = 7
            statusPres = 6
            labelColor = 3
            Status = renderWindowUpperCommon(outstring1, outstring2, outstring3, wWidth, wHeight,Ypos,btn,btnText,statusNext,statusPres,labelColor)
        
        # Status 7. Construction.
        if Status == 7:
            tilist = getPic.loadImage2("./image/06_Construction.ti")
            renderTopper()
            renderImage()
            renderStatusBar()
            outstring1 = " SET UP "
            outstring2 = "  Pilot-Server archive was downloaded"
            outstring3 = "  Press 'U' to unzip package. "
            wWidth = 66
            wHeight = 6
            Ypos = -12
            btn = 's'
            btnText = "'S' - Unzip  "
            statusNext = 8
            statusPres = 7
            labelColor = 3
            Status = renderWindowUpperCommon(outstring1, outstring2, outstring3, wWidth, wHeight,Ypos,btn,btnText,statusNext,statusPres,labelColor)
        
        # Status 8. Test Launch.
        if Status == 8:
            tilist = getPic.loadImage2("./image/07_Launch.ti")
            renderTopper()
            renderImage()
            renderStatusBar()
            outstring1 = " TEST "
            outstring2 = "  Pilot-Server archive was downloaded"
            outstring3 = "  Press 'U' to unzip package. "
            wWidth = 66
            wHeight = 6
            Ypos = -12
            btn = 'l'
            btnText = "'L' - Launch  "
            statusNext = 9
            statusPres = 8
            labelColor = 3
            Status = renderWindowUpperCommon(outstring1, outstring2, outstring3, wWidth, wHeight,Ypos,btn,btnText,statusNext,statusPres,labelColor)
        
        # Status 9. System.
        if Status == 9:
            tilist = getPic.loadImage2("./image/08_System.ti")
            renderTopper()
            renderImage()
            renderStatusBar()
            outstring1 = " SYSTEM "
            outstring2 = "  Pilot-Server archive was downloaded"
            outstring3 = "  Press 's' to unzip package. "
            wWidth = 66
            wHeight = 6
            Ypos = -12
            btn = 's'
            btnText = "'S' - Unzip  "
            statusNext = 10
            statusPres = 9
            labelColor = 3
            Status = renderWindowUpperCommon(outstring1, outstring2, outstring3, wWidth, wHeight,Ypos,btn,btnText,statusNext,statusPres,labelColor)
        
        
        # Status 10. System.
        if Status == 10:
            tilist = getPic.loadImage2("./image/09_Complete.ti")
            renderTopper()
            renderImage()
            renderStatusBar()
            outstring1 = " SYSTEM "
            outstring2 = "  Pilot-Server archive was downloaded"
            outstring3 = "  Press 'C' to unzip package. "
            wWidth = 66
            wHeight = 6
            Ypos = -12
            btn = 'c'
            btnText = "'C' - Unzip  "
            statusNext = 11
            statusPres = 10
            labelColor = 3
            Status = renderWindowUpperCommon(outstring1, outstring2, outstring3, wWidth, wHeight,Ypos,btn,btnText,statusNext,statusPres,labelColor)
        
        # Status 11. Connect.
        if Status == 11:
            tilist = getPic.loadImage2("./image/10_Connect.ti")
            renderTopper()
            renderImage()
            renderStatusBar()
            outstring1 = " SYSTEM "
            outstring2 = "  Pilot-Server archive was downloaded"
            outstring3 = "  Press 'O' to unzip package. "
            wWidth = 66
            wHeight = 6
            Ypos = -12
            btn = 'o'
            btnText = "'O' - Unzip  "
            statusNext = 12
            statusPres = 11
            labelColor = 3
            Status = renderWindowUpperCommon(outstring1, outstring2, outstring3, wWidth, wHeight,Ypos,btn,btnText,statusNext,statusPres,labelColor)
        
        # Status 12. UPDATE.
        if Status == 12:
            tilist = getPic.loadImage2("./image/11_Update.ti")
            renderTopper()
            renderImage()
            renderStatusBar()
            outstring1 = " SYSTEM "
            outstring2 = "  Pilot-Server archive was downloaded"
            outstring3 = "  Press 'U' to unzip package. "
            wWidth = 66
            wHeight = 6
            Ypos = -12
            btn = 'u'
            btnText = "'U' - Unzip  "
            statusNext = 1
            statusPres = 12
            labelColor = 3
            Status = renderWindowUpperCommon(outstring1, outstring2, outstring3, wWidth, wHeight,Ypos,btn,btnText,statusNext,statusPres,labelColor)
        
        
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
