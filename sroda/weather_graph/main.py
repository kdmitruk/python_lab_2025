import requests
from datetime import datetime, timedelta
import matplotlib.pyplot as plt
import PySide6

def main():
    latitude = 51.25
    longitude = 22.57

    start_date = datetime.now().date()
    end_date = start_date + timedelta(days=7)

    url = (
        f"https://api.open-meteo.com/v1/forecast?"
        f"latitude={latitude}&longitude={longitude}"
        f"&daily=sunrise,sunset"
        f"&hourly=temperature_2m,apparent_temperature,precipitation"
        f"&start_date={start_date}&end_date={end_date}"
        f"&timezone=Europe/Warsaw"
    )

    response = requests.get(url)
    data = response.json()

    print(data["daily"])
    print(data["hourly"])

def draw_line():
    plt.figure(figsize=(6,4))
    plt.plot([0,1],[0,1], label="mój pierwszy wykres", marker="x", color="red")
    plt.grid()
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.title("wykres")
    plt.legend()
    plt.show()



if __name__ == '__main__':
    #main()
    draw_line()
