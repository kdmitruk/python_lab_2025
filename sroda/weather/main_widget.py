from PySide6.QtWidgets import QWidget, QLabel, QPushButton, QLineEdit, QGridLayout, QMessageBox
import requests

class MainWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Weather")

        self.label = QLabel(self)
        self.button = QPushButton(self)
        self.edit = QLineEdit("abdsabsd", self)

        self.button.clicked.connect(self._on_button_clicked)

        layout = QGridLayout(self)
        layout.addWidget(self.edit, 0, 0, 1, 1)
        layout.addWidget(self.button, 0, 1, 1, 1)
        layout.addWidget(self.label, 1, 0, 1, 2)

    def _on_button_clicked(self):
        text = self.edit.text()
        #self.label.setText(text)
        response = requests.get(f'https://geocoding-api.open-meteo.com/v1/search?name={text}')
        #print(response.json())
        json = response.json()
        if "results" not in json.keys():
            QMessageBox.information(self, "error", "Brak miejscowosci")
            return

        results = response.json()["results"]
        #print(results)
        result = results[0]
        #print(result)
        latitude = result["latitude"]
        longitude = result["longitude"]
        print(latitude, longitude)






