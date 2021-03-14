def screenHelp(center_x, center_y):
    # Help screen
    import curses
    tw1 = curses.initscr()
    wdh = 72
    hgt = 16
    WX = (center_x - wdh // 2)
    WY = (center_y - hgt // 2)
    CP = 9
    SP = 1
    tw1 = curses.newwin(hgt, wdh, WY, WX)
    tw1.attron(curses.color_pair(CP))
    tw1.addstr(3, 3, "Pilot TUI - Terminal User Interface for Pilot-Sever on Linux.")
    tw1.addstr(5, 3, "Pilot TUI provides:")
    tw1.addstr(6, 3, "    - fast and errorproof installation;")
    tw1.addstr(7, 3, "    - automatic uninstallation & purging the traces;")
    tw1.addstr(8, 3, "    - database downloading, connection & control;")
    tw1.addstr(9, 3, "    - server to service convertation;")
    tw1.addstr(10, 3, "    - Pilot-Server service start, stop & check abilities.")
    tw1.attroff(curses.color_pair(CP))
    tw1.attron(curses.color_pair(SP))
    tw1.addstr(12, 3, "Pilot TUI is developed by bileyg, http://bileyg.com")
    tw1.attroff(curses.color_pair(SP))
    tw1.border()
    tw1.refresh()
    # time.sleep(0.5)
    # Label
    tw2 = curses.initscr()
    wdh = 16
    hgt = 3
    WX = (center_x - (wdh) // 2)
    WY = WY - 1
    CP = 5
    tw2 = curses.newwin(hgt, wdh, WY, WX)
    tw2.attron(curses.color_pair(CP))
    tw2.addstr(1, 1, "     HELP     ")
    tw2.attroff(curses.color_pair(CP))
    tw2.border()
    tw2.refresh()