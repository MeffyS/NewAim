import PySide2
import PySide6
import sys
import random
import time

from abc import ABC

from PySide6.QtCore import QTimer, Slot, QDateTime, QElapsedTimer

from PySide6 import QtWidgets
from PySide6.QtWidgets import QApplication, QPushButton, QLabel
from PySide6.QtGui import QPixmap


class Play(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        self.hearts()

        self.aim_seconds = 0

        self.aim_timer_seconds = QLabel("0", self)
        self.aim_timer_seconds.setGeometry(145, 15, 300, 25)
        self.aim_timer_seconds.setStyleSheet("font-size: 25px;")

        self.aim_username = QLabel("Username", self)
        self.aim_username.setGeometry(15, 15, 300, 25)
        self.aim_username.setStyleSheet("font-size: 25px;")

        self.aim_level = QLabel(f"Level: 0", self)
        self.aim_level.setGeometry(245, 15, 300, 25)
        self.aim_level.setStyleSheet("font-size: 25px;")

        self.setFixedSize(1280, 800)

        self.obj_first = AimObject(100, 100, 50, 50, "obj_1", 5)

        self.obj_first.setGeometry(
            self.obj_first.position_x,
            self.obj_first.position_y,
            self.obj_first.o_width,
            self.obj_first.o_height,
        )

        self.obj_first.setParent(self)

        self.obj_first.clicked.connect(self.button_change_position)

        self.timer = QTimer(self)
        self.timer.timeout.connect(self.button_change_position)
        self.timer.start(3000)

        self.game_time = QTimer(self)
        self.game_time.timeout.connect(self.update_time_label)
        self.game_time.start(100)

        self.elapsed_timer = QElapsedTimer()
        self.elapsed_timer.start()
        self.start_time = QDateTime.currentDateTime()

    def button_change_position(self):

        self.new_position_x = random.randint(20, 600)
        self.new_position_y = random.randint(20, 600)
        self.obj_first.setGeometry(
            self.new_position_x,
            self.new_position_y,
            self.obj_first.o_width,
            self.obj_first.o_height,
        )
        self.timer.start(3000)

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
            # print(f'pos_x {position * 20} pos_y {position} h {heart}')
            self.heart_label = QLabel('',self)
            self.heart_label.setGeometry(350 + 40*position, -10, 80, 80)
            self.heart_label_pixmap = QPixmap('Aim_icons/heart.png')
            self.heart_label_pixmap = self.heart_label_pixmap.scaled(40,40)
            self.heart_label.setPixmap(self.heart_label_pixmap)
            setattr(self, heart, self.heart_label)
            

            # self.heart_label = QLabel('')
            # self.heart_label.setGeometry(225,440,25,25)
            # self.heart_label_pixmap = QPixmap('Aim_icons/heart.png')
            # self.heart_label_pixmap = self.heart_label_pixmap.scaled(22,22)
            # self.heart_label.setPixmap(self.heart_label_pixmap)


class AimObject(QtWidgets.QPushButton):
    def __init__(self, position_x, position_y, o_width, o_height, name, seconds):
        super().__init__()
        self.position_x = position_x
        self.position_y = position_y
        self.o_width = o_width
        self.o_height = o_height
        self.name = name
        self.timer = seconds


class AimLevel(ABC):
    def __init__(
        self,
        level=1,
        money=0,
        min_points=0,
        max_points=25,
        change_speed=10,
        hearts=4,
        points_counter=1,
    ):
        self.level = level
        self.money = money
        self.min_points = min_points
        self.max_points = max_points
        self.change_speed = change_speed
        self.hearts = hearts
        self.points_counter = points_counter

    def money_converter(self):
        pass

    def count_points(self):
        pass


class Level_1(AimLevel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def money_converter(self):
        return (self.level + 0) * 1.5

    def count_points(self):
        return (self.level + self.min_points) + 10


if __name__ == "__main__":

    app = QtWidgets.QApplication([])

    aim_play = Play()
    aim_play.show()

    sys.exit(app.exec())
