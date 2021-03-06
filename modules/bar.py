# module bar

def renderSubtitle(stdscr, start_y, start_x_title, title):
    # Rendering subtitle
    import curses
    stdscr.attron(curses.color_pair(1))
    stdscr.attron(curses.A_BOLD)
    stdscr.addstr(start_y + 3, start_x_title + 15, title)
    stdscr.attroff(curses.color_pair(2))
    stdscr.attroff(curses.A_BOLD)


def renderTopper(stdscr, width):
    # Topper showing the coordinates
    # whstr = "W-H: [{},{}]".format(width, height)
    # topperstr1 = whstr
    import curses
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


# def pressAnyKey():


def renderStatusBar(stdscr, Status, height, width, statusbarstr1, statusbarstr2):
    # Render 2 nether Status Bars
    import curses
    sbpair1 = 9
    sbpair2 = 3

    ## normalization of names for menu when get'em from conf
    # Fconf0names = []
    # for i in range(1,13):
    # Fconf0 = Fconf[i][0]
    # scl = len(Fconf0)
    # if scl > 10:
    # sss = (Fconf0[0:10])
    # elif scl == 10:
    # sss = Fconf0
    # else:
    # ascl = 10 - scl
    # sss = Fconf0[0:10] + ' '*ascl
    # Fconf0names.append(sss)
    # FCN = Fconf0names

    if height <= 23 and width <= 79:
        statusbarstr2 = "Window size should be minimum 79x23 "
        statusbarstr1 = " "

    # Render status bar
    stdscr.attron(curses.color_pair(sbpair1))
    stdscr.addstr(height - 1, 0, statusbarstr1)
    stdscr.addstr(height - 1, len(statusbarstr1), " " * (width - len(statusbarstr1) - 1))
    stdscr.attroff(curses.color_pair(sbpair1))

    # Render top status bar
    stdscr.attron(curses.color_pair(sbpair2))
    stdscr.addstr(height - 2, 0, statusbarstr2)
    stdscr.addstr(height - 2, len(statusbarstr2), " " * (width - len(statusbarstr2) - 1))
    stdscr.attroff(curses.color_pair(sbpair2))