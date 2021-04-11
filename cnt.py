# PyQt5
import sys
from PyQt5 import QtWidgets

import config # Config

import connect_ui # connect UI

class Connect(QtWidgets.QMainWindow, connect_ui.Ui_MainWindow):

	def __init__(self):

		super().__init__()
		self.setupUi(self)

def con():

	app = QtWidgets.QApplication(sys.argv)
	window = Connect()
	window.show()
	app.exec_()

con()