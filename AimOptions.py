import PySide2
import PySide6
from PySide6 import QtWidgets
from PySide6.QtWidgets import QPushButton, QSlider, QLabel, QColorDialog
from PySide6.QtGui import QCursor, QIcon, Qt
import sys
import time
import AimMenu


class Options(QtWidgets.QTabWidget):
    def __init__(self):
        super().__init__()

        self.setGeometry(100, 100, 1200, 1200)
        self.setWindowTitle("Options")
        self.setWindowIcon(QIcon("Aim_icons\settings.png"))

        self.save_button = QPushButton("Save", self)
        self.save_button.setGeometry(470, 550, 100, 30)
        self.setFixedHeight(600)
        self.setFixedWidth(600)
        self.save_button.clicked.connect(self.back_to_menu)

        self.music_label = QLabel("Music", self)
        self.music_label.setGeometry(430, 48, 100, 10)

        self.music = QSlider(Qt.Orientation.Horizontal, self)
        self.music.setGeometry(470, 50, 100, 10)

        self.sound_label = QLabel("Sound", self)
        self.sound_label.setGeometry(430, 76, 100, 10)

        self.sound = QSlider(Qt.Orientation.Horizontal, self)
        self.sound.setGeometry(470, 78, 100, 10)

        self.color = QPushButton("Username Color", self)
        # self.color.setGeometry(100, 108, 100, 10)
        self.color.clicked.connect(self.choose_color)

    def back_to_menu(self):

        self.menu_back = AimMenu.Menu()
        self.menu_back.show()
        self.close()

    def choose_color(self):
        self.color = QColorDialog.getColor()


if __name__ == "__main__":
    app = QtWidgets.QApplication([])

    aim_options = Options()
    aim_options.show()

    sys.exit(app.exec())
