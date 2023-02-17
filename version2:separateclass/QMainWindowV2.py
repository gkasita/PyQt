#version2 : setting up a separate class
import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton

#subclass of qmainwindow class
class ButtonHolder(QMainWindow):
    def __init__(self):
        #self = QMainWindow
        super().__init__()
        self.setWindowTitle("Button Holder app")
        button = QPushButton("Press Me")
        self.setCentralWidget(button)

app = QApplication(sys.argv)
window = ButtonHolder()
window.show()
app.exec()