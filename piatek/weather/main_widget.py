from PySide6.QtGui import Qt
from PySide6.QtWidgets import QWidget, QLineEdit, QPushButton, QLabel, QGridLayout, QMessageBox, QListWidget, \
    QListWidgetItem
import requests

class MainWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle('Weather')
        self.city_edit = QLineEdit('Lublin', self)
        get_cities_button = QPushButton("Get cities", self)
        self.weather_label = QLabel(self)
        self.city_list = QListWidget(self)
        get_cities_button.clicked.connect(self.get_cities)
        self.city_list.itemClicked.connect(self.get_weather)

        layout = QGridLayout(self)
        layout.addWidget(self.city_edit, 0, 0)
        layout.addWidget(get_cities_button, 0, 1)
        layout.addWidget(self.city_list, 1, 0, 1, 2)
        layout.addWidget(self.weather_label, 2, 0, 1, 2)



    def get_cities(self):
        # self.weather_label.setText(self.city_edit.text())
        url = f"https://geocoding-api.open-meteo.com/v1/search?name={self.city_edit.text()}"
        response = requests.get(url)
        json = response.json()
        if 'results' not in json.keys():
            #print("No such city!")
            QMessageBox.critical(self, "Error!!!", "No such city")
            return
        results = json['results']
        for city in results:
            latitude = city['latitude']
            longitude = city['longitude']
            print(latitude, longitude)
            name = city['name']
            country = city['country']
            item = QListWidgetItem(f"{name}, {country}")
            item.setData(Qt.UserRole,(latitude, longitude))
            self.city_list.addItem(item)

    def get_weather(self):
        # print(self.city_list.currentItem().data(Qt.UserRole))
        latitude,longitude = self.city_list.currentItem().data(Qt.UserRole)
        url=f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&current=temperature_2m"
        response = requests.get(url)
        json = response.json()
        self.weather_label.setText(str(json['current']['temperature_2m']))
        # print(json['current']['temperature_2m'])