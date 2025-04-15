from PySide6.QtCore import Qt, QSettings
from PySide6.QtWidgets import QWidget, QLabel, QPushButton, QLineEdit, QGridLayout, QMessageBox, QListWidget, \
    QListWidgetItem
import requests

from city_list_item import CityListItem
from settings_dialog import SettingsDialog


class MainWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Weather")

        self.label = QLabel(self)
        self.button = QPushButton(self)
        self.settings_button = QPushButton("Settings", self)
        self.edit = QLineEdit("Lublin", self)
        self.city_list = QListWidget(self)
        self.fav_city_list = QListWidget(self)

        self.button.clicked.connect(self._on_button_clicked)
        self.city_list.itemDoubleClicked.connect(self.__move_city_to_fav)
        self.fav_city_list.itemClicked.connect(self.__get_weather_for_clicked_city)
        self.settings_button.clicked.connect(self.__show_settings)

        layout = QGridLayout(self)
        layout.addWidget(self.edit, 0, 0, 1, 1)
        layout.addWidget(self.button, 0, 1, 1, 1)
        layout.addWidget(self.city_list, 1, 0, 1, 2)
        layout.addWidget(self.fav_city_list, 2, 0, 1, 2)
        layout.addWidget(self.label, 3, 0, 1, 2)
        layout.addWidget(self.settings_button, 4, 0, 1, 2)

        self.qsettings = QSettings()
        self.weather_params = {
            "temperature_2m": self.qsettings.value("current/temperature_2m", True, type=bool),
            "weather_code": self.qsettings.value("current/weather_code", False, type=bool),
            "pressure_msl": self.qsettings.value("current/pressure_msl", False, type=bool)
        }
        self.__restore_favorites()

    def _on_button_clicked(self):
        text = self.edit.text()
        response = requests.get(f'https://geocoding-api.open-meteo.com/v1/search?name={text}')
        json = response.json()
        if "results" not in json.keys():
            QMessageBox.information(self, "error", "Brak miejscowosci")
            return

        results = json["results"]
        self.city_list.clear()
        for city in results:
            item = CityListItem(city["name"], city["latitude"], city["longitude"])
            found = False
            for i in range(self.fav_city_list.count()):
                if item == self.fav_city_list.item(i):
                    found = True
                    break
            if not found:
              self.city_list.addItem(item)

    def __update_fav_setting(self):
        favorites = []
        for i in range(self.fav_city_list.count()):
            favorites.append(self.fav_city_list.item(i).serialize())
        dump = ";".join(favorites)
        self.qsettings.setValue("cities/favorites", dump)

    def __restore_favorites(self):
        dump = self.qsettings.value("cities/favorites", "", type=str)
        if dump != "":
            favorites = dump.split(";")
            for favorite in favorites:
                self.fav_city_list.addItem(CityListItem.deserialize(favorite))


    def __move_city_to_fav(self):
        # current_city = self.city_list.currentItem()
        current_city = self.city_list.takeItem(self.city_list.currentRow())
        self.fav_city_list.addItem(current_city)
        self.__update_fav_setting()


    def __get_weather_for_clicked_city(self):
        latitute, longitute = self.fav_city_list.currentItem().get_geo_params()
        params = []
        for key, val in self.weather_params.items():
            if val == True:
                params.append(key)
        response = requests.get(f'https://api.open-meteo.com/v1/forecast?latitude={latitute}&longitude={longitute}&current={','.join(params)}')
        json = response.json()
        self.label.setText(f"{json["current"]}")


    def __show_settings(self):
        settings_dialog = SettingsDialog(self.weather_params, parent=self)
        settings_dialog.exec()
        if settings_dialog.result():
            self.weather_params = settings_dialog.get_params()
            self.qsettings.setValue("current/temperature_2m", self.weather_params["temperature_2m"])
            self.qsettings.setValue("current/weather_code", self.weather_params["weather_code"])
            self.qsettings.setValue("current/pressure_msl", self.weather_params["pressure_msl"])

    def keyPressEvent(self, event):
        if (self.fav_city_list.hasFocus()
                and event.key() == Qt.Key.Key_Delete):
            self.fav_city_list.takeItem(self.fav_city_list.currentRow())
            self.__update_fav_setting()







