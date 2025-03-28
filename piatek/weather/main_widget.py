from PySide6.QtWidgets import QWidget

class MainWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle('Weather')