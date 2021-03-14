# module bar

def renderSubtitle():
    # Rendering subtitle
    stdscr.attron(curses.color_pair(1))
    stdscr.attron(curses.A_BOLD)
    stdscr.addstr(start_y + 3, start_x_title + 15, title)
    stdscr.attroff(curses.color_pair(2))
    stdscr.attroff(curses.A_BOLD)


def renderTopper():
    # Topper showing the coordinates
    # whstr = "W-H: [{},{}]".format(width, height)
    # topperstr1 = whstr
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


def renderStatusBar():
    # Render 2 nether Status Bars
    sbpair1 = 9
    sbpair2 = 3

    # normalization of names for menu
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

    if height >= 23 and width >= 79:

        if Status < 12:
            statusbarstr2 = " "
            statusbarstr1 = " "
        else:
            # statusbar menu set
            # statusbarstr2 = " "+FCN[0]+" | "+FCN[1]+" | "+FCN[2]+" | "+FCN[3]+" | "+FCN[4]+" | "+FCN[5]+" |"
            # statusbarstr1 = " "+FCN[6]+" | "+FCN[7]+" | "+FCN[8]+" | "+FCN[9]+" | "+FCN[10]+" | "+FCN[11]+" |"
            statusbarstr2 = " F1 - help  | F2 - servr | F3 -       | F4 -       | F5 - bases | F6 - upgrd "
            statusbarstr1 = " F7 - admin | F8 - purge | F9 - instl | F10 - alt  | F11 - fscr | F12 - EXIT "

    else:
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