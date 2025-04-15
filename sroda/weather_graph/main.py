import requests
from datetime import datetime, timedelta
import matplotlib.pyplot as plt
import PySide6

def get_data():
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
    print(data["hourly"])
    return data["hourly"]
    #print(data["daily"])
    #print(data["hourly"])

def draw_graph(data):
    format = "%Y-%m-%dT%H:%M"
    hours = [datetime.strptime(i,format) for i in data["time"]]
    plt.figure(figsize=(6,4))
    plt.plot(hours, data["temperature_2m"], label="mój pierwszy wykres", color="red")
    plt.grid()
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.title("wykres")
    plt.legend()
    plt.xticks(rotation = 45)
    plt.show()

if __name__ == '__main__':
    data = get_data()
    draw_graph(data)
