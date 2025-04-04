from PySide6.QtWidgets import QApplication, QWidget

from main_widget import MainWidget


def main():
    app = QApplication()
    QApplication.setOrganizationName("UMCS")
    QApplication.setApplicationName("Pogoda")
    widget = MainWidget()
    widget.show()
    return app.exec()

if __name__ == '__main__':
    main()