import sys

import AimMenu

from PySide6 import QtWidgets
from PySide6.QtWidgets import (
    QPushButton,
    QSlider,
    QLabel,
    QColorDialog,
    QLineEdit,
    QFrame,
)
from PySide6 import QtCore
from PySide6.QtGui import QCursor, QIcon, Qt, QColor

import AimPlay


class Options(QtWidgets.QTabWidget):
    def __init__(self, save):
        super().__init__()
        self.save = save
        # print(self.save['game_options'])
        

        self.setFixedHeight(600)
        self.setFixedWidth(600)

        self.setGeometry(100, 100, 1200, 1200)
        self.setWindowTitle("Options")
        self.setWindowIcon(QIcon("Aim_icons\settings.png"))
        self.setStyleSheet("background-color: #135440")

        self.audio_options()
        self.user_options()
        self.difficulty_options()

        self.save_button = QPushButton("Save", self)
        self.save_button.setGeometry(390, 540, 200, 50)
        self.save_button.clicked.connect(self.back_to_menu)

        self.save_button.setStyleSheet(
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

    def user_options(self):

        self.user_label = QLabel("User", self)
        self.user_label.setGeometry(2, 78, 80, 30)
        self.user_label.setStyleSheet(
            "font-size: 25px; font-weight: bold; color: #ffffff; border: 3px solid #61c7a2; border-bottom-right-radius: 10px; border-bottom-left-radius: 10px; background-color: #70e5ba;"
        )
        self.user_label.setAlignment(QtCore.Qt.AlignCenter)

        self.username_label = QLabel("Choose Username", self)
        self.username_label.setGeometry(250, 140, 130, 40)

        self.username_color_warning_label = QLabel("", self)
        self.username_color_warning_label.setGeometry(125, 50, 280, 20)

        self.username_qline = QLineEdit(self)
        self.username_qline.setGeometry(400, 140, 130, 40)

        self.username_warning = QLabel(f"", self)
        self.username_warning.setGeometry(250, 80, 200, 20)

        self.username_accept = QPushButton(f"OK", self)
        self.username_accept.setGeometry(550, 140, 40, 40)
        self.username_accept.clicked.connect(self.accept_username)

        self.color = QPushButton("Username Color", self)
        self.color.setGeometry(100, 140, 140, 40)
        self.color.clicked.connect(self.choose_color)

        self.color.setStyleSheet(
            """
            QPushButton {
                color: #75a154; 
                background-color: #2a6b48;
                border: 2px solid #45814e;
                border-radius: 20px;
                font-size: 15px;
            
            }            
            QPushButton:hover {
                color: #9ab657;
            }
            """
        )

        self.username_label.setStyleSheet(
            """
            QLabel {
                color: #75a154; 
                background-color: #2a6b48;
                border: 2px solid #45814e;
                border-radius: 20px;
                font-size: 15px;

            }

            """
        )

        self.username_qline.setStyleSheet(
            """
            QLineEdit {
                color: #75a154; 
                background-color: #2a6b48;
                border: 2px solid #45814e;
                border-radius: 20px;
                font-size: 15px;
                font-weight: bold;

            }

            """
        )

        self.username_accept.setStyleSheet(
            """
            QPushButton {
                color: #75a154; 
                background-color: #2a6b48;
                border: 2px solid #45814e;
                border-radius: 20px;
                font-size: 15px;
            
            }            
            QPushButton:hover {
                color: #9ab657;
            }
            """
        )
        self.user_down_line = QFrame(self)
        self.user_down_line.setFrameShape(QFrame.HLine)
        self.user_down_line.setFrameShadow(QFrame.Sunken)
        self.user_down_line.setGeometry(2, 70, 594, 10)
        self.user_down_line.setLineWidth(4)
        self.user_down_line.setStyleSheet("background-color: #61c7a2")

        try:
            if self.save["game_options"] == "GAME":
                self.username_label.setText(self.save["username_set"])
                print(self.save["hearts"])
        except Exception:
            print("x")
        #     try:
        #         self.username_label.setText(self.save['username_set'])
        #     except Exception:
        #         self.username_label.setText(self.save['username_not_set'])

        # else:
        #     print("ERROR")

    def audio_options(self):

        self.audio_label = QLabel("Audio", self)
        self.audio_label.setGeometry(2, 10, 90, 30)
        self.audio_label.setStyleSheet(
            "font-size: 25px; font-weight: bold; background-color: #70e5ba; color: #ffffff; border: 3px solid #61c7a2; border-bottom-right-radius: 10px; border-bottom-left-radius: 10px;"
        )
        self.audio_label.setAlignment(QtCore.Qt.AlignCenter)

        self.music_label = QLabel("Music", self)
        self.music_label.setGeometry(415, 34, 100, 20)
        self.music_label.setStyleSheet("font-size: 15px; color: #75a154; ")

        self.music = QSlider(Qt.Orientation.Horizontal, self)
        self.music.setGeometry(460, 40, 100, 10)
        self.music.setValue(50)
        self.music.valueChanged.connect(self.music_value)
        self.music.setStyleSheet(
            "QSlider::groove:horizontal { background: #82cc9f;} QSlider::handle:horizontal { background: #eae4ca; width:10px;}"
        )

        self.music_number_label = QLabel("50", self)
        self.music_number_label.setGeometry(565, 34, 25, 20)
        self.music_number_label.setStyleSheet(
            "font-size: 15px; color: #75a154; text-align:right;"
        )

        self.sound_label = QLabel("Sound", self)
        self.sound_label.setGeometry(415, 14, 100, 20)
        self.sound_label.setStyleSheet("font-size: 15px; color: #75a154; ")

        self.sound = QSlider(Qt.Orientation.Horizontal, self)
        self.sound.setGeometry(460, 20, 100, 10)
        self.sound.setValue(50)
        self.sound.valueChanged.connect(self.sound_value)
        self.sound.setStyleSheet(
            "QSlider::groove:horizontal { background: #82cc9f;} QSlider::handle:horizontal { background: #eae4ca; width:10px;}"
        )

        self.sound_number_label = QLabel("50", self)
        self.sound_number_label.setGeometry(565, 14, 25, 20)
        self.sound_number_label.setStyleSheet(
            "font-size: 15px; color: #75a154; text-align:right;"
        )

        self.audio_up_line = QFrame(self)
        self.audio_up_line.setFrameShape(QFrame.HLine)
        self.audio_up_line.setFrameShadow(QFrame.Sunken)
        self.audio_up_line.setGeometry(2, 2, 594, 10)
        self.audio_up_line.setLineWidth(4)
        self.audio_up_line.setStyleSheet("background-color: #61c7a2")

    def difficulty_options(self):

        self.difficulty_label = QLabel("Difficulty", self)
        self.difficulty_label.setGeometry(2, 218, 130, 35)
        self.difficulty_label.setAlignment(QtCore.Qt.AlignCenter)
        self.difficulty_label.setStyleSheet(
            "font-size: 25px; font-weight: bold; color: #ffffff; border: 3px solid #61c7a2; border-bottom-right-radius: 10px; border-bottom-left-radius: 10px; background-color: #70e5ba;"
        )

        self.choosed_difficulty_label = QLabel("Medium", self)
        self.choosed_difficulty_label.setGeometry(129, 218, 130, 35)
        self.choosed_difficulty_label.setAlignment(QtCore.Qt.AlignCenter)
        self.choosed_difficulty_label.setStyleSheet(
            "font-size: 25px; font-weight: bold; color: #ffffff; border: 3px solid #61c7a2; border-bottom-right-radius: 10px; border-bottom-left-radius: 10px; background-color: #70e5ba;"
        )

        self.easy_difficulty = QPushButton("Easy", self)
        self.easy_difficulty.setGeometry(100, 298, 130, 45)
        self.easy_difficulty.clicked.connect(self.set_difficulty)

        self.medium_difficulty = QPushButton("Medium", self)
        self.medium_difficulty.setGeometry(250, 298, 130, 45)
        self.medium_difficulty.clicked.connect(self.set_difficulty)

        self.hard_difficulty = QPushButton("Hard", self)
        self.hard_difficulty.setGeometry(400, 298, 130, 45)
        self.hard_difficulty.clicked.connect(self.set_difficulty)
        self.difficulty_down_line = QFrame(self)

        self.difficulty_down_line.setFrameShape(QFrame.HLine)
        self.difficulty_down_line.setFrameShadow(QFrame.Sunken)
        self.difficulty_down_line.setGeometry(2, 210, 594, 10)
        self.difficulty_down_line.setLineWidth(4)
        self.difficulty_down_line.setStyleSheet("background-color: #61c7a2")

        self.easy_difficulty.setStyleSheet(
            """
            QPushButton {
                color: #aae566; 
                background-color: #2a6b48;
                border: 2px solid #45814e;
                border-radius: 20px;
                font-size: 15px;
                font-weight: bold;

            }
            QPushButton:hover {
                color: #9ab657;

            }

            """
        )
        self.medium_difficulty.setStyleSheet(
            """
            QPushButton {
                color: #f6ff66; 
                background-color: #2a6b48;
                border: 2px solid #45814e;
                border-radius: 20px;
                font-size: 15px;
                font-weight: bold;

            }
            QPushButton:hover {
                color: #9ab657;

            }

            """
        )
        self.hard_difficulty.setStyleSheet(
            """
            QPushButton {
                color: #ff5c58; 
                background-color: #2a6b48;
                border: 2px solid #45814e;
                border-radius: 20px;
                font-size: 15px;
                font-weight: bold;

            }
            QPushButton:hover {
                color: #9ab657;

            }


            """
        )

    def set_difficulty(self):

        sender = self.sender()
        if sender.text() == "Easy":
            print("Easy")

            print(self.choosed_difficulty_label.styleSheet())

            self.choosed_difficulty_label.setText("Easy")

            print(self.choosed_difficulty_label.styleSheet())

        elif sender.text() == "Medium":
            self.choosed_difficulty_label.setText("Medium")
        elif sender.text() == "Hard":
            self.choosed_difficulty_label.setText("Hard")

    def back_to_menu(self):
        self.start_game = True
        user = self.username_label.text()

        if self.start_game is True:
            print(self.start_game)
            self.start_game = False
            save = {"username": user.capitalize()}
            self.menu_back = AimMenu.Menu(save)
            self.menu_back.show()
            self.close()

        if self.save["username"] == self.username_label.text():
            self.menu_back.close()
            self.play_back = AimPlay.Play(self.save)
            self.play_back.show()
            
            self.close()

        try:
            if self.save["username"] != self.username_label.text():
                self.menu_back.close()
                self.save["username"] = self.username_label.text()
                if self.save["game_options"] == "GAME":
                    self.save["game_options"] == "PLAY"
                    self.save["username"] = self.username_label.text()
                    self.play_back = AimPlay.Play(self.save)
                    self.play_back.show()
                    self.close()
        except Exception:
            print('Player username doesn\'t exist yet')
        
        
        

        if self.username_label.text() in ("Choose Username", ""):
            self.username_warning.setText("You must enter username!")
            self.username_warning.setStyleSheet("color: #ff5c58;")



    def choose_color(self):
        color_v_counter = 0
        self.color = QColorDialog.getColor()

        # self.username_warning.setStyleSheet(
        #     f"color: rgb({QColor.getRgb(self.color)[0]}, {QColor.getRgb(self.color)[1]}, {QColor.getRgb(self.color)[2]})"
        # )

        # for color_v in list(QColor.getRgb(self.color)):
        #     print(color_v)
        #     if color_v_counter < 3:
        #         if color_v > 220:
        #             color_v_counter += 1
        #             continue
        #     if color_v_counter == 3:
        #         self.username_warning.setStyleSheet(f"color: rgb({0}, {0}, {0})")
        #         self.username_color_warning_label.setText(
        #             "Your color cannot be in white hue"
        #         )
        #         self.username_color_warning_label.setStyleSheet(
        #             f"color: rgb({255}, {0}, {0})"
        #         )
        #     else:
        #         self.username_color_warning_label.setStyleSheet(
        #             f"color: rgb({255}, {255}, {255})"
        #         )

    def music_value(self):
        self.music_number_label.setText(str(self.music.value() + 1))

    def sound_value(self):
        self.sound_number_label.setText(str(self.sound.value() + 1))

    def accept_username(self):
        if (
            self.username_qline.text() not in ("Choose Username", "")
            and len(self.username_qline.text()) <= 16
            and len(self.username_qline.text()) > 0
        ):
            self.username_label.setText(self.username_qline.text())
            self.username_warning.setText("")
        elif len(self.username_label.text()) > 16:
            self.username_warning.setText("Entered cannot be higher than 16")
            self.username_warning.setStyleSheet("color: #ff5c58;")
        else:
            self.username_warning.setText("Entered name cannot be blank")
            self.username_warning.setStyleSheet("color: #ff5c58;")


if __name__ == "__main__":
    app = QtWidgets.QApplication([])

    aim_options = Options("")
    aim_options.show()

    sys.exit(app.exec())
