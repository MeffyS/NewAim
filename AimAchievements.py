import sys

from PySide6.QtWidgets import (
    QApplication,
    QMainWindow,
    QPushButton,
    QLabel,
    QLineEdit,
    QTextEdit,
)

from PySide6.QtCore import QTimer
from PySide6.QtGui import QScreen, QGuiApplication
from PySide6 import QtWidgets

achievements = {
    "achievement_1": ["Get 50 points", "NOT REACHED"],
    "achievement_2": ["Get 100 points", "NOT REACHED"],
    "achievement_3": ["Get 200 points", "NOT REACHED"],
    "achievement_4": ["Get 500 points", "NOT REACHED"],
    "achievement_5": ["Get 1000 points", "NOT REACHED"],
}


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setFixedSize(500, 500)

        self.test_label = QLabel("ABC1")
        self.test_label.hide()

        # self.b = self.my_screen.physicalSize()

        # self.test_label.setGeometry(1210, 270, 50, 50)

        self.my_button = QPushButton("Achievements", self)
        self.my_button.setGeometry(50, 50, 100, 50)

        self.my_button.enterEvent = self.show_button
        self.my_button.leaveEvent = self.hide_button

        self.timer = QTimer(self)
        self.timer.timeout.connect(self.refreshMainWindow)
        self.timer.start(1000)

    def refreshMainWindow(self):
        self.repaint()
        self.check_screen_paramters()

    def show_button(self, event):
        self.check_screen_paramters()

        self.test_label.show()

        super().enterEvent(event)

    def hide_button(self, event):
        self.test_label.hide()
        print("no hide")
        super().leaveEvent(event)

    def check_screen_paramters(self):

        pos = self.pos()
        x, y = int(pos.x()), int(pos.y())
        self.test_label.setGeometry(x + 500, y + 31, 500, 500)
        self.test_label.setStyleSheet("background-color: #431556; color: #ffffff")
        achievements_params = self.test_label.geometry()
        screen = app.primaryScreen()
        print("achi x", achievements_params.x()+500)
        print("achi y", achievements_params.y())
        print(f"Screen Height: {screen.size().height()}")
        print(f"Screen Width: {screen.size().width()}")
        screen_x = screen.size().width()
        achievement_x = achievements_params.x()
        achievement_width = achievements_params.width()
        if screen_x // 2 > (achievement_x // 2) + achievement_width :
            

            print("screen is > ")
        else:
            print("Screen is < ")
            self.test_label.setGeometry(x - 500, y + 31, 500, 500)

        # if achievements_params.x() // 2 > 1 :
        #     self.test_label.setGeometry(x + 500, y + 31, 500, 500)
        #     print(
        #         "Lewa",
        #     )
        #     print(achievements_params.x() // 2, "scr", screen.size().width() // 2)
        # if achievements_params.x() // 2 < 1 :
        #     self.test_label.setGeometry(x - 500, y + 31, 500, 500)


if __name__ == "__main__":
    app = QApplication([])
    widget = MainWindow()
    widget.show()
    app.exec_()
