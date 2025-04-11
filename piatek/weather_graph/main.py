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

y = data["hourly"]["temperature_2m"]
print(y)
x = [i for i in range(len(y))]
print(x)
plt.figure(figsize=(6,4))
plt.plot(x, y)
plt.ylabel('temperatura')
plt.title('Wykres')
plt.grid(True)
plt.show()

#print(data["daily"])
#print(data["hourly"])
