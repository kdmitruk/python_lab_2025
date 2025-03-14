import curses
import os


def load_structure_from_directory(path):
    file_names=os.listdir(path)
    structures={}
    for file_name in file_names:
        file_path=os.path.join(path,file_name)
        structure=load_structure_from_file(file_path)
        structures[structure[0]]=structure
    return structures

def load_structure_from_file(path):
    with open(path) as file:
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

def add_structure(structures, y, x,height, available_structures, active_structure):
    structures.append((y,x, list(available_structures.keys())[active_structure]))

def draw_map(stdscr, structures, available_structures):
    for y, x, name in structures:
        draw_structure(stdscr,available_structures[name],x,y,centered=True)

def draw_scene(stdscr, structures, active_structure, available_structures, height, width):
    stdscr.clear()
    draw_map(stdscr, structures, available_structures)
    stdscr.addstr(height - 1, 0, list(available_structures.keys())[active_structure])
    stdscr.refresh()

def show_title_screen(stdscr,height,width):
    contents=["Map maker", "version 1.0", "", "Naciśnij dowolny klawisz aby kontynuować"]
    y=(height-len(contents))//2
    for i in range(len(contents)):
        x=(width-len(contents[i]))//2
        stdscr.addstr(y+i, x, contents[i])

    stdscr.getch()

def main(stdscr):
    available_structures=load_structure_from_directory('structures')
    active_structure = 0

    curses.start_color()
    curses.init_pair(1,curses.COLOR_YELLOW,curses.COLOR_BLACK)
    curses.curs_set(0)
    curses.mousemask(curses.ALL_MOUSE_EVENTS | curses.REPORT_MOUSE_POSITION)
    structures = []
    height, width = stdscr.getmaxyx()
    stdscr.clear()
    show_title_screen(stdscr,height,width)
    while True:
        draw_scene(stdscr, structures, active_structure, available_structures, height, width)
        ch = stdscr.getch()
        if ch == ord('q'):
            break
        elif ch in list(range(ord('1'),ord('4') + 1)):
            active_structure = ch - ord('1')
        elif ch == curses.KEY_MOUSE:
            _, x, y, _, bstate = curses.getmouse()
            if bstate & curses.BUTTON1_CLICKED:
                add_structure(structures, y, x,height, available_structures, active_structure)


if __name__ == '__main__':
    curses.wrapper(main)
