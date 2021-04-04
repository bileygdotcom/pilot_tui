#renderWindow module

def windowStart(center_x, center_y, k):
    # WINDOW over Logo
    import curses
    import time
    tw1 = curses.initscr()
    # winn = curses.newwin(wHeight, wWidth, begin_y, begin_x)
    WX = (center_x - (34) // 2 + 9)
    WY = (center_y + 3)
    CP = 1
    tw1 = curses.newwin(4, 34, WY, WX)
    tw1.attron(curses.color_pair(CP))
    tw1.addstr(1, 3, "Pilot TUI has been launched")
    tw1.attroff(curses.color_pair(CP))
    if k == ord('s'):
        colA = 5
        #Status = 1
    else:
        colA = 6
        #Status = 0
    tw1.attron(curses.color_pair(CP))
    tw1.addstr(2, 6, "PRESS")
    tw1.attroff(curses.color_pair(CP))
    tw1.attron(curses.color_pair(colA))
    tw1.addstr(2, 13, " 'S' ")
    tw1.attroff(curses.color_pair(colA))
    tw1.attron(curses.color_pair(CP))
    tw1.addstr(2, 19, "TO START")
    tw1.attroff(curses.color_pair(CP))
    tw1.border()
    tw1.refresh()
    time.sleep(0.5)
    #return Status


def smallWindow(center_x, center_y, funcText, moveY):
    import curses
    import time
    tw1 = curses.initscr()
    WX = (center_x - 39)
    WY = (center_y - 1 + moveY)
    CP = 1
    tw1 = curses.newwin(3, 27, WY, WX)
    tw1.attron(curses.color_pair(CP))
    tw1.addstr(1, 2, funcText)
    tw1.attroff(curses.color_pair(CP))
    tw1.border()
    tw1.refresh()
    time.sleep(0.5)


def inputWindow(center_x, center_y, promtText, moveY):
    import curses
    import time
    curses.echo()
    tw1 = curses.initscr()
    WX = (center_x - 39)
    WY = (center_y - 1 + moveY)
    CP = 1
    tw1 = curses.newwin(3, 73, WY, WX)
    tw1.attron(curses.color_pair(CP))
    tw1.addstr(1, 1, promtText)
    tw1.attroff(curses.color_pair(CP))
    tw1.border()
    input = tw1.getstr(1, 11, 80)
    inputUrlTail = str(input)[2:-1]
    tw1.refresh()
    curses.noecho()
    time.sleep(0.5)
    return inputUrlTail


def renderWindowUpperCommon(k, center_x, center_y, outstring1, outstring2, outstring3, wWidth, wHeight, Ypos, btn, btnText, statusNext,
                            statusPres, labelColor):
    import curses
    import time
    tw1 = curses.initscr()
    WX = (center_x - (wWidth) // 2)
    WY = (center_y + Ypos)
    tw1 = curses.newwin(wHeight, wWidth, WY, WX)
    tw1.attron(curses.color_pair(labelColor))
    tw1.addstr(1, 1, outstring1)
    tw1.attroff(curses.color_pair(labelColor))
    tw1.addstr(1, 13, outstring2)
    tw1.addstr(2, 13, outstring3)
    if k == ord(btn):
        colA = 5
        colB = 6
        #Status = statusNext
        Funkie = True
    else:
        colA = 6
        colB = 6
        #Status = statusPres
        Funkie = False
    tw1.attron(curses.color_pair(colA))
    tw1.addstr(4, 20, btnText)
    tw1.attroff(curses.color_pair(colA))
    tw1.attron(curses.color_pair(colB))
    tw1.addstr(4, 40, "'F12' -  QUIT  ")
    tw1.attroff(curses.color_pair(colB))
    tw1.border()
    tw1.refresh()
    time.sleep(0.5)
    #return Status