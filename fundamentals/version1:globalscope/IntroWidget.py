#version1: setting everything up in the global scope

#importing the compenets we need
from PySide6.QtWidgets import QApplication, QWidget, QPushButton

#The sys modelu is resposible for processing command line arguments
import sys

#QApplication class manage the gui application's control flow and main settings
app = QApplication(sys.argv)

#QWidget is the base class for all drawable classes in Qt 
#QDialog is based on QWidget
#QMainWindow is designed around common needs for a main window to have
window = QWidget()
window.show()


#start the event loop
#app.exec_() -> older version of python
app.exec()
