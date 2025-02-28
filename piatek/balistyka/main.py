from math import sin, radians, cos
GRAVITY = 9.81
DISTANCE = 100
IMPACT_RADIUS = 5
ROWS=6
COLS=10

def draw_scene_adjusted(x, y):
    aspect_ratio = COLS / DISTANCE

    x_t = x * aspect_ratio
    y_t = ROWS  - (y * aspect_ratio / 2)

    draw_scene(round(x_t), round(y_t))

def draw_scene(x,y):
    for _ in range(y-1):
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
        if check_victory(DISTANCE,z):
            break
        # else:
        #     if check_victory(0,DISTANCE-z):
        #         break

        # player=3-player
    print(f"Zwyciężył gracz {player}")

if __name__ == '__main__':
    #    main()
    draw_scene_adjusted(100,100)

