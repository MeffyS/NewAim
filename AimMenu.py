import sys
import time
import os


import AimOptions
import AimStart

from PySide6 import QtWidgets
from PySide6.QtWidgets import QPushButton, QLabel
from PySide6.QtGui import QCursor, QIcon
from PySide6.QtCore import Qt 


class Menu(QtWidgets.QWidget):
    def __init__(self, save):
        super().__init__()
        self.save = save

        self.setFixedHeight(600)
        self.setFixedWidth(600)

        try:
            self.welcome_label = QLabel(
                f'WELCOME {save["username"]} IN AIM TRAINING', self
            )

        except Exception:
            self.welcome_label = QLabel(
                f"WELCOME {os.getlogin()} IN AIM TRAINING", self
            )

        self.welcome_label.setGeometry(100, 20, 450, 50)
        self.welcome_label.setAlignment(Qt.AlignCenter)

        self.setGeometry(100, 100, 1200, 1200)
        self.setWindowTitle("Aim menu")
        self.setWindowIcon(QIcon("Aim_icons\click.png"))

        self.start_button = QPushButton("Start Aim", self)
        self.start_button.setGeometry(210, 120, 200, 100)
        self.start_button.clicked.connect(self.aim_start)

        self.options_button = QPushButton("Options", self)
        self.options_button.setGeometry(210, 260, 200, 100)
        self.options_button.clicked.connect(self.aim_options)

        self.exit_button = QPushButton("Exit", self)
        self.exit_button.setGeometry(210, 400, 200, 100)
        self.exit_button.clicked.connect(self.aim_exit)

        self.setStyleSheet("background-color: #135440")

        self.start_button.setStyleSheet(
            """
            QPushButton {
                color: #75a154; 
                background-color: #2a6b48;
                border: 2px solid #45814e;
                border-radius: 20px;
                font-size: 25px;

            }
            QPushButton:hover {
                color: #9ab657;
            }
        """
        )

        self.options_button.setStyleSheet(
            """
            QPushButton {
                color: #75a154; 
                background-color: #2a6b48;
                border: 2px solid #45814e;
                border-radius: 20px;
                font-size: 25px;

            }
            QPushButton:hover {
                color: #9ab657;
            }
        """
        )

        self.exit_button.setStyleSheet(
            """
            QPushButton {
                color: #75a154; 
                background-color: #2a6b48;
                border: 2px solid #45814e;
                border-radius: 20px;
                font-size: 25px;

            }
            QPushButton:hover {
                color: #9ab657;
            }
        """
        )

        self.welcome_label.setStyleSheet(
            """
            QLabel {
                color: #9ab657; 
                background-color: #0e4232;
                border: 2px solid #45814e;
                border-radius: 20px;
                font-size: 20px;
                

            }
    
        """
        )

    def aim_start(self,save):
        self.close()
        self.aim_start = AimStart.Lobby(self.save)
        self.aim_start.show()

    def aim_options(self):
        self.close()
        self.options_window = AimOptions.Options('')
        self.options_window.show()
        self.close()

    def aim_exit(self):
        sys.exit()


if __name__ == "__main__":
    app = QtWidgets.QApplication([])

    aim_menu = Menu("")

    aim_menu.resize(800, 600)
    aim_menu.show()

    sys.exit(app.exec())
