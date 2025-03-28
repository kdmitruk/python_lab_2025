from PySide6.QtWidgets import QWidget, QLineEdit, QPushButton, QLabel, QGridLayout


class MainWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle('Weather')
        city_edit = QLineEdit(self)
        get_cities_button = QPushButton("Get cities", self)
        weather_label = QLabel(self)

        layout = QGridLayout(self)
        layout.addWidget(city_edit, 0, 0)
        layout.addWidget(get_cities_button, 0, 1)
        layout.addWidget(weather_label, 1, 0, 1, 2)