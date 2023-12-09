from __future__ import annotations

from PySide6.QtUiTools import loadUiType

from typing import TYPE_CHECKING

if TYPE_CHECKING:
	from PySide6.QtWidgets import QWidget


ui_cls: object
base_cls: QWidget

# TODO: On build package autouic.. (uis to code) Hmm..
ui_cls, base_cls = loadUiType('src/uis/about.ui')


class About(ui_cls, base_cls):

	def __init__(self):
		super().__init__()

		self.setupUi(self)

		from settings import AppVersion
		self.label_4.setText(AppVersion)  ##
		from setlang import SetAboutWindowLang
		SetAboutWindowLang(self)  ##
