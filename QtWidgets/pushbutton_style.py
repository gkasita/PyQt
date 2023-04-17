#Qicon dont work on mac

from PySide6.QtWidgets import QApplication, QWidget, QPushButton
from PySide6.QtGui import QIcon, QFont, QPixmap
from PySide6.QtCore import QSize
import sys

class Window(QWidget):
    def __init__(self):
        super().__init__()

        self.setGeometry(100, 100, 600, 500)
        self.setWindowTitle("PySide QPushButton")
        self.setWindowIcon(QIcon('icons/qt.png'))

        #2 parameter -> text, qwidget
        btn = QPushButton("click", self)
        #settext
        btn.setText("click me")
        #set xpos, ypos, width, height
        btn.setGeometry(100, 100, 100, 100)
        #set icon
        btn.setIcon(QIcon("icons/qt.png"))
        #set font -> font family, font size
        btn.setFont(QFont("Sanserif", 20))
        #set icon size -> width, height
        btn.setIconSize(QSize(36, 36))

        #set style sheet
        btn.setStyleSheet('background-color:green')

app = QApplication(sys.argv)

window = Window()
window.show()

app.exec()