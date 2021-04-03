# selectServerVersion.py

def window(center_x, center_y, selServ):
    # Help screen
    import curses
    tw1 = curses.initscr()
    wdh = 72
    hgt = 16
    WX = (center_x - wdh // 2)
    WY = (center_y - hgt // 2)
    CP = 9
    SP = 1
    DP = 5
    tw1 = curses.newwin(hgt, wdh, WY, WX)
    tw1.attron(curses.color_pair(CP))
    tw1.addstr(3, 3, "Please select version of Pilot-Server for Slot #"+str(selServ))
    tw1.addstr(5, 3, "Press the keys:")
    tw1.addstr(6, 3, "     - for current Release;")
    tw1.addstr(7, 3, "     - for latest Beta;")
    tw1.addstr(8, 3, "     - for freshest Alpha;")
    tw1.addstr(9, 3, "     - input your own url (not safe mode);")
    #tw1.addstr(10, 3, "    - Pilot-Server service start, stop & check abilities.")
    tw1.attroff(curses.color_pair(CP))
    tw1.attron(curses.color_pair(SP))
    tw1.addstr(12, 3, "Select option & installation will begin soon.")
    tw1.attroff(curses.color_pair(SP))
    tw1.attron(curses.color_pair(DP))
    tw1.addstr(6, 3, " 1 ")
    tw1.addstr(7, 3, " 2 ")
    tw1.addstr(8, 3, " 3 ")
    tw1.addstr(9, 3, " 4 ")
    tw1.attroff(curses.color_pair(DP))
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
    tw2.addstr(1, 1, "SELECT VERSION")
    tw2.attroff(curses.color_pair(CP))
    tw2.border()
    tw2.refresh()