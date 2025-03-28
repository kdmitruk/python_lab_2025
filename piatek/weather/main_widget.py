from PySide6.QtWidgets import QWidget, QLineEdit, QPushButton, QLabel, QGridLayout, QMessageBox, QListWidget
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
            self.city_list.addItem(f"{name}, {country}")
