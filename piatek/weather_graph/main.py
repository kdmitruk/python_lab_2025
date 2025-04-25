import requests
import PySide6
import matplotlib.pyplot as plt
from datetime import datetime, timedelta



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

format = "%Y-%m-%dT%H:%M"
temperature_2m = data["hourly"]["temperature_2m"]
apparent_temperature = data['hourly']['apparent_temperature']
precipitation = data['hourly']['precipitation']
print(temperature_2m)
x = [datetime.strptime(i, format) for i in data["hourly"]["time"]]
print(x)
# plt.figure(figsize=(6,4))
fig, (ax_temp, ax_rain) = plt.subplots(2,1,figsize=(6,8), sharex=True)
ax_temp.plot(x, temperature_2m, label='Temperatura', color='red')
ax_temp.plot(x, apparent_temperature, label='Temperatura odczuwalna')
ax_rain.bar(x, precipitation, label='Opady')
ax_temp.legend()
ax_temp.set_ylabel('temperatura')
ax_temp.set_xlabel("czas")
ax_rain.tick_params(axis='x',rotation = 45)

fig.canvas.manager.set_window_title('Wykres')
for ax in [ax_temp, ax_rain]:
    ax.grid(True)
plt.show()

#print(data["daily"])
print(data["hourly"])
