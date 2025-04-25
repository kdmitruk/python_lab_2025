import geopandas as gpd
import matplotlib.pyplot as plt



class PolandMap:
    cities = {
        "Warszawa": (52.2297, 21.0122),
        "Kraków":   (50.0647, 19.9450),
        "Łódź":     (51.7592, 19.4560),
        "Wrocław":  (51.1079, 17.0385),
        "Poznań":   (52.4064, 16.9252),
        "Gdańsk":   (54.3520, 18.6466),
        "Szczecin": (53.4285, 14.5528),
        "Bydgoszcz":(53.1235, 18.0084),
        "Lublin":   (51.2465, 22.5684),
        "Katowice": (50.2649, 19.0238),
        "Białystok":(53.1325, 23.1688),
        "Rzeszów":  (50.0413, 21.9990),
        "Olsztyn":  (53.7784, 20.4801),
        "Kielce":   (50.8661, 20.6286),
        "Opole":    (50.6751, 17.9213),
        "Zielona Góra": (51.9355, 15.5062)
    }

    def __init__(self, shapefile_url=None):
        default_url = 'https://naciscdn.org/naturalearth/50m/cultural/ne_50m_admin_0_countries.zip'
        self.shapefile_url = shapefile_url or default_url
        self._world = gpd.read_file(self.shapefile_url)
        self.poland = self._world[self._world['ADMIN'] == 'Poland']

    def draw(self):
        fig, ax = plt.subplots(figsize=(8, 8))
        self.poland.plot(ax=ax, color='lightgrey', edgecolor='black')
        ax.scatter([city_pos[1] for city_pos in self.cities.values()],
                   [city_pos[0] for city_pos in self.cities.values()])
        for city_name,city_pos in self.cities.items():
            ax.text(city_pos[1],city_pos[0],city_name,ha='center',va='bottom',
                    bbox=dict(fc="white",alpha=0.2,boxstyle="round,pad=0.6"))
if __name__ == '__main__':
    poland = PolandMap()
    poland.draw()
    plt.show()
