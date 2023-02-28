import sys

import AimMenu

from PySide6 import QtWidgets
from PySide6.QtWidgets import QPushButton, QSlider, QLabel, QColorDialog, QLineEdit
from PySide6.QtGui import QCursor, QIcon, Qt, QColor

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

        self.username_label = QLabel("Choose username", self)
        self.username_label.setGeometry(300, 108, 100, 10)

        self.username_color_warning_label = QLabel("", self)
        self.username_color_warning_label.setGeometry(125, 20, 300, 20)

        self.username_qline = QLineEdit(self)
        self.username_qline.setGeometry(400, 104, 100, 20)

        self.username_button = QPushButton("Enter username", self)
        self.username_button.setGeometry(500, 104, 100, 20)
        self.username_button.clicked.connect(self.change_username)

        self.username = QLabel(f"", self)
        self.username.setGeometry(50, 50, 100, 20)

        self.music_label = QLabel("Music", self)
        self.music_label.setGeometry(430, 48, 100, 10)

        self.music = QSlider(Qt.Orientation.Horizontal, self)
        self.music.setGeometry(470, 50, 100, 10)
        self.music.setValue(50)
        self.music.valueChanged.connect(self.music_value)
        

        self.music_number_label = QLabel("50", self)
        self.music_number_label.setGeometry(575, 45, 100, 10)
        

        self.sound_label = QLabel("Sound", self)
        self.sound_label.setGeometry(430, 76, 100, 10)

        self.sound = QSlider(Qt.Orientation.Horizontal, self)
        self.sound.setGeometry(470, 78, 100, 10)
        self.sound.setValue(50)
        self.sound.valueChanged.connect(self.sound_value)
        

        self.sound_number_label = QLabel("50", self)
        self.sound_number_label.setGeometry(575, 75, 100, 10)

        self.color = QPushButton("Username Color", self)
        self.color.setGeometry(20, 20, 100, 20)
        self.color.clicked.connect(self.choose_color)

    def back_to_menu(self):
        user = self.username.text()
        save = {'username':user}

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
