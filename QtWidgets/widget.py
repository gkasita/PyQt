import sys
from PySide6.QtWidgets import *

class Widget(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        self.setGeometry(100, 100, 200, 500)



app = QApplication(sys.argv)
w = Widget()
w.show()
app.exec()

