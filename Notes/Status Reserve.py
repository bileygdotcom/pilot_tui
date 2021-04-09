# Status 1. Check
if Status == 100:
    tilist = getPic.loadImage2("./image/00_pilottui-logo.ti")
    bar.renderTopper(stdscr, width)
    # funkList["Image"]
    funkList["Topper"]
    funkList["Image"]
    funkList["Subtitle"]
    funkList["Statusbar"]
    # renderImage.renderImage(stdscr, height, width, tilist, center_x, center_y, B)
    # bar.renderSubtitle(stdscr, start_y, start_x_title, title)
    # bar.renderStatusBar(stdscr, Status, height, width)
    # Status = renderWindowOverLogo()
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
    Status = renderWindow.renderWindowUpperCommon(k, center_x, center_y, outstring1, outstring2, outstring3, wWidth,
                                                  wHeight, Ypos, btn, btnText, statusNext, statusPres, labelColor)

# Status 2. Distrakt. Pilot-Server was set without Pilot-TUI
if Status == 2:
    tilist = getPic.loadImage2("./image/04_Distrakt.ti")
    bar.renderTopper(stdscr, width)
    renderImage.renderImage(stdscr, height, width, tilist, center_x, center_y, B)
    bar.renderStatusBar(stdscr, Status, height, width)
    # renderWindow.renderWindowUpperCommon(k, center_x, center_y, outstring1, outstring2, outstring3, wWidth, wHeight,Ypos,btn,btnText)
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
    Status = renderWindow.renderWindowUpperCommon(k, center_x, center_y, outstring1, outstring2, outstring3, wWidth,
                                                  wHeight, Ypos, btn, btnText, statusNext, statusPres, labelColor)

# Status 3. Purging.
if Status == 3:
    tilist = getPic.loadImage2("./image/03_Purging.ti")
    bar.renderTopper(stdscr, width)
    renderImage.renderImage(stdscr, height, width, tilist, center_x, center_y, B)
    bar.renderStatusBar(stdscr, Status, height, width)
    if firstPurge == True:
        purge.stopPilotServer()
        renderWindow.smallWindow(center_x, center_y, "Services are stopped.", 0)
        purge.disablePilotServices()
        renderWindow.smallWindow(center_x, center_y, "Services are disabled.", 3)
        purge.removePilotDirectory()
        renderWindow.smallWindow(center_x, center_y, "Directory is removed.", 6)
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
    Status = renderWindow.renderWindowUpperCommon(k, center_x, center_y, outstring1, outstring2, outstring3, wWidth,
                                                  wHeight, Ypos, btn, btnText, statusNext, statusPres, labelColor)

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
    Status = renderWindow.renderWindowUpperCommon(k, center_x, center_y, outstring1, outstring2, outstring3, wWidth,
                                                  wHeight, Ypos, btn, btnText, statusNext, statusPres, labelColor)

# Status 5. Downloading.
if Status == 5:
    tilist = getPic.loadImage2("./image/01_Downloading.ti")
    bar.renderTopper(stdscr, width)
    renderImage.renderImage(stdscr, height, width, tilist, center_x, center_y, B)
    bar.renderStatusBar(stdscr, Status, height, width)
    if firstLoad == True:
        loadIntoDirectory.makeFolder(softpath)
        renderWindow.smallWindow(center_x, center_y, "The folder was created.", 0)
        renderWindow.smallWindow(center_x, center_y, "Downloading archive....", 3)
        loadIntoDirectory.download(softpath)
        renderWindow.smallWindow(center_x, center_y, "Archive was downloaded.", 3)
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
    Status = renderWindow.renderWindowUpperCommon(k, center_x, center_y, outstring1, outstring2, outstring3, wWidth,
                                                  wHeight, Ypos, btn, btnText, statusNext, statusPres, labelColor)

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
    Status = renderWindow.renderWindowUpperCommon(k, center_x, center_y, outstring1, outstring2, outstring3, wWidth,
                                                  wHeight, Ypos, btn, btnText, statusNext, statusPres, labelColor)

