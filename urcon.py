from __future__ import annotations

from PySide6.QtUiTools import loadUiType
from PySide6.QtWidgets import QApplication

from typing import TYPE_CHECKING

import checker

from setlang import SetMainWindowLang
from setlang import SetLangEN, SetLangRU
from client import Client

import logging

import connect as conctwin

import config

import settings

if TYPE_CHECKING:
	from PySide6.QtWidgets import QMainWindow

# Icon from https://www.hiclipart.com/free-transparent-background-png-clipart-vrmjs

ui_cls: object
base_cls: QMainWindow

# TODO: On build package autouic.. (uis to code) Hmm..
# TODO: More hints..
ui_cls, base_cls = loadUiType('src/uis/main.ui')


class URCON(ui_cls, base_cls):

	def __init__(self):

		super().__init__()

		self.setupUi(self)

		self.show()  ##

		SetMainWindowLang(self)
		self.sendButton.clicked.connect(self.Send)
		self.sendButton.setShortcut("Enter")

		self.lineEdit.returnPressed.connect(self.Send)
		self.connectui.triggered.connect(self.ConUi)

		self.setlangen.triggered.connect(SetLangEN)
		self.setlangru.triggered.connect(SetLangRU)

		self.log()

		self.Stop()


	def Send(self: URCON) -> None:
		try:

			with Client(host = config.ip, port = config.prt, passwd = config.pswd) as client:
				empty = " " # " " is for other servers
				sendcmd = empty + self.lineEdit.text() # input cmd from text label
				servcmd = client.run(sendcmd)

				self.sendcmd = sendcmd

				self.servcmd = servcmd

				self.textbrowser.append(servcmd)

				self.lineEdit.clear()

				if sendcmd == empty + "stop":

					from setlang import ConnectionLost
					self.textbrowser.append(ConnectionLost)

		except:
			from setlang import RconConnectionError
			self.textbrowser.append(RconConnectionError)

			self.lineEdit.clear()


	def ConUi(self) -> None:
		##
		self.conwin = conctwin.Connect()
		self.conwin.show()


	def log(self):
		if settings.logs == "True":
			return

		# self.sendButton.clicked.connect(self.logs)


	# def logs(self):

	# 	try:

	# 		logfile('logs/rcon.log', maxBytes=1000000, backupCount=3)

	# 		fmt = logging.Formatter('%(asctime)s: %(message)s');

	# 		logzero.formatter(fmt)

	# 		logger.info(self.sendcmd)
	# 		logger.info(self.servcmd)

	# 	except:

	# 		pass

	def Stop(self):

		pass


def main():
	app = QApplication([])
	window = URCON()
	window.show()
	app.exec()


if __name__ == '__main__':
	main()
