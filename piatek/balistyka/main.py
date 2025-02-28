from math import sin, radians, cos
GRAVITY = 9.81
def get_input():
    angle = None
    while angle is None or not(angle>=0 and angle<=90):
        angle = float(input("Podaj kąt: "))
    velocity = float(input("Podaj prędkość: "))
    angle = radians(angle)
    return angle, velocity

def calculate_impact(angle, velocity):
    return velocity**2 * sin(2 * angle) / GRAVITY


def main():
    while True:
        angle, velocity = get_input()
        print(calculate_impact(angle, velocity))


if __name__ == '__main__':
    main()

