import sys
import random
import os
import time


from PySide6.QtCore import QUrl
from PySide6.QtMultimedia import QSoundEffect

from PySide6.QtCore import QTimer, QDateTime, QElapsedTimer, Qt, QSize
from PySide6 import QtWidgets
from PySide6.QtWidgets import QLabel, QFrame
from PySide6.QtGui import QPixmap, QCursor, QIcon, QShortcut, QKeySequence
from PySide6.QtTest import QTest


import AimLevels


class Play(QtWidgets.QWidget):
    def __init__(self, save):
        super().__init__()
        self.save = save

        self.setCursor(QCursor(QPixmap("Aim_icons/axe.png")))

        self.setStyleSheet("background-color: #135440; color: #75a154; ")

        self.aim_seconds = 0
        self.points = 0
        self.combo_points_counter = 0
        self.combo_points = 0
        self.combo_high = 0
        self.hit_points_value = 0
        self.miss_points_value = 0
        self.health_value = 5
        self.gold = 100
        self.space_helper_count = 10

        self.setFixedSize(1280, 1000)

        self.hearts()
        self.gained_gold()
        self.username()
        self.level_up()
        self.points_image()
        self.hit_combo_image()
        self.miss_combo_image()

        self.heart_count_label = QLabel(str(self.health_value), self)
        self.heart_count_label.setGeometry(30, 3, 10, 20)
        self.heart_count_label.setStyleSheet("font-size: 20px;")

        self.gold_label = QLabel(str(self.gold), self)
        self.gold_label.setGeometry(80, 3, 100, 20)
        self.gold_label.setStyleSheet("font-size: 20px;")

        self.aim_timer_seconds = QLabel("0", self)
        self.aim_timer_seconds.setGeometry(145, 315, 90, 25)
        self.aim_timer_seconds.setStyleSheet("font-size: 25px;")

        try:
            self.aim_username = QLabel(f'Username: {save["username"]}', self)

        except Exception:
            self.aim_username = QLabel(f"Username: {os.getlogin()}", self)

        self.aim_username.setGeometry(25, 25, 260, 25)
        self.aim_username.setStyleSheet("font-size: 20px;")

        self.aim_level = QLabel(f"0", self)
        self.aim_level.setGeometry(330, 25, 30, 25)
        self.aim_level.setStyleSheet("font-size: 20px;")

        self.aim_points = QLabel(f"Points: {self.points:,}", self)
        self.aim_points.setGeometry(330, 0, 150, 25)
        self.aim_points.setStyleSheet("font-size: 20px;")

        self.aim_combo = QLabel(f"Combo:  {self.combo_points}", self)
        self.aim_combo.setGeometry(500, 660, 130, 25)
        self.aim_combo.setStyleSheet("font-size: 15px;")

        self.hit_object_label = QLabel(f"Hit: {self.hit_points_value}", self)
        self.hit_object_label.setGeometry(1070, 15, 300, 25)
        self.hit_object_label.setStyleSheet("font-size: 25px;")

        self.miss_object_label = QLabel(f"Miss: {self.miss_points_value}", self)
        self.miss_object_label.setGeometry(1170, 15, 300, 25)
        self.miss_object_label.setStyleSheet("font-size: 25px;")

        self.average_hit_label = QLabel(f"100 %", self)
        self.average_hit_label.setGeometry(970, 15, 70, 25)
        self.average_hit_label.setStyleSheet("font-size: 25px;")

        self.average_hit_ratio_label = QLabel(f"HIT RATIO", self)
        self.average_hit_ratio_label.setGeometry(870, 15, 100, 25)
        self.average_hit_ratio_label.setStyleSheet("font-size: 20px;")

        self.highest_score_label = QLabel(f"Highest Score", self)
        self.highest_score_label.setGeometry(470, 200, 120, 17)
        self.highest_score_label.setStyleSheet("font-size: 13px;")

        self.fastest_click_label = QLabel(f"Fastest Click", self)
        self.fastest_click_label.setGeometry(470, 280, 120, 17)
        self.fastest_click_label.setStyleSheet("font-size: 13px;")

        self.hit_combo_label = QLabel(f"Hit Combo: {self.combo_high}", self)
        self.hit_combo_label.setGeometry(510, 23, 160, 30)
        self.hit_combo_label.setStyleSheet("font-size: 20px;")

        self.miss_combo_label = QLabel(f"Miss Combo: 0", self)
        self.miss_combo_label.setGeometry(510, 3, 130, 20)
        self.miss_combo_label.setStyleSheet("font-size: 20px;")

        self.hit_effect = QSoundEffect(self)
        self.hit_effect.setSource(QUrl.fromLocalFile("Aim_audio/punch.wav"))

        self.fail_effect = QSoundEffect(self)
        self.fail_effect.setSource(QUrl.fromLocalFile("Aim_audio/fail_sound.wav"))

        self.obj_first = AimObject(600, 600, 250, 250, "obj_1", 5)

        self.obj_first.setGeometry(
            self.obj_first.position_x,
            self.obj_first.position_y,
            self.obj_first.o_width,
            self.obj_first.o_height,
        )

        self.obj_first.setCursor(QCursor(QPixmap("Aim_icons/axe_cursor.png")))
        self.obj_first.setIcon(QIcon("aim_icons/shield.png"))
        self.obj_first.setIconSize(
            QSize(self.obj_first.o_width, self.obj_first.o_height)
        )

        self.obj_first.setParent(self)
        self.obj_first.setAutoRepeat(False)

        self.obj_first.pressed.connect(self.clicked_button_change_position)
        self.obj_first.setAutoExclusive(False)
        self.obj_first.setFocusPolicy(Qt.NoFocus)  # Blocking Keyboard

        self.last_hit = QLabel("", self)
        self.last_hit.setGeometry(0, 0, 20, 20)
        self.last_hit.setStyleSheet("background-color: #75a154; border-radius: 10px;")
        self.last_hit.hide()

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

        shortcut = QShortcut(QKeySequence("space"), self)
        self.shortcut_available = True
        shortcut.activated.connect(self.onShortcutActivated)

    def no_clicked_button_change_position(self):

        self.fail_effect.play()
        self.remove_points()
        self.miss_points()
        self.set_high_combo()
        self.set_attributes()
        self.average_of_hit()

        self.obj_first.setGeometry(
            self.new_position_x,
            self.new_position_y,
            self.obj_first.o_width,
            self.obj_first.o_height,
        )

        self.hearts_remove()

    def clicked_button_change_position(self):

        QTest.mouseRelease(self.obj_first, Qt.LeftButton)

        self.click_functionality()

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

        self.heart_label = QLabel("", self)
        self.heart_label.setGeometry(5, 0, 50, 25)
        self.heart_label_pixmap = QPixmap("Aim_icons/green_heart.png")
        self.heart_label_pixmap = self.heart_label_pixmap.scaled(20, 20)
        self.heart_label.setPixmap(self.heart_label_pixmap)

    def gained_gold(self):

        self.gold_img = QLabel("", self)
        self.gold_img.setGeometry(60, 1, 50, 25)
        self.gold_img_pixmap = QPixmap("Aim_icons/coins.png")
        self.gold_img_pixmap = self.gold_img_pixmap.scaled(20, 20)
        self.gold_img.setPixmap(self.gold_img_pixmap)

    def username(self):
        self.user_img = QLabel("", self)
        self.user_img.setGeometry(3, 24, 50, 25)
        self.user_img_pixmap = QPixmap("Aim_icons/user.png")
        self.user_img_pixmap = self.user_img_pixmap.scaled(20, 20)
        self.user_img.setPixmap(self.user_img_pixmap)

    def level_up(self):

        self.level_img = QLabel("", self)
        self.level_img.setGeometry(290, 21, 40, 35)
        self.level_img_pixmap = QPixmap("Aim_icons/crown.png")
        self.level_img_pixmap = self.level_img_pixmap.scaled(20, 20)
        self.level_img.setPixmap(self.level_img_pixmap)

    def points_image(self):

        self.points_img = QLabel("", self)
        self.points_img.setGeometry(280, 0, 40, 24)
        self.points_img_pixmap = QPixmap("Aim_icons/stars.png")
        self.points_img_pixmap = self.points_img_pixmap.scaled(40, 40)
        self.points_img.setPixmap(self.points_img_pixmap)

    def hit_combo_image(self):

        self.combo_img = QLabel("", self)
        self.combo_img.setGeometry(480, 10, 30, 50)
        self.combo_img_pixmap = QPixmap("Aim_icons/power.png")
        self.combo_img_pixmap = self.combo_img_pixmap.scaled(22, 22)
        self.combo_img.setPixmap(self.combo_img_pixmap)

    def miss_combo_image(self):

        self.miss_img = QLabel("", self)
        self.miss_img.setGeometry(480, 3, 30, 20)
        self.miss_img_pixmap = QPixmap("Aim_icons/snail.png")
        self.miss_img_pixmap = self.miss_img_pixmap.scaled(22, 22)
        self.miss_img.setPixmap(self.miss_img_pixmap)

    def add_points(self):

        self.points += 1
        self.aim_points.setText(f"Points: {self.points:,}")
        self.new_level = AimLevels.points_checker(self.points)
        self.aim_level.setText(str(self.new_level.level))
        # self.aim_level.setText(f"Level: {self.new_level.level}")
        self.timer.start(self.new_level.change_speed)

        # COMBO POINTS
        self.combo_points_counter += 1

    def remove_points(self):

        self.points -= 1
        self.aim_points.setText(f"Points: {self.points:,}")
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

    def combo_result(self):

        self.aim_combo.setText(f"Combo: {self.combo_points_counter}")

    def set_high_combo(self):

        if self.combo_points_counter >= self.combo_high:
            self.combo_high = self.combo_points_counter
            self.hit_combo_label.setText(f"Hit Combo: {self.combo_high}")
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
            self.obj_first.setIconSize(
                QSize(self.level_options.object_width, self.level_options.object_height)
            )

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

    def average_of_hit(self) -> int:

        if self.miss_points_value > 0:
            self.average_result = round(
                (
                    self.hit_points_value
                    / (self.miss_points_value + self.hit_points_value)
                    * 100
                ),
                2,
            )
            self.average_hit_label.setText(f"{str(self.average_result)}")
        else:
            self.average_hit_label.setText(f"100 %")

    def click_gold(self) -> int:

        self.level_gold = AimLevels.set_level_attributes(self.points)
        self.gold_converter = self.level_gold.money_converter()
        self.gold += self.gold_converter
        print(round(self.gold, 2))
        self.gold_label.setText(f"{round(self.gold,2)}")

    def click_mouse_pos(self):

        mouse_position = QCursor.pos()
        # print(f"Kliknięto w pozycji: {mouse_position}")
        x = mouse_position.x()
        y = mouse_position.y()
        print(x, y)
        if y < 100:
            self.last_hit.hide()
        else:
            self.last_hit.setGeometry(x - 18, y - 50, 20, 20)
            self.last_hit.show()

    # def keyPressEvent(self, event):

    #     if event.key() == Qt.Key_Space:
    #         self.click_functions()
    #         self.obj_first.setGeometry(
    #         self.new_position_x,
    #         self.new_position_y,
    #         self.obj_first.o_width,
    #         self.obj_first.o_height,
    #     )

    #         print('space')
    #     elif event.key() == Qt.Key_A:
    #         self.last_hit.hide()
    #     elif event.key() == Qt.Key_S:
    #         print("S key pressed")
    #     elif event.key() == Qt.Key_D:
    #         print("D key pressed")
    #     else:
    #         super().keyPressEvent(event)

    def click_functionality(self):
        self.hit_effect.play()
        self.add_points()
        self.hit_points()
        self.combo_result()
        self.set_attributes()
        self.average_of_hit()
        self.click_gold()
        self.click_mouse_pos()

        self.obj_first.setGeometry(
            self.new_position_x,
            self.new_position_y,
            self.obj_first.o_width,
            self.obj_first.o_height,
        )

    def onShortcutActivated(self):

        if self.shortcut_available and self.space_helper_count > 0:
            self.shortcut_available = False
            self.click_functionality()
            self.last_hit.hide()
            QTimer.singleShot(500, self.enableButton)
            self.space_helper_count -= 1

    def enableButton(self):
        self.shortcut_available = True


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
