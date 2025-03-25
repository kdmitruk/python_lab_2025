from PySide6.QtCore import Qt
from PySide6.QtWidgets import QWidget, QLabel, QPushButton, QLineEdit, QGridLayout, QMessageBox, QListWidget, \
    QListWidgetItem
import requests

class MainWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Weather")

        self.label = QLabel(self)
        self.button = QPushButton(self)
        self.edit = QLineEdit("Lublin", self)
        self.city_list = QListWidget(self)

        self.button.clicked.connect(self._on_button_clicked)
        self.city_list.itemClicked.connect(self.on_city_clicked)

        layout = QGridLayout(self)
        layout.addWidget(self.edit, 0, 0, 1, 1)
        layout.addWidget(self.button, 0, 1, 1, 1)
        layout.addWidget(self.city_list, 1, 0, 1, 2)
        layout.addWidget(self.label, 2, 0, 1, 2)

    def _on_button_clicked(self):
        text = self.edit.text()
        #self.label.setText(text)
        response = requests.get(f'https://geocoding-api.open-meteo.com/v1/search?name={text}')
        #print(response.json())
        json = response.json()
        if "results" not in json.keys():
            QMessageBox.information(self, "error", "Brak miejscowosci")
            return

        results = json["results"]
        self.city_list.clear()
        for city in results:
            #self.city_list.addItem(city["name"])
            item = QListWidgetItem(city["name"])
            latitude = city["latitude"]
            longitude = city["longitude"]
            item.setData(Qt.UserRole,(latitude,longitude))
            self.city_list.addItem(item)
        #print(results)
        result = results[0]
        #print(result)
        latitude = result["latitude"]
        longitude = result["longitude"]
        print(latitude, longitude)

    def on_city_clicked(self):
        print(self.city_list.currentItem().data(Qt.UserRole))




