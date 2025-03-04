import curses

def show_title_screen(stdscr, rows, cols):
    contents = ["Map maker", "version 1.0", "", "Naciśnij dowolny klawisz aby kontynuować"]
    offset_y = (rows - len(contents)) // 2
    for i, line in enumerate(contents):
        y = offset_y + i
        x = (cols - len(line)) // 2
        stdscr.addstr(y, x, line)
    stdscr.refresh()

def main(stdscr):
    curses.curs_set(0)
    curses.mousemask(curses.ALL_MOUSE_EVENTS | curses.REPORT_MOUSE_POSITION)

    height, width = stdscr.getmaxyx()
    stdscr.clear()
    # stdscr.addstr(5, 10, f"* {height}x{width} *")
    show_title_screen(stdscr, height, width)
    # stdscr.refresh()
    stdscr.getch()


if __name__ == '__main__':
    curses.wrapper(main)