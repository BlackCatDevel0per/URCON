from PyQt5 import uic
from PyQt5.QtWidgets import (QWidget)

class About(QWidget):

	def __init__(self):
		super(About, self).__init__()
		uic.loadUi('src/windows/about.ui', self)
		from settings import AppVersion
		self.label_4.setText(AppVersion)
		from setlang import SetAboutWindowLang
		SetAboutWindowLang(self)