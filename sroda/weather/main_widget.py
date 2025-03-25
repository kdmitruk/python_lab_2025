from PySide6.QtWidgets import QWidget


class MainWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Weather")
