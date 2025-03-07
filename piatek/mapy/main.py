import curses

PANEL_HEIGHT = 10

def add_structure(structures, y, x,height):
    y_max = height - PANEL_HEIGHT - 1
    if y<y_max:
        structures.append((y,x))


def draw_map(stdscr, structures):
    for y, x in structures:
        stdscr.addstr(y, x, "*")


def draw_separator(stdscr,height,width):
    separator_y = height - PANEL_HEIGHT - 1
    stdscr.addstr(separator_y, 0, '-' * width)

def draw_scene(stdscr, structures, height, width):
    stdscr.clear()
    draw_separator(stdscr, height, width)
    draw_map(stdscr, structures)
    stdscr.refresh()

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
    structures = [(10, 5), (8,9), (15, 20)]
    height, width = stdscr.getmaxyx()
    stdscr.clear()
    show_title_screen(stdscr,height,width)
    while True:
        draw_scene(stdscr, structures, height, width)
        ch = stdscr.getch()
        if ch == curses.KEY_MOUSE:
            _, x, y, _, bstate = curses.getmouse()
            if bstate & curses.BUTTON1_CLICKED:
                add_structure(structures, y, x,height)


if __name__ == '__main__':
    curses.wrapper(main)