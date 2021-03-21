# init color module
def initPairs():
    import curses
    curses.initscr()

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

    # colors for logo.
    curses.init_pair(20, curses.COLOR_BLACK, curses.COLOR_WHITE)
    curses.init_pair(21, curses.COLOR_RED, curses.COLOR_WHITE)
    curses.init_pair(22, curses.COLOR_GREEN, curses.COLOR_WHITE)
    curses.init_pair(23, curses.COLOR_YELLOW, curses.COLOR_WHITE)
    curses.init_pair(24, curses.COLOR_BLUE, curses.COLOR_WHITE)
    curses.init_pair(25, curses.COLOR_MAGENTA, curses.COLOR_WHITE)
    curses.init_pair(26, curses.COLOR_CYAN, curses.COLOR_WHITE)
    curses.init_pair(27, curses.COLOR_WHITE, curses.COLOR_BLACK)
    curses.init_pair(28, curses.COLOR_BLACK, curses.COLOR_WHITE)
    curses.init_pair(29, curses.COLOR_RED, curses.COLOR_WHITE)
    curses.init_pair(30, curses.COLOR_GREEN, curses.COLOR_WHITE)
    curses.init_pair(31, curses.COLOR_YELLOW, curses.COLOR_WHITE)
    curses.init_pair(32, curses.COLOR_BLUE, curses.COLOR_WHITE)
    curses.init_pair(33, curses.COLOR_MAGENTA, curses.COLOR_WHITE)
    curses.init_pair(34, curses.COLOR_CYAN, curses.COLOR_WHITE)
    curses.init_pair(35, curses.COLOR_WHITE, curses.COLOR_BLACK)