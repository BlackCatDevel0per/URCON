import os, sys
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

		ip = self.lineEdit.text() # input cmd from text label

		prt = self.lineEdit_2.text() # input cmd from text label

		pswd = self.lineEdit_3.text() # input cmd from text label

		# создать новый текстовый файл
		conf = text_file = open("src/data/config.ini", "w")
		# запить текста в этот файл

		text_file.write("[DATA]")

		text_file.write("\nip = " + ip )

		text_file.write("\nprt = " + prt)

		text_file.write("\npswd = " + pswd )

		conf.close()

	def Settings(self, toggle):

		settings = text_file = open("src/data/settings.ini", "w")

		if toggle == Qt.Checked:

			text_file.write("[SETTINGS]")

			text_file.write("\nlogs = True") # Turn on rcon logs True or False

		else:

			text_file.write("[SETTINGS]")

			text_file.write("\nlogs = False") # Turn on rcon logs True or False

		settings.close()

	def closewin(self):

		self.close()
