import geopandas as gpd
import matplotlib.pyplot as plt

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

    def draw(self):
        fig, ax = plt.subplots(figsize=(8, 8))
        self.poland.plot(ax=ax, color='lightgrey', edgecolor='black')
        self.draw_cities(ax)
        self.draw_cities_labels(ax)

    def draw_cities(self, ax):
        x = [city[2] for city in cities]
        y = [city[1] for city in cities]
        ax.scatter(x, y)

    def draw_cities_labels(self, ax):
        for city in cities:
            ax.text(city[2],city[1], city[0], ha = "center", bbox = dict(boxstyle = "Round,pad=0.2", fc = "white", alpha = 0.2))


if __name__ == '__main__':
    poland = PolandMap()
    poland.draw()
    plt.show()
