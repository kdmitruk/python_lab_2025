from PySide6.QtCore import QSettings
from PySide6.QtWidgets import QDialog, QCheckBox, QPushButton, QGridLayout


class SettingsDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Settings")

        settings = QSettings()
        self.temperature_box = QCheckBox('Temperature', self)
        self.temperature_box.setChecked(settings.value('parameters/temperature_2m', True, type=bool))
        self.weather_code_box = QCheckBox('Weather code', self)
        self.weather_code_box.setChecked(settings.value('parameters/weather_code', False, type=bool))
        self.pressure_box = QCheckBox('Pressure', self)
        self.pressure_box.setChecked(settings.value('parameters/pressure_msl', False, type=bool))
        okay_button = QPushButton('Okay', self)
        cancel_button = QPushButton('Cancel', self)

        layout = QGridLayout(self)
        layout.addWidget(self.temperature_box, 0, 0, 1, 2)
        layout.addWidget(self.weather_code_box, 1, 0, 1, 2)
        layout.addWidget(self.pressure_box, 2, 0, 1, 2)
        layout.addWidget(okay_button, 3, 0)
        layout.addWidget(cancel_button, 3, 1)

        okay_button.clicked.connect(self.accept)
        cancel_button.clicked.connect(self.reject)

    def result_data(self):
        result = {}
        result.update({'temperature_2m': self.temperature_box.isChecked()})
        result.update({'weather_code': self.weather_code_box.isChecked()})
        result.update({'pressure_msl': self.pressure_box.isChecked()})
        return result