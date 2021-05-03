import configparser, os, sys
from PyQt5 import uic
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QMainWindow, QFileDialog, QLineEdit)

import about

import config

import settings

class Connect(QMainWindow):

	def __init__(self):
		super(Connect, self).__init__()
		uic.loadUi('src/windows/connect.ui', self)

		from setlang import SetConnectWindowLang
		SetConnectWindowLang(self)

		self.pushButton.clicked.connect(self.ConnectConfig)

		self.pushButton.clicked.connect(self.closewin)

		self.pushButton_2.clicked.connect(self.openlogsdir)

		self.checkBox.stateChanged.connect(self.Settings)

		self.toolButton.clicked.connect(self.About)

		self.lineEdit_3.setEchoMode(QLineEdit.Password) # Спрятать пароль
###
		self.lineEdit.setText( config.ip )
		self.lineEdit_2.setText( str( config.prt ) )
		self.lineEdit_3.setText( config.pswd )
###
		if settings.logs == "True":

			self.checkBox.setChecked(True)

		else:

			self.checkBox.setChecked(False)

		self.aboutwin = about.About() # Окно о приложении

	def About(self):

		self.aboutwin.show()

	def openlogsdir(self):

		title = "Logs"

		qfd = QFileDialog()
		path = "logs/"
		filter = "log(*.log)"
		f = QFileDialog.getOpenFileName(qfd, title, path, filter)

	def ConnectConfig(self):

		config1 = configparser.ConfigParser()

		ip = self.lineEdit.text() # input cmd from text label

		prt = self.lineEdit_2.text() # input cmd from text label

		pswd = self.lineEdit_3.text() # input cmd from text label

		conf1 = "src/data/config.ini"
		config1.read(conf1)
		config1.set("DATA", "ip", ip)
		config1.set("DATA", "prt", prt)
		config1.set("DATA", "pswd", pswd)
		config1.write(open(conf1, "w"))

	def Settings(self, toggle):

		config2 = configparser.ConfigParser()

		if toggle == Qt.Checked: # Turn on rcon logs

			conf2 = "src/data/settings.ini"
			config2.read(conf2)
			config2.set("SETTINGS", "logs", "True")
			config2.write(open(conf2, "w"))

		else: # Turn off rcon logs

			conf2 = "src/data/settings.ini"
			config2.read(conf2)
			config2.set("SETTINGS", "logs", "False")
			config2.write(open(conf2, "w"))

	def closewin(self):

		self.close()
