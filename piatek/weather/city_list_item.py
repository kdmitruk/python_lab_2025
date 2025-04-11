from PySide6.QtWidgets import QListWidgetItem
import pickle
import base64

class CityListItem(QListWidgetItem):
    def __init__(self, name, latitude, longitude):
        super().__init__(name)
        self.latitude = latitude
        self.longitude = longitude

    def __eq__(self, other):
        return self.text() == other.text() and self.latitude == other.latitude and self.longitude == other.longitude

    def dump(self):
        data = pickle.dumps((self.text(), self.latitude, self.longitude))
        data = base64.b64encode(data)
        return data

    @staticmethod
    def from_dump(data):
        data = base64.b64decode(data)
        name, latitude, longitude = pickle.loads(data)
        return CityListItem(name, latitude, longitude)