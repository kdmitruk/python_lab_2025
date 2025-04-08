from PySide6.QtWidgets import QListWidgetItem
from base64 import b64encode, b64decode

class CityListItem(QListWidgetItem):
    def __init__(self, name, lat, long):
        super().__init__()

        self.setText(name)
        self.lat = lat
        self.long = long

    def get_geo_params(self):
        return self.lat,self.long

    def serialize(self):
        return b64encode(f"{self.lat};{self.long};{self.text()}".encode()).decode()

    @classmethod
    def deserialize(cls, dump: bytes):
        lat, long, name = b64decode(dump).decode().split(";", maxsplit=2)
        return cls(name, lat, long)

    def __eq__(self, other):
        # if self == other:
        #     return True
        if not isinstance(other, CityListItem):
            return False
        return (self.text() == other.text()
                and self.lat == other.lat
                and self.long == other.long)