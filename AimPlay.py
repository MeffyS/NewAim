import sys
import random
import os


from PySide6.QtCore import QUrl
from PySide6.QtMultimedia import QSoundEffect

from PySide6.QtCore import QTimer, QDateTime, QElapsedTimer, Qt
from PySide6 import QtWidgets
from PySide6.QtWidgets import QLabel, QFrame
from PySide6.QtGui import QPixmap
from PySide6.QtTest import QTest


import AimLevels


class Play(QtWidgets.QWidget):
    def __init__(self, save):
        super().__init__()
        self.save = save

        self.setStyleSheet("background-color: #135440; color: #75a154; ")

        self.aim_seconds = 0
        self.points = 0
        self.combo_points_counter = 0
        self.combo_points = 0
        self.combo_high = 0
        self.hit_points_value = 0
        self.miss_points_value = 0
        self.health_value = 5

        self.setFixedSize(1280, 1000)

        self.hearts()

        self.heart_count_label = QLabel(str(self.health_value), self)
        self.heart_count_label.setGeometry(350, 2, 50, 50)
        self.heart_count_label.setStyleSheet("font-size: 25px;")

        self.aim_timer_seconds = QLabel("0", self)
        self.aim_timer_seconds.setGeometry(145, 15, 90, 25)
        self.aim_timer_seconds.setStyleSheet("font-size: 25px;")

        try:
            # self.aim_username.setText(f'{save["username"]}')
            self.waim_username = QLabel(f'{save["username"]}', self)

        except Exception:
            # self.aim_username.setText(f'{save["username"]}')
            self.aim_username = QLabel(f"{os.getlogin()}", self)

        self.aim_username.setGeometry(15, 15, 130, 25)
        self.aim_username.setStyleSheet("font-size: 25px;")

        self.aim_level = QLabel("0", self)
        self.aim_level.setGeometry(245, 15, 30, 25)
        self.aim_level.setStyleSheet("font-size: 25px;")

        self.aim_points = QLabel(f"Points: {self.points}", self)
        self.aim_points.setGeometry(525, 15, 130, 25)
        self.aim_points.setStyleSheet("font-size: 25px;")

        self.aim_combo = QLabel(f"Combo:  {self.combo_points}", self)
        self.aim_combo.setGeometry(725, 5, 130, 25)
        self.aim_combo.setStyleSheet("font-size: 15px;")

        self.high_aim_combo = QLabel(f"HIGH Combo: {self.combo_high}", self)
        self.high_aim_combo.setGeometry(725, 30, 130, 15)
        self.high_aim_combo.setStyleSheet("font-size: 15px;")

        self.hit_object_label = QLabel(f"Hit: {self.hit_points_value}", self)
        self.hit_object_label.setGeometry(1070, 15, 300, 25)
        self.hit_object_label.setStyleSheet("font-size: 25px;")

        self.miss_object_label = QLabel(f"Miss: {self.miss_points_value}", self)
        self.miss_object_label.setGeometry(1170, 15, 300, 25)
        self.miss_object_label.setStyleSheet("font-size: 25px;")

        self.hit_effect = QSoundEffect(self)
        self.hit_effect.setSource(QUrl.fromLocalFile("Aim_audio/punch.wav"))

        self.fail_effect = QSoundEffect(self)
        self.fail_effect.setSource(
            QUrl.fromLocalFile("Aim_audio/fail_sound.wav")
        )

        self.obj_first = AimObject(600, 600, 250, 250, "obj_1", 5)

        self.obj_first.setGeometry(
            self.obj_first.position_x,
            self.obj_first.position_y,
            self.obj_first.o_width,
            self.obj_first.o_height,
        )

        self.obj_first.setParent(self)
        self.obj_first.setAutoRepeat(False)

        self.obj_first.pressed.connect(self.clicked_button_change_position)
        self.obj_first.setAutoExclusive(False)
        # self.obj_first.setFocusPolicy(Qt.NoFocus) #Blocking Keyboard

        self.menu_line = QFrame(self)
        self.menu_line.setFrameShape(QFrame.HLine)
        self.menu_line.setFrameShadow(QFrame.Sunken)
        self.menu_line.setGeometry(2, 50, 1278, 10)
        self.menu_line.setLineWidth(4)
        self.menu_line.setStyleSheet("background-color: #61c7a2")

        self.timer = QTimer(self)
        self.timer.timeout.connect(self.no_clicked_button_change_position)
        self.timer.start(3000)

        self.game_time = QTimer(self)
        self.game_time.timeout.connect(self.update_time_label)
        self.game_time.start(100)

        self.elapsed_timer = QElapsedTimer()
        self.elapsed_timer.start()

        self.start_time = QDateTime.currentDateTime()

        self.obj_first.setStyleSheet(
            """
            QPushButton {
                color: #75a154; 
                background-color: #2a6b48;
                border: 2px solid #45814e;
                border-radius: 120px;

            }
            QPushButton:hover {
                color: #9ab657;
            }
        """
        )

    def no_clicked_button_change_position(self):

        self.fail_effect.play()
        self.remove_points()
        self.miss_points()
        self.set_high_combo()
        self.set_attributes()

        self.obj_first.setGeometry(
            self.new_position_x,
            self.new_position_y,
            self.obj_first.o_width,
            self.obj_first.o_height,
        )

        self.hearts_remove()

    def clicked_button_change_position(self):
        button_size = self.obj_first.sizeHint()
        print(button_size.width())
        print(button_size.height())
        QTest.mouseRelease(self.obj_first, Qt.LeftButton)

        self.hit_effect.play()
        self.add_points()
        self.hit_points()
        self.combo_result()
        self.set_attributes()

        # self.new_position_x = random.randint(70, 1100)
        # self.new_position_y = random.randint(70, 850)
        self.obj_first.setGeometry(
            self.new_position_x,
            self.new_position_y,
            self.obj_first.o_width,
            self.obj_first.o_height,
        )

    def update_time_label(self):

        self.main_game_time = self.start_time.secsTo(QDateTime.currentDateTime())
        self.main_game_mins = self.main_game_time // 60
        self.main_game_secs = self.main_game_time % 60
        self.main_game_hours = self.main_game_mins // 60
        self.main_game_mins %= 60
        self.aim_timer_seconds.setText(
            f"{self.main_game_hours:02d}:{self.main_game_mins:02d}:{self.main_game_secs:02d}"
        )

    def hearts(self):
        self.heart_label = QLabel("a", self)
        self.heart_label.setGeometry(300, 2, 50, 50)
        self.heart_label.setStyleSheet("font-size: 25px;")
        self.heart_label_pixmap = QPixmap("Aim_icons/green_heart.png")
        self.heart_label_pixmap = self.heart_label_pixmap.scaled(40, 40)
        self.heart_label.setPixmap(self.heart_label_pixmap)
        self.heart_label.setStyleSheet("color: red;")
        self.heart_label.raise_()
        self.heart_label.stackUnder(self)

        self.heart_count_label = QLabel("", self)
        self.heart_count_label.setGeometry(350, 2, 50, 50)

    def add_points(self):
        self.points += 1
        self.aim_points.setText(f"Points: {self.points}")
        self.new_level = AimLevels.points_checker(self.points)
        self.aim_level.setText(str(self.new_level.level))
        self.timer.start(self.new_level.change_speed)

        # COMBO POINTS
        self.combo_points_counter += 1

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

    def hearts_remove(self):
        self.new_heart_count = 5

        heart = {
            5: [0, 100],
            4: [101, 200],
            3: [201, 300],
            2: [301, 400],
            1: [401, 500],
            0: [501, 600],
        }

        for x, y in heart.items():
            if self.miss_points_value > 600:
                sys.exit()
            if self.miss_points_value >= y[0] and self.miss_points_value <= y[1]:

                self.heart_count_label.setText(str(x))

            if self.new_heart_count <= x:
                self.new_heart_count = x

    def ignore_buttons(self, event):
        if event.key() == Qt.Key_Space:
            event.ignore()
        else:
            super().keyPressEvent(event)

    def combo_result(self):
        self.aim_combo.setText(f"Combo: {self.combo_points_counter}")

    def set_high_combo(self):

        if self.combo_points_counter >= self.combo_high:
            self.combo_high = self.combo_points_counter
            self.high_aim_combo.setText(f"HIGH Combo: {self.combo_high}")
        self.combo_points_counter = 0
        self.aim_combo.setText(f"Combo: {str(0)}")

    def set_attributes(self):
        self.level_options = AimLevels.set_level_attributes(self.points)

        START_X_AND_Y = 70

        if int(self.aim_level.text()) == self.level_options.level:

            self.level_border_x = int(self.level_options.border_x)
            self.level_border_y = int(self.level_options.border_y)
            self.obj_first.o_height = self.level_options.object_height
            self.obj_first.o_width = self.level_options.object_width
            print(self.level_border_x, self.level_border_y)

            self.new_position_x = random.randint(START_X_AND_Y, self.level_border_x)
            self.new_position_y = random.randint(START_X_AND_Y, self.level_border_y)
            self.obj_first.setStyleSheet(
                f"""
                QPushButton {{
                    color: #75a154; 
                    background-color: #2a6b48;
                    border: 2px solid #45814e;
                    border-radius: {self.level_options.object_height//2}px;
                }}
                QPushButton:hover {{
                    color: #9ab657;
                }}
                """
            )


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

    aim_play = Play("")
    aim_play.show()

    sys.exit(app.exec())
