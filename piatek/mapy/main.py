import curses

barracks = None

def load_structure_from_file(src):
    with open(src) as file:
        lines = file.read()
        lines = lines.splitlines()
        return lines[0], lines[1:]

def draw_structure(stdscr, structure, x, y, centered = False, labeled = False, highlighted = False):
    name, art = structure
    y -= len(art)
    color = curses.color_pair(1 if highlighted else 0)
    if centered:
        x -= len(art[0]) // 2

    for i, line in enumerate(art):
        stdscr.addstr(i + y,x,line, color | curses.A_BOLD)

    if labeled:
        stdscr.addstr(y+len(art), x, name, color | curses.A_BOLD)

def add_structure(structures, y, x,height):
    structures.append((y,x))

def draw_map(stdscr, structures):
    global barracks
    for y, x in structures:
        draw_structure(stdscr,barracks,x,y,centered=True)

def draw_scene(stdscr, structures, height, width):
    stdscr.clear()
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
    global barracks
    barracks = load_structure_from_file("structures/barracks.txt")

    curses.start_color()
    curses.init_pair(1,curses.COLOR_YELLOW,curses.COLOR_BLACK)
    curses.curs_set(0)
    curses.mousemask(curses.ALL_MOUSE_EVENTS | curses.REPORT_MOUSE_POSITION)
    structures = []
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