from PySide6.QtCore import QSettings
from PySide6.QtGui import Qt
from PySide6.QtWidgets import QWidget, QLineEdit, QPushButton, QLabel, QGridLayout, QMessageBox, QListWidget, \
    QListWidgetItem
import requests

from city_list_item import CityListItem
from settings_dialog import SettingsDialog


class MainWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle('Weather')
        self.city_edit = QLineEdit('Lublin', self)
        get_cities_button = QPushButton("Get cities", self)
        self.weather_label = QLabel(self)
        self.city_list = QListWidget(self)
        settings_button = QPushButton("Settings", self)

        get_cities_button.clicked.connect(self.get_cities)
        settings_button.clicked.connect(self.show_settings)
        self.city_list.itemClicked.connect(self.get_weather)

        layout = QGridLayout(self)
        layout.addWidget(self.city_edit, 0, 0)
        layout.addWidget(get_cities_button, 0, 1)
        layout.addWidget(self.city_list, 1, 0, 1, 2)
        layout.addWidget(self.weather_label, 2, 0, 1, 2)
        layout.addWidget(settings_button, 3, 0, 1, 2)

        # self.weather_params = {"temperature_2m": True}

    def get_cities(self):
        url = f"https://geocoding-api.open-meteo.com/v1/search?name={self.city_edit.text()}"
        response = requests.get(url)
        json = response.json()
        if 'results' not in json.keys():
            QMessageBox.critical(self, "Error!!!", "No such city")
            return
        results = json['results']
        for city in results:
            latitude = city['latitude']
            longitude = city['longitude']
            name = city['name']
            country = city['country']
            item = CityListItem(f"{name}, {country}", latitude, longitude)
            self.city_list.addItem(item)

    def get_weather(self):
        # print(self.city_list.currentItem().data(Qt.UserRole))
        latitude = self.city_list.currentItem().latitude
        longitude = self.city_list.currentItem().longitude
        keys = ''
        settings = QSettings()
        settings.beginGroup('parameters')
        for key in settings.childKeys():
            if settings.value(key, type=bool) == True:
                keys += key + ','
        url=f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&current={keys}"
        response = requests.get(url)
        json = response.json()
        self.weather_label.setText(str(json['current']))

    def show_settings(self):
        settings_dialog = SettingsDialog()

        settings_dialog.exec()
        if settings_dialog.result() == 1:
            # self.weather_params = settings_dialog.result_data()
            settings = QSettings()
            for key, value in settings_dialog.result_data().items():
                settings.setValue(f'parameters/{key}', value)