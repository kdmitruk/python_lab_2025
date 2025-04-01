from PySide6.QtWidgets import QDialog, QCheckBox, QGridLayout, QPushButton


class SettingsDialog(QDialog):
    def __init__(self, parent = None):
        super().__init__(parent)
        self.setWindowTitle("Settings")

        self.temperature_box = QCheckBox("Temperature",self)
        self.weather_code_box = QCheckBox("Weather Code",self)
        self.pressure_msl_box = QCheckBox("Pressure",self)
        self.ok_button = QPushButton("Ok",self)
        self.cancel_button = QPushButton("Cancel",self)

        layout = QGridLayout(self)
        layout.addWidget(self.temperature_box,0,0,1,2)
        layout.addWidget(self.weather_code_box,1,0,1,2)
        layout.addWidget(self.pressure_msl_box,2,0,1,2)
        layout.addWidget(self.ok_button,3,0)
        layout.addWidget(self.cancel_button,3,1)

        self.ok_button.clicked.connect(self.accept)
        self.cancel_button.clicked.connect(self.reject)

    def get_params(self):
        result = []
        if self.temperature_box.isChecked():
            result += ["temperature_2m"]
        if self.weather_code_box.isChecked():
            result += ["weather_code"]
        if self.pressure_msl_box.isChecked():
            result += ["pressure_msl"]

        return result