# Status 7. Construction.
if Status == 7:
    tilist = getPic.loadImage2("./image/06_Construction.ti")
    bar.renderTopper(stdscr, width)
    renderImage.renderImage(stdscr, height, width, tilist, center_x, center_y, B)
    bar.renderStatusBar(stdscr, Status, height, width)
    if firstAuth == True:
        login = renderWindow.inputWindow(center_x, center_y, "Enter login: ", 0)
        passw = renderWindow.inputWindow(center_x, center_y, "Enter passw: ", 3)
        setUp.rights(softpath, login, passw)
        renderWindow.smallWindow(center_x, center_y, "Pilot-Server is set.", 6)
        firstAuth = False
    # renderWindow.smallWindow(center_x, center_y, "Services are stopped.",0)
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
    Status = renderWindow.renderWindowUpperCommon(k, center_x, center_y, outstring1, outstring2, outstring3, wWidth,
                                                  wHeight, Ypos, btn, btnText, statusNext, statusPres, labelColor)

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
        # renderWindow.smallWindow(center_x, center_y, out,6)
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
    Status = renderWindow.renderWindowUpperCommon(k, center_x, center_y, outstring1, outstring2, outstring3, wWidth,
                                                  wHeight, Ypos, btn, btnText, statusNext, statusPres, labelColor)

# Status 9. Build a Complex.
if Status == 9:
    tilist = getPic.loadImage2("./image/08_System.ti")
    bar.renderTopper(stdscr, width)
    renderImage.renderImage(stdscr, height, width, tilist, center_x, center_y, B)
    bar.renderStatusBar(stdscr, Status, height, width)
    if firstBuild == True:
        buildComplex.adduser(softpath)
        renderWindow.smallWindow(center_x, center_y, "User 'pilotuser' was added.", 0)
        time.sleep(0.5)
        buildComplex.service(softpath)
        renderWindow.smallWindow(center_x, center_y, "Pilot-Server is Service now.", 3)
        time.sleep(0.5)
        buildComplex.service(softpath)
        renderWindow.smallWindow(center_x, center_y, "Automatization complete.", 6)
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
    Status = renderWindow.renderWindowUpperCommon(k, center_x, center_y, outstring1, outstring2, outstring3, wWidth,
                                                  wHeight, Ypos, btn, btnText, statusNext, statusPres, labelColor)

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
    Status = renderWindow.renderWindowUpperCommon(k, center_x, center_y, outstring1, outstring2, outstring3, wWidth,
                                                  wHeight, Ypos, btn, btnText, statusNext, statusPres, labelColor)

# Status 11. Connect.
if Status == 11:
    tilist = getPic.loadImage2("./image/10_Connect.ti")
    bar.renderTopper(stdscr, width)
    renderImage.renderImage(stdscr, height, width, tilist, center_x, center_y, B)
    bar.renderStatusBar(stdscr, Status, height, width)
    if firstConnect == True:
        # connectDemoBases.download(softpath)
        renderWindow.smallWindow(center_x, center_y, "Demobases were downloaded & unzipped", 0)
        time.sleep(1.0)
        # connectDemoBases.unzip(softpath)
        # renderWindow.smallWindow(center_x, center_y, "... & unzipped.",3)
        # time.sleep(0.5)
        connectDemoBases.attach(softpath)
        renderWindow.smallWindow(center_x, center_y, "Demobases were connected.", 6)
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
    Status = renderWindow.renderWindowUpperCommon(k, center_x, center_y, outstring1, outstring2, outstring3, wWidth,
                                                  wHeight, Ypos, btn, btnText, statusNext, statusPres, labelColor)

# Status 12. FRONT.
if Status == 12:
    installed = True
    tilist = getPic.loadImage2("./image/00_pilottui-logo.ti")
    bar.renderTopper(stdscr, width)
    funkList["Image"]
    # renderImage.renderImage(stdscr, height, width, tilist, center_x, center_y, B)
    # renderImage()
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
    Status = renderWindow.renderWindowUpperCommon(k, center_x, center_y, outstring1, outstring2, outstring3, wWidth,
                                                  wHeight, Ypos, btn, btnText, statusNext, statusPres, labelColor)

# Control SCREENS

# Screen 1. HELP
if ScreenN == 1:
    time.sleep(0.1)
    helpPage.screenHelp(center_x, center_y)

# Screen 2. SRVS
if ScreenN == 2:
    time.sleep(0.1)
    switchSelect.serverSelect(center_x, center_y, servSelect, B, serverON)