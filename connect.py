from __future__ import annotations

import configparser

from PySide6.QtUiTools import loadUiType

from PySide6.QtCore import Qt
from PySide6.QtWidgets import QFileDialog

import about

import config

import settings

from typing import TYPE_CHECKING

if TYPE_CHECKING:
	from PySide6.QtWidgets import QWidget


ui_cls: object
base_cls: QWidget

# TODO: On build package autouic.. (uis to code) Hmm..
ui_cls, base_cls = loadUiType('src/uis/connect.ui')


class Connect(ui_cls, base_cls):

	# TODO: Fixed ui size & etc.
	def __init__(self):
		super().__init__()

		self.setupUi(self)

		from setlang import SetConnectWindowLang
		SetConnectWindowLang(self)

		self.acceptButton.clicked.connect(self.ConnectConfig)
		self.acceptButton.clicked.connect(self.closewin)

		self.openLogsButton.clicked.connect(self.openlogsdir)

		self.checkBox.stateChanged.connect(self.Settings)

		self.toolButton.clicked.connect(self.About)

		self.lineEdit.setText(config.ip)
		self.lineEdit_2.setText(str(config.prt))
		self.lineEdit_3.setText(config.pswd)
		if settings.logs == "True":

			self.checkBox.setChecked(True)

		else:

			self.checkBox.setChecked(False)

		self.aboutwin = about.About()

	def About(self):

		self.aboutwin.show()

	def openlogsdir(self):

		title = "Logs"

		qfd = QFileDialog()
		path = "logs/"
		fil = "log(*.log)"
		##
		QFileDialog.getOpenFileName(qfd, title, path, fil)


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

		##
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
