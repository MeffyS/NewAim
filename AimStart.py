import sys
import time
import os

import PySide2
import PySide6
import AimOptions

from PySide6 import QtWidgets
from PySide6.QtWidgets import QPushButton, QLabel, QTabBar
from PySide6.QtGui import QCursor, QIcon
from PySide6.QtWidgets import QWidget


class Lobby(QtWidgets.QWidget):
    def __init__(self, save):
        super().__init__()

        self.setGeometry(100, 100, 1200, 1200)

        self.setWindowTitle("Aim Game")
        self.setWindowIcon(QIcon("Aim_icons\icon_aim.png"))
        self.setFixedHeight(600)
        self.setFixedWidth(600)

        self.play_button = QPushButton("PLAY", self)
        self.play_button.setGeometry(50, 200, 200, 100)

        self.introduction_button = QPushButton("INTRODUCTION", self)
        self.introduction_button.setGeometry(350, 200, 200, 100)

        self.play_button.setStyleSheet(
            """
            QPushButton {
                color: #008000; 
                background-color: #272727;
                border: 2px solid white;
                border-radius: 20px;
                font-size: 25px;

            }
            QPushButton:hover {
                color: #00DD00;
            }
        """
        )

        self.introduction_button.setStyleSheet(
            """
            QPushButton{
                color: #008000;
                background-color: #272727;
                border: 2px solid white;
                border-radius: 20px;
                font-size: 25px;
            }
            QPushButton:hover{
                color: #00DD00;

            }
            """
        )
        self.setStyleSheet("background-color: #000000;")


if __name__ == "__main__":
    app = QtWidgets.QApplication([])

    aim_lobby = Lobby("")

    aim_lobby.resize(800, 600)
    aim_lobby.show()

    sys.exit(app.exec())
