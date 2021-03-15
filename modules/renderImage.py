# module renderImage

def renderImage(stdscr, height, width, tilist, center_x, center_y, B):
# Rendering logo
# from the terminal image strings
    import curses
    PixelMatrix = []
    PixelString = []
    PixelColors = ['0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F']
    if height >= 23 and width >= 80:
        for j in range(3,22):
            PixelString = tilist[j]
            for i in range(3,82):
                Pixel = tilist[j][i]
                #print('got it')
                #print(Pixel)
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
