#QMainwindow <- qtoolbar, qdockwidget, qmenubar, qstatusbar
#a main window provides a framework for building an application

#Qmainwindow inherits from qwidget

from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton
import sys

app = QApplication(sys.argv)

window = QMainWindow()
window.setWindowTitle("Our first MainWindow App")

button = QPushButton()
button.setText("Press Me")

window.setCentralWidget(button)

window.show()
app.exec()