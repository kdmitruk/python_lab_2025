from PySide6.QtWidgets import QListWidgetItem


class CityListItem(QListWidgetItem):
    def __init__(self, name, latitude, longitude):
        super().__init__(name)
        self.latitude = latitude
        self.longitude = longitude

    def __eq__(self, other):
        return self.text() == other.text() and self.latitude == other.latitude and self.longitude == other.longitude
