import sys

from PySide6 import QtWidgets
from PySide6.QtWidgets import QApplication, QLabel, QPushButton
from PySide6.QtGui import QCursor, QIcon


class Introduction(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        self.step_count = 0
        self.setWindowTitle("Aim Introduction")
        self.setWindowIcon(QIcon("Aim_icons/magic-book.png"))
        self.setFixedHeight(600)
        self.setFixedWidth(600)

        self.head_introduction_label = QLabel(
            "WELCOME PLAYER IN OUR AIM TRAINING", self
        )
        self.head_introduction_label.setGeometry(20, 50, 580, 30)

        self.post_introduction_label = QLabel(
            "I am very pleased and glad that u downloaded my aim training", self
        )
        self.post_introduction_label.setGeometry(25, 130, 580, 100)

        self.second_post_introduction_label = QLabel(
            "CLICK NEXT TO GET MORE INFORMATION ABOUT AIM GAME", self
        )
        self.second_post_introduction_label.setGeometry(25, 230, 580, 100)

        self.footer_label = QLabel("Created By: Meffy", self)
        self.footer_label.setGeometry(250, 580, 120, 20)

        self.next_step = QPushButton("NEXT", self)
        self.next_step.clicked.connect(self.description)
        self.next_step.setGeometry(500, 550, 100, 50)

        self.back_step = QPushButton("BACK", self)
        self.back_step.clicked.connect(self.description)
        self.back_step.setGeometry(0, 550, 100, 50)

        self.back_step.hide()

        self.head_introduction_label.setStyleSheet(
            """
            QLabel {
            color: red;
            font-size: 30px;
            }
            """
        )

        self.post_introduction_label.setStyleSheet(
            """
            QLabel {
            color: red;
            font-size: 20px;
            }
            
            """
        )

        self.second_post_introduction_label.setStyleSheet(
            """
            QLabel {
            color: red;
            font-size: 20px;
            }
            
            """
        )

        self.next_step.setStyleSheet(
            """
            QPushButton {
                color: #008000; 
                background-color: #272727;
                border: 2px solid white;
                border-radius: 20px;
                font-size: 25px;

            }
            QPushButton:hover {
                color: #00DD00;
            }
            """
        )

        self.back_step.setStyleSheet(
            """
            QPushButton {
                color: #008000; 
                background-color: #272727;
                border: 2px solid white;
                border-radius: 20px;
                font-size: 25px;

            }
            QPushButton:hover {
                color: #00DD00;
            }
            """
        )

    def update_labels(self):
        if self.step_count == 0:
            self.head_introduction_label.setText("WELCOME PLAYER IN OUR AIM TRAINING")
            self.post_introduction_label.setText(
                "I am very pleased and glad that u downloaded my aim training"
            )
        elif self.step_count == 1:
            self.head_introduction_label.setText("Nic")
            self.post_introduction_label.setText("Nic")
            self.second_post_introduction_label.setText("")
        elif self.step_count == 2:
            self.head_introduction_label.setText("Hello")
            self.post_introduction_label.setText("Hi")
            self.second_post_introduction_label.setText("")

    def description(self):
        sender = self.sender()

        if sender.text() == "NEXT":
            self.step_count += 1
            self.update_labels()
            self.back_step.show()
            print(self.step_count)
            if self.step_count >= 2:
                self.next_step.hide()

        elif sender.text() == "BACK":
            self.step_count -= 1
            print(self.step_count)
            self.update_labels()
            if self.step_count == 0:
                self.back_step.hide()
                self.next_step.show()


if __name__ == "__main__":

    app = QtWidgets.QApplication([])

    aim_introduction = Introduction()

    aim_introduction.resize(800, 600)
    aim_introduction.show()

    sys.exit(app.exec())
