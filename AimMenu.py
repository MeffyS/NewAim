import PySide2
import PySide6
from PySide6 import QtWidgets
from PySide6.QtWidgets import QPushButton
from PySide6.QtGui import QCursor, QIcon
import AimOptions
import sys
import time


class Menu(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        self.setGeometry(100, 100, 1200, 1200)
        self.setWindowTitle("Aim menu")
        self.setWindowIcon(QIcon("Aim_icons\click.png"))

        self.start_button = QPushButton("Start Aim", self)
        self.start_button.setGeometry(80, 50, 100, 30)
        self.start_button.clicked.connect(self.aim_start)
        self.setFixedHeight(250)
        self.setFixedWidth(250)

        self.options_button = QPushButton("Options", self)
        self.options_button.setGeometry(80, 100, 100, 30)
        self.options_button.clicked.connect(self.aim_options)
        self.setFixedHeight(250)
        self.setFixedWidth(250)

        self.exit_button = QPushButton("Exit", self)
        self.exit_button.setGeometry(80, 150, 100, 30)
        self.exit_button.clicked.connect(self.aim_exit)
        self.setFixedHeight(250)
        self.setFixedWidth(250)

    def aim_start(self):
        print("start")

    def aim_options(self):
        self.close()
        self.options_window = AimOptions.Options()
        self.options_window.show()
        self.close()


    def aim_exit(self):
        sys.exit()


if __name__ == "__main__":
    app = QtWidgets.QApplication([])

    aim_menu = Menu()

    aim_menu.resize(800, 600)
    aim_menu.show()

    sys.exit(app.exec())
