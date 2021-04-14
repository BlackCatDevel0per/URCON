import sys
from PyQt5 import uic
from PyQt5.QtWidgets import (QMainWindow, QApplication)

from logzero import logger, logfile # Логирование
###
import checker # Проверка целостности

from client import Client # RCON

import logging, logzero # Логирование

import connect as conctwin # Connect

import config # Config

import settings # Settings

# Иконка окна взята из https://www.hiclipart.com/free-transparent-background-png-clipart-vrmjs

### Инициализация главного окна
class URCON(QMainWindow):

	def __init__(self):

		super(URCON, self).__init__()
		uic.loadUi('src/windows/main.ui', self)
		self.show()
		
		self.pushButton.clicked.connect(self.Send) # Действие при нажатии на кнопку SEND

		self.pushButton.setShortcut("Enter") # Действие при нажатии на Enter

		self.lineEdit.returnPressed.connect(self.Send) # Действие при нажатии на Enter

		self.toolButton.clicked.connect(self.ConUi) # Открытие нового окна

		self.log()

		self.conwin = conctwin.Connect() # Окно соеденения

		self.Stop()

	def Send(self):

		try:

			with Client(host = config.ip, port = config.prt, passwd = config.pswd) as client:

				empty = " " # " " is for other servers

				sendcmd = empty + self.lineEdit.text() # input cmd from text label

				servcmd = client.run( sendcmd )

				self.sendcmd = sendcmd

				self.servcmd = servcmd

				self.textbrowser.append( servcmd )

				self.lineEdit.clear() # Очистка текста после отправки

				if sendcmd == empty + "stop":

					self.textbrowser.append( 'Соеденение разорвано!' )

		except:

			self.textbrowser.append( 'Ошибка подключения!' )

			self.lineEdit.clear() # Очистка текста после отправки

	def ConUi(self):  # Открытие окна настроек

		self.conwin.show()

	def log(self):

		if settings.logs == "True":

			self.pushButton.clicked.connect(self.logs) # Логгирование при нажатии на кнопку SEND

		else:

			pass # Ничего :D

	def logs(self):

		try:

			logfile('logs/rcon.log', maxBytes=1000000, backupCount=3)

			# Установка форматирования

			format = logging.Formatter('%(asctime)s: %(message)s');

			logzero.formatter(format)

			logger.info( self.sendcmd ) # Лог команд пользователя

			logger.info( self.servcmd ) # Лог команд с сервера

		except:

			pass

	def Stop(self):

		pass

def main():

	app = QApplication(sys.argv)
	window = URCON()
	app.exec_()

main()