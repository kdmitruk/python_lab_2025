from PySide6.QtWidgets import QDialog, QCheckBox, QGridLayout, QPushButton, QComboBox


class SettingsDialog(QDialog):
    def __init__(self, weather_params: dict, parent = None):
        super().__init__(parent)
        self.setWindowTitle("Settings")

        self.temperature_box = QCheckBox("Temperature",self)
        self.temperature_box.setChecked(weather_params["temperature_2m"])

        self.temperature_unit_box = QComboBox(self)
        self.temperature_unit_box.addItem("°C")
        self.temperature_unit_box.addItem("°F")
        self.temperature_unit_box.setVisible(self.temperature_box.isChecked())

        self.weather_code_box = QCheckBox("Weather Code",self)
        self.weather_code_box.setChecked(weather_params["weather_code"])

        self.pressure_msl_box = QCheckBox("Pressure",self)
        self.pressure_msl_box.setChecked(weather_params["pressure_msl"])

        self.ok_button = QPushButton("Ok",self)
        self.cancel_button = QPushButton("Cancel",self)

        layout = QGridLayout(self)
        layout.addWidget(self.temperature_box,0,0,1,1)
        layout.addWidget(self.temperature_unit_box,0,1,1,1)
        layout.addWidget(self.weather_code_box,1,0,1,2)
        layout.addWidget(self.pressure_msl_box,2,0,1,2)
        layout.addWidget(self.ok_button,3,0)
        layout.addWidget(self.cancel_button,3,1)

        self.ok_button.clicked.connect(self.accept)
        self.cancel_button.clicked.connect(self.reject)
        self.temperature_box.toggled.connect(self.temperature_unit_box.setVisible)

    def get_params(self):
        return {
            "temperature_2m": self.temperature_box.isChecked(),
            "weather_code": self.weather_code_box.isChecked(),
            "pressure_msl": self.pressure_msl_box.isChecked()
        }

    # def get_params(self):
    #     result = []
    #     current_result = []
    #     if self.temperature_box.isChecked():
    #         current_result += ["temperature_2m"]
    #         if self.temperature_unit_box.currentText() == "°F":
    #             result += ["temperature_unit=fahrenheit"]
    #     if self.weather_code_box.isChecked():
    #         current_result += ["weather_code"]
    #     if self.pressure_msl_box.isChecked():
    #         current_result += ["pressure_msl"]
    #
    #     current_result = f"current={','.join(current_result)}"
    #     result += [current_result]
    #     result='&'.join(result)
    #     return result

