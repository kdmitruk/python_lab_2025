from math import sin, radians, cos
from time import sleep
import os

GRAVITY = 9.81
DISTANCE = 100
IMPACT_RADIUS = 5
ROWS=80
COLS=24

def animate_shot(velocity, angle):
    t_c = 2* velocity * sin(angle) / GRAVITY
    d_t = 0.05
    v_x = velocity * cos(angle)
    v_y = velocity * sin(angle)
    t = 0
    while t < t_c:
        x = v_x * t
        y = v_y * t - GRAVITY * t**2 / 2

        draw_scene_adjusted(x, y)
        t += d_t
        sleep(d_t)
        clear()


def clear():
    os.system("clear")

def draw_scene_adjusted(x, y):
    aspect_ratio = COLS / DISTANCE

    x_t = x * aspect_ratio
    y_t = ROWS  - (y * aspect_ratio / 2)

    draw_scene(round(x_t), round(y_t))

def draw_scene(x,y):
    for _ in range(y-2):
        print()
    for _ in range(x-1):
        print(" ",end="")
    print("o")
    for _ in range(y,ROWS-1):
        print()
    for _ in range(COLS):
        print("‾",end="")


def get_input():
    angle = None
    while angle is None or not(angle>=0 and angle<=90):
        angle = float(input("Podaj kąt: "))
    velocity = float(input("Podaj prędkość: "))
    angle = radians(angle)
    return angle, velocity

def calculate_impact(angle, velocity):
    return velocity**2 * sin(2 * angle) / GRAVITY

def check_victory(distance,z):
    return abs(distance-z)<IMPACT_RADIUS

def main():
    player = 1
    while True:
        print(f"tura gracza {player}")
        angle, velocity = get_input()
        z=calculate_impact(angle, velocity)
        print(z)
        # if player==1:
        animate_shot(velocity, angle)
        if check_victory(DISTANCE,z):
            break
        # else:
        #     if check_victory(0,DISTANCE-z):
        #         break

        # player=3-player
    print(f"Zwyciężył gracz {player}")

if __name__ == '__main__':
    main()
    #draw_scene_adjusted(100,100)

