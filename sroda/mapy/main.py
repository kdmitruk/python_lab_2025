import curses
import os


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
    global barracks
    for y, x in structures:
        draw_structure(stdscr,x,y,barracks,centered = True)

def draw_structure(stdscr,x,y,structure,centered = False, labeled = False, highlighted = False):
    name, art = structure
    offset_y = y - len(art)
    offset_x = x - len(art[0])//2 if centered else x
    for i, line in enumerate(art):
        stdscr.addstr(offset_y+i, offset_x, line, curses.color_pair(1 if highlighted else 0))
    if labeled:
        stdscr.addstr(offset_y + len(art)+1,offset_x,name,curses.color_pair(1 if highlighted else 0))

def add_structure(structures, y, x, rows):
    structures.append((y, x))

def load_structure_from_file(path):
    with open(path) as fd:
        lines = fd.read().splitlines()
        name, image = lines[0], lines[1:]
        return name, image
def load_stuctures_from_directory():
    path = "structures"
    dir_list = os.listdir(path)
    #print(dir_list)
    result = {}

    for file_name in dir_list:
        file_path = os.path.join(path,file_name)
        stucture = load_structure_from_file(file_path)
        result[stucture[0]] = stucture
    return result



barracks = load_structure_from_file('structures/barracks.txt')

def main(stdscr):
    curses.start_color()
    curses.init_pair(1,curses.COLOR_YELLOW, curses.COLOR_BLACK)

    curses.curs_set(0)
    curses.mousemask(curses.ALL_MOUSE_EVENTS | curses.REPORT_MOUSE_POSITION)

    height, width = stdscr.getmaxyx()
    stdscr.clear()
    show_title_screen(stdscr, height, width)
    stdscr.clear()
    structures = []
    while True:
        draw_map(stdscr, height, width, structures)
        stdscr.refresh()

        key = stdscr.getch()
        if key == curses.KEY_MOUSE:
            _, x, y, _, bstate = curses.getmouse()
            if bstate & curses.BUTTON1_CLICKED:
                add_structure(structures, y, x, height)

if __name__ == '__main__':
    #curses.wrapper(main)
    print(load_stuctures_from_directory())
