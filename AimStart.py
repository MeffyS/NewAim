import sys



from PySide6 import QtWidgets
from PySide6.QtWidgets import QPushButton
from PySide6.QtGui import QIcon


import AimPlay
import AimIntroduction

class Lobby(QtWidgets.QWidget):
    def __init__(self,save):
        super().__init__()
        self.save = save
        print('save',save)

        self.setGeometry(100, 100, 1200, 1200)

        self.setWindowTitle("Aim Game")
        self.setWindowIcon(QIcon("Aim_icons\icon_aim.png"))
        self.setFixedHeight(600)
        self.setFixedWidth(600)

        self.play_button = QPushButton("PLAY", self)
        self.play_button.setGeometry(50, 200, 200, 100)
        self.play_button.clicked.connect(self.aim_play)

        self.introduction_button = QPushButton("INTRODUCTION", self)
        self.introduction_button.setGeometry(350, 200, 200, 100)
        self.introduction_button.clicked.connect(self.aim_introduction)

        self.setStyleSheet("background-color: #135440")

        self.play_button.setStyleSheet(
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

        self.introduction_button.setStyleSheet(
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
    
    def aim_play(self):
        self.play = AimPlay.Play(self.save)
        self.play.show()
        self.close()
        

    def aim_introduction(self):
        self.close()
        self.aim_introduction = AimIntroduction.Introduction()
        self.aim_introduction.show()


if __name__ == "__main__":
    app = QtWidgets.QApplication([])

    aim_lobby = Lobby('')

    aim_lobby.resize(800, 600)
    aim_lobby.show()

    sys.exit(app.exec())
