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
from PySide6.QtGui import QScreen, QGuiApplication, QImage, QPixmap, Qt


class MyTest(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setFixedSize(500, 500)

        points = 22512

        # słownik z danymi
        achievements = {
            "achievement_1": [
                50,
                "Congratulations You Unlock New Achievement",
                "NO REACHED",
                66,
            ],
            "achievement_3": [
                100,
                "Congratulations You Unlock New Achievement",
                "NO REACHED",
                114,
            ],
            "achievement_4": [
                200,
                "Congratulations You Unlock New Achievement",
                "NO REACHED",
                162,
            ],
            "achievement_5": [
                500,
                "Congratulations You Unlock New Achievement",
                "NO REACHED",
                210,
            ],
            "achievement_6": [
                1000,
                "Congratulations You Unlock New Achievement",
                "NO REACHED",
                258,
            ],
            "achievement_7": [
                2000,
                "Congratulations You Unlock New Achievement",
                "NO REACHED",
                306,
            ],
            "achievement_8": [
                5000,
                "Congratulations You Unlock New Achievement",
                "NO REACHED",
                354,
            ],
            "achievement_9": [
                10000,
                "Congratulations You Unlock New Achievement",
                "NO REACHED",
                402,
            ],
            "achievement_10": [
                20000,
                "Congratulations You Unlock New Achievement",
                "NO REACHED",
                450,
            ],
        }

        print(achievements["achievement_1"][0])
        labels = []
        for key, value in achievements.items():
            print(key)
            label = QLabel(f"{achievements[key][0]}", self)
            label.move(0, value[3] + len(labels) * 0)
            label.resize(70, 50)
            label.setStyleSheet(
                "background-color: red; border: 2px solid gray; color: white;"
            )
            label.setAlignment(Qt.AlignCenter)
            labels.append(label)
            if points > achievements[key][0]:
                label.setStyleSheet(
                "background-color: green; border: 2px solid gray; color: white;"
            )

        self.points_label = QLabel("POINTS", self)
        self.points_label.setGeometry(0, 0, 70, 68)
        self.points_label.setStyleSheet(
            "background-color: purple; border: 2px solid gray; color: white;"
        )
        self.points_label.setAlignment(Qt.AlignCenter)

        # self.achievement_label.setGeometry(0, 48, 70, 50)
        # self.achievement_label.setStyleSheet(
        #     "background-color: red; border: 2px solid gray; color: white;"
        # )
        # self.achievement_label.setAlignment(Qt.AlignCenter)


if __name__ == "__main__":
    app = QApplication([])
    widget = MyTest()
    widget.show()
    app.exec_()
