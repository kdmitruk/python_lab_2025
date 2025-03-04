import curses

PANEL_HEIGHT = 10

def draw_separator(stdscr, rows, cols):
    y = rows - (PANEL_HEIGHT + 1)
    # stdscr.hline(y, 0, '-', cols)
    stdscr.addstr(y, 0, '-' * cols)
    stdscr.refresh()

def show_title_screen(stdscr, rows, cols):
    contents = ["Map maker", "version 1.0", "", "Naciśnij dowolny klawisz aby kontynuować"]
    offset_y = (rows - len(contents)) // 2
    for i, line in enumerate(contents):
        y = offset_y + i
        x = (cols - len(line)) // 2
        stdscr.addstr(y, x, line)
    stdscr.refresh()
    stdscr.getch()

def draw_map(stdscr, rows, cols, structures):
    # for structure in structures:
    #     y,x = structure
    #     stdscr.addstr(y,x,'*')
    #     #stdscr.addstr(structure[0], structure[1],'*')
    global barracks
    for i, line in enumerate(barracks[1]):
        stdscr.addstr(i, 0, line)
    for y, x in structures:
        stdscr.addstr(y,x,'*')


def add_structure(structures, y, x, rows):
    max_y = rows - (PANEL_HEIGHT + 1)
    if y < max_y:
        structures.append((y, x))

def load_structure_from_file(path):
    with open(path) as fd:
        lines = fd.read().splitlines()
        name, image = lines[0], lines[1:]
        return name, image

barracks = load_structure_from_file('structures/barracks.txt')

def main(stdscr):
    curses.curs_set(0)
    curses.mousemask(curses.ALL_MOUSE_EVENTS | curses.REPORT_MOUSE_POSITION)

    height, width = stdscr.getmaxyx()
    stdscr.clear()
    # stdscr.addstr(5, 10, f"* {height}x{width} *")
    show_title_screen(stdscr, height, width)
    stdscr.clear()
    structures = []
    while True:
        draw_map(stdscr, height, width, structures)
        draw_separator(stdscr, height, width)
        stdscr.refresh()

        key = stdscr.getch()
        if key == curses.KEY_MOUSE:
            _, x, y, _, bstate = curses.getmouse()
            if bstate & curses.BUTTON1_CLICKED:
                add_structure(structures, y, x, height)

if __name__ == '__main__':
    curses.wrapper(main)