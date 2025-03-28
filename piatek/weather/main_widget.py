from PySide6.QtWidgets import QWidget, QLineEdit, QPushButton, QLabel, QGridLayout


class MainWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle('Weather')
        self.city_edit = QLineEdit(self)
        get_cities_button = QPushButton("Get cities", self)
        self.weather_label = QLabel(self)
        get_cities_button.clicked.connect(self.get_cities)

        layout = QGridLayout(self)
        layout.addWidget(self.city_edit, 0, 0)
        layout.addWidget(get_cities_button, 0, 1)
        layout.addWidget(self.weather_label, 1, 0, 1, 2)

    def get_cities(self):
        self.weather_label.setText(self.city_edit.text())