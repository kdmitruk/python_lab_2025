from PySide6.QtWidgets import QWidget, QLabel, QPushButton, QLineEdit, QGridLayout


class MainWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Weather")

        self.label = QLabel(self)
        self.button = QPushButton(self)
        self.edit = QLineEdit(self)

        layout = QGridLayout(self)
        layout.addWidget(self.edit, 0, 0, 1, 1)
        layout.addWidget(self.button, 0, 1, 1, 1)
        layout.addWidget(self.label, 1, 0, 1, 2)






