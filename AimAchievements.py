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
from PySide6.QtGui import QScreen, QGuiApplication, QImage, QPixmap, QTextCursor
from PySide6 import QtWidgets

from test import MyTest


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setFixedSize(1280, 1000)

        self.a = MyTest()

        self.test_label = QTextEdit(f"ABC1\nxD")
        self.test_label.hide()
        self.test_label.setReadOnly(True)

        self.my_button = QLabel("Achievements", self)
        self.my_button.setGeometry(1100, 5, 100, 50)

        self.my_button.enterEvent = self.show_button
        self.my_button.leaveEvent = self.hide_button

        self.timer = QTimer(self)
        self.timer.timeout.connect(self.refreshMainWindow)
        self.timer.start(1000)

        self.minus_points = QPushButton("minus p", self)
        self.minus_points.setGeometry(0, 5, 100, 50)

    def minus_p(self):
        

    

    def refreshMainWindow(self):
        self.repaint()
        self.check_screen_paramters()

    def show_button(self, event):
        self.check_screen_paramters()
        self.a.show()

        super().enterEvent(event)

    def hide_button(self, event):
        # self.a.hide()
        self.test_label.hide()
        print("no hide")
        super().leaveEvent(event)

    def check_screen_paramters(self):

        pos = self.pos()
        x, y = int(pos.x()), int(pos.y())
        # self.a.setGeometry(x + 500, y + 31, 500, 500)
        self.a.setStyleSheet("background-color: #431556; color: #ffffff")
        print(self.a.x())
        achievements_params = self.a.geometry()
        screen = app.primaryScreen()

        screen_x = screen.size().width()
        achievement_x = achievements_params.x()
        achievement_width = achievements_params.width()
        if screen_x // 2 > (achievement_x // 2) + achievement_width:
            pass

            print("screen is > ")
        else:
            print("Screen is < ")
            # self.a.setGeometry(x - 500, y + 31, 500, 500)


if __name__ == "__main__":
    app = QApplication([])
    widget = MainWindow()
    widget.show()
    app.exec_()
