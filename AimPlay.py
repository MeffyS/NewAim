import PySide2
import PySide6
import sys
import random
import time


from PySide6.QtCore import QUrl
from PySide6.QtMultimedia import QSoundEffect

from PySide6.QtCore import QTimer, Slot, QDateTime, QElapsedTimer
from PySide6 import QtWidgets, QtMultimedia
from PySide6.QtWidgets import QApplication, QPushButton, QLabel
from PySide6.QtGui import QPixmap, QCursor

from abc import ABC
import AimLevels


class Play(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        self.hearts()
        self.setFixedSize(1280, 800)
        # self.setCursor(QCursor(ClosedHandCursor))

        self.aim_seconds = 0
        self.points = 0
        self.hit_points_value = 0
        self.miss_points_value = 0

        self.aim_timer_seconds = QLabel("0", self)
        self.aim_timer_seconds.setGeometry(145, 15, 300, 25)
        self.aim_timer_seconds.setStyleSheet("font-size: 25px;")

        self.aim_username = QLabel("Username", self)
        self.aim_username.setGeometry(15, 15, 300, 25)
        self.aim_username.setStyleSheet("font-size: 25px;")

        self.aim_level = QLabel("0", self)
        self.aim_level.setGeometry(245, 15, 300, 25)
        self.aim_level.setStyleSheet("font-size: 25px;")

        self.aim_points = QLabel(f"Points: {self.points}", self)
        self.aim_points.setGeometry(525, 15, 300, 25)
        self.aim_points.setStyleSheet("font-size: 25px;")

        self.hit_object_label = QLabel(f"Hit: {self.hit_points_value}", self)
        self.hit_object_label.setGeometry(1000, 15, 300, 25)
        self.hit_object_label.setStyleSheet("font-size: 25px;")

        self.miss_object_label = QLabel(f"Miss: {self.miss_points_value}", self)
        self.miss_object_label.setGeometry(1100, 15, 300, 25)
        self.miss_object_label.setStyleSheet("font-size: 25px;")

        self.obj_first = AimObject(100, 100, 200, 200, "obj_1", 5)

        self.hit_effect = QSoundEffect(self)
        self.hit_effect.setSource(QUrl.fromLocalFile("Aim_audio/punch.wav"))

        self.fail_effect = QSoundEffect(self)
        self.fail_effect.setSource(QUrl.fromLocalFile("Aim_audio/fail_sound.wav"))

        self.obj_first.setGeometry(
            self.obj_first.position_x,
            self.obj_first.position_y,
            self.obj_first.o_width,
            self.obj_first.o_height,
        )

        self.obj_first.setParent(self)

        self.obj_first.clicked.connect(self.clicked_button_change_position)

        self.timer = QTimer(self)
        self.timer.timeout.connect(self.no_clicked_button_change_position)
        self.timer.start(3000)

        self.game_time = QTimer(self)
        self.game_time.timeout.connect(self.update_time_label)
        self.game_time.start(100)

        self.elapsed_timer = QElapsedTimer()
        self.elapsed_timer.start()
        self.start_time = QDateTime.currentDateTime()

    def no_clicked_button_change_position(self):
        self.fail_effect.play()
        self.remove_points()
        self.miss_points()

        self.new_position_x = random.randint(20, 600)
        self.new_position_y = random.randint(20, 600)
        self.obj_first.setGeometry(
            self.new_position_x,
            self.new_position_y,
            self.obj_first.o_width,
            self.obj_first.o_height,
        )

    def clicked_button_change_position(self):
        self.hit_effect.play()
        self.add_points()
        self.hit_points()

        self.new_position_x = random.randint(20, 600)
        self.new_position_y = random.randint(20, 600)
        self.obj_first.setGeometry(
            self.new_position_x,
            self.new_position_y,
            self.obj_first.o_width,
            self.obj_first.o_height,
        )
        

    def update_time_label(self):

        main_game_time = self.start_time.secsTo(QDateTime.currentDateTime())
        main_game_mins = main_game_time // 60
        main_game_secs = main_game_time % 60
        main_game_hours = main_game_mins // 60
        main_game_mins %= 60
        self.aim_timer_seconds.setText(
            f"{main_game_hours:02d}:{main_game_mins:02d}:{main_game_secs:02d}"
        )

    def hearts(self):
        hearts_list = ["Heart_1", "Heart_2", "Heart_3", "Heart_4"]
        for position, heart in enumerate(hearts_list):
            self.heart_label = QLabel("", self)
            self.heart_label.setGeometry(350 + 40 * position, -10, 80, 80)
            self.heart_label_pixmap = QPixmap("Aim_icons/heart.png")
            self.heart_label_pixmap = self.heart_label_pixmap.scaled(40, 40)
            self.heart_label.setPixmap(self.heart_label_pixmap)
            setattr(self, heart, self.heart_label)

    def add_points(self):
        self.timer.start(10000)
        self.points += 1
        self.aim_points.setText(f"Points: {self.points}")
        self.new_level = AimLevels.points_checker(self.points)
        self.aim_level.setText(str(self.new_level.level))
        self.timer.start(self.new_level.change_speed)

    def remove_points(self):
        self.points -= 1
        self.aim_points.setText(f"Points: {self.points}")
        self.new_level = AimLevels.points_checker(self.points)
        self.aim_level.setText(str(self.new_level.level))

    def hit_points(self):
        self.hit_points_value += 1
        self.hit_object_label.setText(f"Hit: {self.hit_points_value}")

    def miss_points(self):
        self.miss_points_value += 1
        self.miss_object_label.setText(f"Miss: {self.miss_points_value}")


class AimObject(QtWidgets.QPushButton):
    def __init__(self, position_x, position_y, o_width, o_height, name, seconds):
        super().__init__()
        self.position_x = position_x
        self.position_y = position_y
        self.o_width = o_width
        self.o_height = o_height
        self.name = name
        self.timer = seconds


if __name__ == "__main__":

    app = QtWidgets.QApplication([])

    aim_play = Play()
    aim_play.show()

    sys.exit(app.exec())
