import curses

PANEL_HEIGHT = 10

def draw_separator(stdscr,height,width):
    separator_y = height - PANEL_HEIGHT - 1
    stdscr.addstr(separator_y, 0, '-' * width)


def show_title_screen(stdscr,height,width):
    contents=["Map maker", "version 1.0", "", "Naciśnij dowolny klawisz aby kontynuować"]
    y=(height-len(contents))//2
    for i in range(len(contents)):
        x=(width-len(contents[i]))//2
        stdscr.addstr(y+i, x, contents[i])

    stdscr.getch()

def main(stdscr):
    curses.curs_set(0)
    curses.mousemask(curses.ALL_MOUSE_EVENTS | curses.REPORT_MOUSE_POSITION)

    height, width = stdscr.getmaxyx()
    stdscr.clear()
    show_title_screen(stdscr,height,width)
    stdscr.clear()
    draw_separator(stdscr, height, width)
    stdscr.refresh()
    stdscr.getch()


if __name__ == '__main__':
    curses.wrapper(main)