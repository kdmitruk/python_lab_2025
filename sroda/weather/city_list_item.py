from PySide6.QtWidgets import QListWidgetItem


class CityListItem(QListWidgetItem):
    def __init__(self, name, lat, long):
        super().__init__()

        self.setText(name)
        self.lat = lat
        self.long = long

    def get_geo_params(self):
        return self.lat,self.long