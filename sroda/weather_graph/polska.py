import math
from datetime import datetime, timedelta

import geopandas as gpd
import matplotlib.pyplot as plt
import requests

cities = [
    ("Warszawa", 52.2297, 21.0122),
    ("Kraków" ,50.0647, 19.9450),
    ("Łódź" ,51.7592, 19.4560),
    ("Wrocław", 51.1079, 17.0385),
    ("Poznań", 52.4064, 16.9252),
    ("Gdańsk", 54.3520, 18.6466),
    ("Szczecin", 53.4285, 14.5528),
    ("Bydgoszcz", 53.1235, 18.0084),
    ("Lublin",51.2465, 22.5684),
    ("Katowice",50.2649, 19.0238),
    ("Białystok",53.1325, 23.1688),
    ("Rzeszów",50.0413, 21.9990),
    ("Olsztyn",53.7784, 20.4801),
    ("Kielce",50.8661, 20.6286),
    ("Opole",50.6751, 17.9213),
    ("Zielona Góra",51.9355, 15.5062)
]

class PolandMap:
    def __init__(self, shapefile_url=None):
        default_url = 'https://naciscdn.org/naturalearth/50m/cultural/ne_50m_admin_0_countries.zip'
        self.shapefile_url = shapefile_url or default_url
        self._world = gpd.read_file(self.shapefile_url)
        self.poland = self._world[self._world['ADMIN'] == 'Poland']
        self.active_index = 0

    def draw(self):
        fig, (map_ax, temp_ax) = plt.subplots(2,1, figsize=(8, 12))
        self.fig = fig
        self.map_ax = map_ax
        self.temp_ax = temp_ax
        self.poland.plot(ax=map_ax, color='lightgrey', edgecolor='black')
        self.data = self.get_data()
        self.draw_cities(map_ax, self.data, fig)
        self.draw_cities_labels(map_ax,self.data)
        self.draw_temperature_plot(temp_ax, self.data)
        plt.tight_layout()
        cid = fig.canvas.mpl_connect('button_press_event', self.onclick)

    def draw_cities(self, ax, data, fig):
        x = [city[2] for city in cities]
        y = [city[1] for city in cities]
        c = [entry["hourly"]["temperature_2m"][0] for entry in data]
        plot = ax.scatter(x, y, c=c, cmap="Spectral_r")
        fig.colorbar(plot,ax=ax,label="C")

    def draw_cities_labels(self, ax, data):
        for city,entry in zip(cities,data):
            label = f"{city[0]}\n{entry["hourly"]["temperature_2m"][0]}"
            ax.text(city[2],city[1],label , ha = "center", bbox = dict(boxstyle = "Round,pad=0.2", fc = "white", alpha = 0.2))

    def get_data(self):
        start_date = datetime.now().date()
        end_date = start_date + timedelta(days=7)

        latitude = ",".join([str(city[1]) for city in cities])
        longitude = ",".join([str(city[2]) for city in cities])

        url = (
            f"https://api.open-meteo.com/v1/forecast?"
            f"latitude={latitude}&longitude={longitude}"
            f"&hourly=temperature_2m"
            f"&start_date={start_date}&end_date={end_date}"
            f"&timezone=Europe/Warsaw"
        )

        response = requests.get(url)
        data = response.json()
        for i in range(len(cities)):
            print(cities[i][0], data[i]["hourly"]["temperature_2m"][0])
        return data

    def draw_temperature_plot(self, ax, data):
        hourly = data[self.active_index]["hourly"]
        format = "%Y-%m-%dT%H:%M"
        hours = [datetime.strptime(i,format) for i in hourly["time"]]
        ax.plot(hours, hourly["temperature_2m"], label="temperatura", color="red")
        ax.tick_params(axis="x",labelrotation = 45)
        ax.grid(True)
        self.fig.canvas.draw()

    def onclick(self,event):
        if event.inaxes == self.map_ax:
            for i,city in enumerate(cities):
                print(city[0], math.hypot(city[2] - event.xdata,city[1] - event.ydata))
                if math.hypot(city[2] - event.xdata,city[1] - event.ydata) < 0.25:
                    self.fig.set_label(city[0])
                    self.active_index = i
                    self.draw_temperature_plot(self.temp_ax,self.data)
            print('%s click: button=%d, x=%d, y=%d, xdata=%f, ydata=%f' %
                ('double' if event.dblclick else 'single', event.button,
                event.x, event.y, event.xdata, event.ydata))

if __name__ == '__main__':
    poland = PolandMap()
    poland.draw()
    plt.show()
