from PySide6.QtCore import Qt
from PySide6.QtWidgets import QWidget, QLabel, QPushButton, QLineEdit, QGridLayout, QMessageBox, QListWidget, \
    QListWidgetItem
import requests

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

        self.button.clicked.connect(self._on_button_clicked)
        self.city_list.itemClicked.connect(self._on_city_clicked)
        self.settings_button.clicked.connect(self.__show_settings)

        layout = QGridLayout(self)
        layout.addWidget(self.edit, 0, 0, 1, 1)
        layout.addWidget(self.button, 0, 1, 1, 1)
        layout.addWidget(self.city_list, 1, 0, 1, 2)
        layout.addWidget(self.label, 2, 0, 1, 2)
        layout.addWidget(self.settings_button, 3, 0, 1, 2)

        self.weather_params = []

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
            item = QListWidgetItem(city["name"])
            latitude = city["latitude"]
            longitude = city["longitude"]
            item.setData(Qt.UserRole,(latitude,longitude))
            self.city_list.addItem(item)

    def _on_city_clicked(self):
        latitute, longitute = self.city_list.currentItem().data(Qt.UserRole)
        response = requests.get(f'https://api.open-meteo.com/v1/forecast?latitude={latitute}&longitude={longitute}&{self.weather_params}')
        json = response.json()
        self.label.setText(f"{json["current"]}")


    def __show_settings(self):
        settings_dialog = SettingsDialog(self)
        settings_dialog.exec()
        if settings_dialog.result():
            self.weather_params = settings_dialog.get_params()








