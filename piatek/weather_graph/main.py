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
days =  []
for x in range(len(data["daily"]["time"])):
    days.append((data["daily"]["sunrise"][x],data["daily"]["sunset"][x], data['daily']['time'][x]))


print(days)



x = [datetime.strptime(i, format) for i in data["hourly"]["time"]]
print(x)
# plt.figure(figsize=(6,4))
fig, (ax_temp, ax_rain) = plt.subplots(2,1,figsize=(6,8), sharex=True, dpi=600)
ax_temp.plot(x, temperature_2m, label='Temperatura', color='red')
ax_temp.plot(x, apparent_temperature, label='Temperatura odczuwalna')
for day in days:
    ax_temp.axvspan(day[0],day[1],color = "yellow",alpha = 0.2)
    ax_temp.axvspan(day[2],day[0], color='black', alpha = 0.2)
    ax_temp.axvspan(day[1], datetime.strptime(day[2], "%Y-%m-%d")+timedelta(days=1), color='black', alpha = 0.5)

ax_rain.bar(x, precipitation, label='Opady')
ax_temp.legend()
ax_temp.set_ylabel('temperatura')
ax_temp.set_xlabel("czas")
ax_rain.tick_params(axis='x',rotation = 45)

fig.canvas.manager.set_window_title('Wykres')
for ax in [ax_temp, ax_rain]:
    ax.grid(True)
#plt.show()
plt.savefig('plot.png')

print(data["daily"])
#print(data["hourly"])
