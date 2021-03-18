def serverState():
    # Help screen

    def srvNum(y, col, num):
        if servSelect1 == True:
            tw1.addstr(5, 4, " >>> ")
        else:
            tw1.addstr(5, 4, "    ")
        if servSelect2 == True:
            tw1.addstr(7, 4, " >>> ")
        else:
            tw1.addstr(7, 4, "    ")
        if servSelect3 == True:
            tw1.addstr(9, 4, " >>> ")
        else:
            tw1.addstr(9, 4, "    ")
        if servSelect4 == True:
            tw1.addstr(11, 4, " >>> ")
        else:
            tw1.addstr(11, 4, "    ")

        tw1.attron(curses.color_pair(col))
        tw1.addstr(y, 4 + 6, "  " + str(num) + "  ")
        tw1.attroff(curses.color_pair(col))
        tw1.addstr(y, 13 + 6, "O ")
        tw1.addstr(y, 21 + 6, "  I")
        tw1.addstr(y, 28 + 6, "O ")
        tw1.addstr(y, 36 + 6, "  I")
        tw1.addstr(y, 43 + 6, "out")

    def srvSwitcher(y, px):
        tw1.attron(curses.color_pair(21))
        tw1.attron(curses.A_BOLD)
        tw1.addstr(y, butx + px, B + B + B)
        tw1.attroff(curses.A_BOLD)
        tw1.addstr(y, butx + 3 + px, B)
        tw1.attroff(curses.color_pair(21))
        tw1.attron(curses.color_pair(7))
        tw1.attron(curses.A_BOLD)
        tw1.addstr(y, blcx + px, B + B + B)
        tw1.attroff(curses.A_BOLD)
        tw1.attroff(curses.color_pair(7))

    # outpt = testServer.url()
    # out = str(outpt)[1:]
    tw1 = curses.initscr()
    wdh = 72
    hgt = 16
    WX = (center_x - (wdh) // 2)
    WY = (center_y - hgt // 2)
    CP = 21
    SP = 1
    tw1 = curses.newwin(hgt, wdh, WY, WX)

    if serverON == False:
        butx = 15 + 6
        blcx = 19 + 6
    else:
        butx = 18 + 6
        blcx = 15 + 6

    tw1.attron(curses.color_pair(3))
    tw1.attron(curses.A_BOLD)
    tw1.addstr(3, 4, " Sel  Serv#      Launched      Autostart     Version            ")
    tw1.attroff(curses.color_pair(3))
    tw1.attroff(curses.A_BOLD)

    srvNum(5, 6, 1)
    srvSwitcher(5, 0)
    srvSwitcher(5, 15)
    srvNum(7, 6, 2)
    srvSwitcher(7, 0)
    srvSwitcher(7, 15)
    srvNum(9, 6, 3)
    srvSwitcher(9, 0)
    srvSwitcher(9, 15)
    srvNum(11, 6, 4)
    srvSwitcher(11, 0)
    srvSwitcher(11, 15)

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
    tw2.addstr(1, 1, "    STATUS    ")
    tw2.attroff(curses.color_pair(CP))
    tw2.border()
    tw2.refresh()