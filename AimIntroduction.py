import sys

from PySide6 import QtWidgets
from PySide6.QtWidgets import QApplication, QLabel, QPushButton
from PySide6.QtGui import QCursor, QIcon
from PyQt5.QtCore import QFile, QTextStream
from PySide6 import QtCore


class Introduction(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        self.step_count = 0
        self.setWindowTitle("Aim Introduction")
        self.setWindowIcon(QIcon("Aim_icons/magic-book.png"))
        self.setFixedHeight(600)
        self.setFixedWidth(600)

        self.post_introduction_label = QLabel(
            "WELCOME PLAYER IN OUR AIM TRAINING \
            \n\n\nI am very pleased and glad that u downloaded my aim training \
            \n\n\nCLICK NEXT TO GET MORE INFORMATION ABOUT AIM GAME",
            self
        )
        self.post_introduction_label.setGeometry(25, 130, 560, 200)
        self.post_introduction_label.setAlignment(QtCore.Qt.AlignCenter)

        self.footer_label = QLabel("Created By: Meffy", self)
        self.footer_label.setGeometry(250, 580, 120, 20)

        self.next_step = QPushButton("NEXT", self)
        self.next_step.clicked.connect(self.description)
        self.next_step.setGeometry(500, 550, 100, 50)

        self.back_step = QPushButton("BACK", self)
        self.back_step.clicked.connect(self.description)
        self.back_step.setGeometry(0, 550, 100, 50)

        self.play_button = QPushButton("Play", self)
        self.play_button.setGeometry(250, 280, 120, 50)

        self.back_step.hide()
        self.play_button.hide()

        self.introduction_styles()

    def introduction_styles(self):

        self.setStyleSheet("background-color: #135440")

        self.post_introduction_label.setStyleSheet(
            """
            QLabel {
            color: #9ab657;
            font-size: 20px;
            }
            
            """
        )

        self.next_step.setStyleSheet(
            """
            QPushButton {
                color: #75a154; 
                background-color: #2a6b48;
                border: 2px solid #45814e;
                border-radius: 20px;
                font-size: 25px;

            }
            QPushButton:hover {
                color: #9ab657;
            }
            """
        )

        self.back_step.setStyleSheet(
            """
            QPushButton {
                color: #75a154; 
                background-color: #2a6b48;
                border: 2px solid #45814e;
                border-radius: 20px;
                font-size: 25px;

            }
            QPushButton:hover {
                color: #9ab657;
            }
            """
        )

        self.play_button.setStyleSheet(
            """
            QPushButton {
                color: #75a154; 
                background-color: #2a6b48;
                border: 2px solid #45814e;
                border-radius: 20px;
                font-size: 25px;

            }
            QPushButton:hover {
                color: #9ab657;
            }
            """
        )

        self.post_introduction_label.setStyleSheet(
            """
            QLabel {
                color: #9ab657; 
                background-color: #0e4232;
                border: 2px solid #45814e;
                border-radius: 20px;
                font-size: 20px;
                

            }
    
        """
        )


    def update_labels(self):
        if self.step_count == 0:
            self.post_introduction_label.setText(
                "WELCOME PLAYER IN OUR AIM TRAINING \
            \n\n\nI am very pleased and glad that u downloaded my aim training \
            \n\n\nCLICK NEXT TO GET MORE INFORMATION ABOUT AIM GAME"
            )

        elif self.step_count == 1:

            self.post_introduction_label.setText(
                "Your main goal is fast click on showing object. \nAfter clicked specific object amount \nYou will be advancing on next level \
            \nYou have only 4 hearts, \nbut you can get more using your gained points"
            )
            

            self.play_button.hide()
            self.post_introduction_label.setStyleSheet(
            """QLabel {color: #9ab657; background-color: #0e4232;border: 2px solid #45814e;border-radius: 20px;font-size: 20px;}"""
        )
            

        elif self.step_count == 2:
            self.post_introduction_label.setText("")
            self.play_button.show()

            self.post_introduction_label.setStyleSheet(
                """QLabel {}"""
            )


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
