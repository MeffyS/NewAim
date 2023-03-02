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


class Options(QtWidgets.QTabWidget):
    def __init__(self):
        super().__init__()

        self.setFixedHeight(600)
        self.setFixedWidth(600)

        self.setGeometry(100, 100, 1200, 1200)
        self.setWindowTitle("Options")
        self.setWindowIcon(QIcon("Aim_icons\settings.png"))
        self.audio_options()
        self.user_options()

        self.save_button = QPushButton("Save", self)
        self.save_button.setGeometry(390, 540, 200, 50)
        self.save_button.clicked.connect(self.back_to_menu)

        self.username_label = QLabel("Choose username", self)
        self.username_label.setGeometry(300, 308, 100, 10)

        self.username_color_warning_label = QLabel("", self)
        self.username_color_warning_label.setGeometry(125, 50, 300, 20)

        self.username_qline = QLineEdit(self)
        self.username_qline.setGeometry(400, 304, 100, 20)

        self.username_button = QPushButton("Enter username", self)
        self.username_button.setGeometry(210, 520, 200, 50)
        self.username_button.clicked.connect(self.change_username)

        self.username = QLabel(f"", self)
        self.username.setGeometry(50, 50, 100, 20)

        self.color = QPushButton("Username Color", self)
        self.color.setGeometry(20, 200, 100, 20)
        self.color.clicked.connect(self.choose_color)

        self.username_button.setStyleSheet(
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
        self.user_label.setGeometry(260, 78, 80, 30)
        self.user_label.setStyleSheet(
            "font-size: 25px; font-weight: bold; background-color: #70e5ba; color: #ffffff; border: 3px solid #61c7a2; border-radius: 10px;"
        )
        self.user_label.setAlignment(QtCore.Qt.AlignCenter)


        self.user_down_line = QFrame(self)
        self.user_down_line.setFrameShape(QFrame.HLine)
        self.user_down_line.setFrameShadow(QFrame.Sunken)
        self.user_down_line.setGeometry(2, 70, 594, 10)
        self.user_down_line.setLineWidth(4)
        self.user_down_line.setStyleSheet("background-color: #61c7a2")
        self.setStyleSheet("background-color: #135440")


    def audio_options(self):

        self.audio_label = QLabel("Audio", self)
        self.audio_label.setGeometry(260, 10, 80, 30)
        self.audio_label.setStyleSheet(
            "font-size: 25px; font-weight: bold; background-color: #70e5ba; color: #ffffff; border: 3px solid #61c7a2; border-radius: 10px;"
        )
        self.audio_label.setAlignment(QtCore.Qt.AlignCenter)

        self.music_label = QLabel("Music", self)
        self.music_label.setGeometry(18, 26, 100, 20)
        self.music_label.setStyleSheet("font-size: 15px; color: #75a154; ")

        self.music = QSlider(Qt.Orientation.Horizontal, self)
        self.music.setGeometry(60, 30, 100, 10)
        self.music.setValue(50)
        self.music.valueChanged.connect(self.music_value)
        self.music.setStyleSheet(
            "QSlider::groove:horizontal { background: #82cc9f;} QSlider::handle:horizontal { background: #eae4ca; width:10px;}"
        )

        self.music_number_label = QLabel("50", self)
        self.music_number_label.setGeometry(165, 24, 25, 20)
        self.music_number_label.setStyleSheet(
            "font-size: 15px; color: #75a154; text-align:right;"
        )

        self.sound_label = QLabel("Sound", self)
        self.sound_label.setGeometry(415, 24, 100, 20)
        self.sound_label.setStyleSheet("font-size: 15px; color: #75a154; ")

        self.sound = QSlider(Qt.Orientation.Horizontal, self)
        self.sound.setGeometry(460, 30, 100, 10)
        self.sound.setValue(50)
        self.sound.valueChanged.connect(self.sound_value)
        self.sound.setStyleSheet(
            "QSlider::groove:horizontal { background: #82cc9f;} QSlider::handle:horizontal { background: #eae4ca; width:10px;}"
        )

        self.sound_number_label = QLabel("50", self)
        self.sound_number_label.setGeometry(565, 24, 25, 20)
        self.sound_number_label.setStyleSheet(
            "font-size: 15px; color: #75a154; text-align:right;"
        )


        self.audio_up_line = QFrame(self)
        self.audio_up_line.setFrameShape(QFrame.HLine)
        self.audio_up_line.setFrameShadow(QFrame.Sunken)
        self.audio_up_line.setGeometry(2, 2, 594, 10)
        self.audio_up_line.setLineWidth(4)
        self.audio_up_line.setStyleSheet("background-color: #61c7a2")
        self.setStyleSheet("background-color: #135440")

    def back_to_menu(self):
        user = self.username.text()
        save = {"username": user}

        self.menu_back = AimMenu.Menu(save)
        self.menu_back.show()
        self.close()

    def choose_color(self):
        color_v_counter = 0
        self.color = QColorDialog.getColor()

        self.username.setStyleSheet(
            f"color: rgb({QColor.getRgb(self.color)[0]}, {QColor.getRgb(self.color)[1]}, {QColor.getRgb(self.color)[2]})"
        )
        for color_v in list(QColor.getRgb(self.color)):
            print(color_v)
            if color_v_counter < 3:
                if color_v > 220:
                    color_v_counter += 1
                    continue
            if color_v_counter == 3:
                self.username.setStyleSheet(f"color: rgb({0}, {0}, {0})")
                self.username_color_warning_label.setText(
                    "Your color cannot be in white hue"
                )
                self.username_color_warning_label.setStyleSheet(
                    f"color: rgb({255}, {0}, {0})"
                )
            else:
                self.username_color_warning_label.setStyleSheet(
                    f"color: rgb({255}, {255}, {255})"
                )

    def music_value(self):
        self.music_number_label.setText(str(self.music.value() + 1))

    def sound_value(self):
        self.sound_number_label.setText(str(self.sound.value() + 1))

    def change_username(self):
        new_username = self.username_qline.text()
        self.username.setText(new_username)


if __name__ == "__main__":
    app = QtWidgets.QApplication([])

    aim_options = Options()
    aim_options.show()

    sys.exit(app.exec())
