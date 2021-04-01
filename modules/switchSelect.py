#switch select module
#(center_x, center_y,
def srvNum(y, col, num, serverSlots, tw1):
    import curses

    # server slot selector - draw arrows
    for sse in range(1,5):
        if serverSlots[sse][0] == True:
            tw1.addstr(sse*2+3, 4, " >>> ")
        else:
            tw1.addstr(sse*2+3, 4, "     ")

    # color on slot with installed server
    if serverSlots[num][1] == True:
        col = 8
    tw1.attron(curses.color_pair(col))
    tw1.addstr(y, 4 + 6, "  " + str(num) + "  ")
    tw1.attroff(curses.color_pair(col))
    # draw O, I, out
    tw1.addstr(y, 13 + 6, "O ")
    tw1.addstr(y, 21 + 6, "  I")
    tw1.addstr(y, 28 + 6, "O ")
    tw1.addstr(y, 36 + 6, "  I")
    tw1.addstr(y, 43 + 6, "out")

def srvSwitcher(y, ssz, B, tw1, ssw, serverSlots):
    import curses

    if ssz == 2:
        px = 0
    else:
        px = 15

    if serverSlots[ssw][ssz] == False:
        butx = 15 + 6
        blcx = 19 + 6
    else:
        butx = 18 + 6
        blcx = 15 + 6

    # red button
    tw1.attron(curses.color_pair(21))
    tw1.attron(curses.A_BOLD)
    tw1.addstr(y, butx + px, B + B + B)
    tw1.attroff(curses.A_BOLD)
    tw1.addstr(y, butx + 3 + px, B)
    tw1.attroff(curses.color_pair(21))
    # blac space
    tw1.attron(curses.color_pair(7))
    tw1.attron(curses.A_BOLD)
    tw1.addstr(y, blcx + px, B + B + B)
    tw1.attroff(curses.A_BOLD)
    tw1.attroff(curses.color_pair(7))

def serverSelect(center_x, center_y, serverSlots, B, serverON):
    import curses
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

    # draw table header
    tw1.attron(curses.color_pair(3))
    tw1.attron(curses.A_BOLD)
    tw1.addstr(3, 4, " Sel  Serv#      Launched      Autostart     Version            ")
    tw1.attroff(curses.color_pair(3))
    tw1.attroff(curses.A_BOLD)

    # draw switchers
    for ssw in range(1, 5):
        ys = ssw * 2 + 3
        srvNum(ys, 6, ssw, serverSlots, tw1)
        srvSwitcher(ys, 2, B, tw1, ssw, serverSlots)
        srvSwitcher(ys, 3, B, tw1, ssw, serverSlots)

    # draw window
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
    tw2.addstr(1, 1, " SERVER SLOTS ")
    tw2.attroff(curses.color_pair(CP))
    tw2.border()
    tw2.refresh()