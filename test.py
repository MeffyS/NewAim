import PySide6
from PySide6.QtWidgets import (
    QApplication,
    QMainWindow,
    QLabel,
    QWidget,
    QHBoxLayout,
    QVBoxLayout,
    QPushButton,
    QGridLayout,
)
from PySide6.QtGui import QScreen, QGuiApplication, QImage, QPixmap, Qt, QIcon


class MyTest(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setFixedSize(500, 500)

        self.setWindowTitle('Achievements')
        self.setWindowIcon(QIcon("Aim_icons\quest.png"))

        self.points_achievements = {
            "points_achievement_1": [
                50,
                "Congratulations You Unlock New Achievement",
                "NO REACHED",
                66,
            ],
            "points_achievement_2": [
                100,
                "Congratulations You Unlock New Achievement",
                "NO REACHED",
                114,
            ],
            "points_achievement_3": [
                200,
                "Congratulations You Unlock New Achievement",
                "NO REACHED",
                162,
            ],
            "points_achievement_4": [
                500,
                "Congratulations You Unlock New Achievement",
                "NO REACHED",
                210,
            ],
            "points_achievement_5": [
                1000,
                "Congratulations You Unlock New Achievement",
                "NO REACHED",
                258,
            ],
            "points_achievement_6": [
                2000,
                "Congratulations You Unlock New Achievement",
                "NO REACHED",
                306,
            ],
            "points_achievement_7": [
                5000,
                "Congratulations You Unlock New Achievement",
                "NO REACHED",
                354,
            ],
            "points_achievement_8": [
                10000,
                "Congratulations You Unlock New Achievement",
                "NO REACHED",
                402,
            ],
            "points_achievement_9": [
                20000,
                "Congratulations You Unlock New Achievement",
                "NO REACHED",
                450,
            ],
        }
        self.fast_click_achievements = {
            "fast_click_achievement_1": [
                5.0,
                "Congratulations You Unlock New Achievement",
                "NO REACHED",
                66,
            ],
            "fast_click_achievement_2": [
                3.5,
                "Congratulations You Unlock New Achievement",
                "NO REACHED",
                114,
            ],
            "fast_click_achievement_3": [
                2.5,
                "Congratulations You Unlock New Achievement",
                "NO REACHED",
                162,
            ],
            "fast_click_achievement_4": [
                2.0,
                "Congratulations You Unlock New Achievement",
                "NO REACHED",
                210,
            ],
            "fast_click_achievement_5": [
                1.0,
                "Congratulations You Unlock New Achievement",
                "NO REACHED",
                258,
            ],
            "fast_click_achievement_6": [
                0.7,
                "Congratulations You Unlock New Achievement",
                "NO REACHED",
                306,
            ],
            "fast_click_achievement_7": [
                0.4,
                "Congratulations You Unlock New Achievement",
                "NO REACHED",
                354,
            ],
            "fast_click_achievement_8": [
                0.25,
                "Congratulations You Unlock New Achievement",
                "NO REACHED",
                402,
            ],
            "fast_click_achievement_9": [
                0.2,
                "Congratulations You Unlock New Achievement",
                "NO REACHED",
                450,
            ],
        }

        self.hit_combo_achievements = {
            "hit_combo_achievement_1": [
                5,
                "Congratulations You Unlock New Achievement",
                "NO REACHED",
                66,
            ],
            "hit_combo_achievement_2": [
                10,
                "Congratulations You Unlock New Achievement",
                "NO REACHED",
                114,
            ],
            "hit_combo_achievement_3": [
                25,
                "Congratulations You Unlock New Achievement",
                "NO REACHED",
                162,
            ],
            "hit_combo_achievement_4": [
                50,
                "Congratulations You Unlock New Achievement",
                "NO REACHED",
                210,
            ],
            "hit_combo_achievement_5": [
                100,
                "Congratulations You Unlock New Achievement",
                "NO REACHED",
                258,
            ],
            "hit_combo_achievement_6": [
                250,
                "Congratulations You Unlock New Achievement",
                "NO REACHED",
                306,
            ],
            "hit_combo_achievement_7": [
                500,
                "Congratulations You Unlock New Achievement",
                "NO REACHED",
                354,
            ],
            "hit_combo_achievement_8": [
                1000,
                "Congratulations You Unlock New Achievement",
                "NO REACHED",
                402,
            ],
            "hit_combo_achievement_9": [
                1500,
                "Congratulations You Unlock New Achievement",
                "NO REACHED",
                450,
            ],
        }

        self.hit_achievements = {
            "hit_achievement_1": [
                200,
                "Congratulations You Unlock New Achievement",
                "NO REACHED",
                66,
            ],
            "hit_achievement_2": [
                500,
                "Congratulations You Unlock New Achievement",
                "NO REACHED",
                114,
            ],
            "hit_achievement_3": [
                1000,
                "Congratulations You Unlock New Achievement",
                "NO REACHED",
                162,
            ],
            "hit_achievement_4": [
                2000,
                "Congratulations You Unlock New Achievement",
                "NO REACHED",
                210,
            ],
            "hit_achievement_5": [
                5000,
                "Congratulations You Unlock New Achievement",
                "NO REACHED",
                258,
            ],
            "hit_achievement_6": [
                7500,
                "Congratulations You Unlock New Achievement",
                "NO REACHED",
                306,
            ],
            "hit_achievement_7": [
                10000,
                "Congratulations You Unlock New Achievement",
                "NO REACHED",
                354,
            ],
            "hit_achievement_8": [
                15000,
                "Congratulations You Unlock New Achievement",
                "NO REACHED",
                402,
            ],
            "hit_achievement_9": [
                20000,
                "Congratulations You Unlock New Achievement",
                "NO REACHED",
                450,
            ],
        }

    def player_achievements(self, points, fast_click, hit_combo,hit):
        labels = []
        for key, value in self.points_achievements.items():
            label = QLabel(f"{self.points_achievements[key][0]}", self)
            label.move(0, value[3] + len(labels) * 0)
            label.resize(67, 50)
            label.setStyleSheet(
                "background-color: #ff5c58; border: 2px solid gray; color: #ffffff; font-size: 15px; font-weight:bold"
            )
            label.setAlignment(Qt.AlignCenter)
            labels.append(label)
            if points > self.points_achievements[key][0]:
                label.setStyleSheet(
                    "background-color: #135440; border: 2px solid gray; color: #75a154; font-size: 15px; font-weight:bold"
                )
        for key, value in self.fast_click_achievements.items():
            label = QLabel(f" <= {self.fast_click_achievements[key][0]}", self)
            label.move(65, value[3] + len(labels) * 0)
            label.resize(67, 50)
            label.setStyleSheet(
                "background-color: #ff5c58; border: 2px solid gray; color: #ffffff; font-size: 15px; font-weight:bold"
            )
            label.setAlignment(Qt.AlignCenter)
            labels.append(label)
            if fast_click < self.fast_click_achievements[key][0]:
                label.setStyleSheet(
                    "background-color: #135440; border: 2px solid gray; color: #75a154; font-size: 15px; font-weight:bold"
                )

        for key, value in self.hit_combo_achievements.items():
            label = QLabel(f"{self.hit_combo_achievements[key][0]}", self)
            label.move(130, value[3] + len(labels) * 0)
            label.resize(67, 50)
            label.setStyleSheet(
                "background-color: #ff5c58; border: 2px solid gray; color: #ffffff; font-size: 15px; font-weight:bold"
            )
            label.setAlignment(Qt.AlignCenter)
            labels.append(label)
            if hit_combo > self.hit_combo_achievements[key][0]:
                label.setStyleSheet(
                 "background-color: #135440; border: 2px solid gray; color: #75a154; font-size: 15px; font-weight:bold"
                )
        for key, value in self.hit_achievements.items():
            label = QLabel(f"{self.hit_achievements[key][0]}", self)
            label.move(195, value[3] + len(labels) * 0)
            label.resize(67, 50)
            label.setStyleSheet(
                "background-color: #ff5c58; border: 2px solid gray; color: #ffffff; font-size: 15px; font-weight:bold"
            )
            label.setAlignment(Qt.AlignCenter)
            labels.append(label)
            if hit > self.hit_achievements[key][0]:
                label.setStyleSheet(
                "background-color: #135440; border: 2px solid gray; color: #75a154; font-size: 15px; font-weight:bold"
                )

        self.points_label = QLabel("score".upper(), self)
        self.points_label.setGeometry(0, 0, 67, 68)
        self.points_label.setStyleSheet(
            "background-color: #124228; border: 2px solid gray; color: #75a154; font-size: 15px; font-weight:bold"
        )
        self.points_label.setAlignment(Qt.AlignCenter)

        self.fast_click_label = QLabel("f.click".upper(), self)
        self.fast_click_label.setGeometry(65, 0, 67, 68)
        self.fast_click_label.setStyleSheet(
            "background-color: #124228; border: 2px solid gray; color: #75a154; font-size: 15px; font-weight:bold"
        )
        self.fast_click_label.setAlignment(Qt.AlignCenter)

        self.hit_combo_label = QLabel("combo".upper(), self)
        self.hit_combo_label.setGeometry(130, 0, 67, 68)
        self.hit_combo_label.setStyleSheet(
            "background-color: #124228; border: 2px solid gray; color: #75a154; font-size: 15px; font-weight:bold"
        )
        self.hit_combo_label.setAlignment(Qt.AlignCenter)

        self.hit_label = QLabel("hit".upper(), self)
        self.hit_label.setGeometry(195, 0, 67, 68)
        self.hit_label.setStyleSheet(
            "background-color: #124228; border: 2px solid gray; color: #75a154; font-size: 15px; font-weight:bold"
        )
        self.hit_label.setAlignment(Qt.AlignCenter)


if __name__ == "__main__":
    app = QApplication([])
    widget = MyTest()
    widget.show()
    app.exec_()
