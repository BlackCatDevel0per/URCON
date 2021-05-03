import configparser
import settings
import os

config = configparser.ConfigParser()  # создаём объекта парсера

##########
def SetLangEN(self):
	config2 = configparser.ConfigParser()
	set_en_conf = "src/data/settings.ini"
	config2.read(set_en_conf)
	config2.set("SETTINGS", "lang", "en_us")
	config2.write(open(set_en_conf, "w"))


def SetLangRU(self):
	config2 = configparser.ConfigParser()
	set_ru_conf = "src/data/settings.ini"
	config2.read(set_ru_conf)
	config2.set("SETTINGS", "lang", "ru_ru")
	config2.write(open(set_ru_conf, "w"))

##########
config.read("src/languages/en_us.ini")  # читаем конфиг
#####

def MWLang(self): # Замена текста
	# English
	self.EN_MainWindow_MENU = config["en_us"]["MainWindow_MENU"]
	self.EN_MainWindow_SETLANGUAGE = config["en_us"]["MainWindow_SETLANGUAGE"]
	self.EN_MainWindow_SEND = config["en_us"]["MainWindow_SEND"]
	self.EN_MainWindow_Connect = config["en_us"]["MainWindow_Connect"]
	self.EN_MainWindow_ConnectionError = config["en_us"]["MainWindow_ConnectionError"]
	self.EN_ConnectionLost = config["en_us"]["MainWindow_ConnectionLost"]

	# Русский
	self.RU_RconConnectionError = "Ошибка подключения!"
	self.RU_ConnectionLost = 'Соеденение разорвано!'

def MWSetLang(self):
	global RconConnectionError, ConnectionLost

	if settings.language == "en_us":
		SetMainWindowLangEN(self)

	elif settings.language == "ru_ru":
		RconConnectionError = self.RU_RconConnectionError
		ConnectionLost = self.RU_ConnectionLost

	else:
		print("Ошибка! этого языка пока нет в этой программе")

def SetMainWindowLangEN(self):
	global RconConnectionError, ConnectionLost

	self.menurcon.setTitle(self.EN_MainWindow_MENU)
	self.langmenu.setTitle(self.EN_MainWindow_SETLANGUAGE)
	self.pushButton.setText(self.EN_MainWindow_SEND)
	self.connectui.setText(self.EN_MainWindow_Connect)
	RconConnectionError = self.EN_MainWindow_ConnectionError
	ConnectionLost = self.EN_ConnectionLost

def SetMainWindowLang(self):
	MWLang(self)
	MWSetLang(self)

#####

def CWLang(self): ###
	# English
	self.EN_ConnectWindow_Title = config["en_us"]["ConnectWindow_Title"]
	self.EN_ConnectWindow_SetPort = config["en_us"]["ConnectWindow_SetPort"]
	self.EN_ConnectWindow_Password = config["en_us"]["ConnectWindow_Password"]
	self.EN_ConnectWindow_EnableLogs_CheckBox = config["en_us"]["ConnectWindow_EnableLogs_CheckBox"]
	self.EN_ConnectWindow_OpenLogs_Button = config["en_us"]["ConnectWindow_OpenLogs_Button"]

def CWSetLang(self):

	if settings.language == "en_us":
		SetConnectWindowLangEN(self)

	elif settings.language == "ru_ru":
		pass

	else:
		print("Ошибка! этого языка пока нет в этой программе")

def SetConnectWindowLangEN(self):
	self.setWindowTitle(self.EN_ConnectWindow_Title)
	self.label_2.setText(self.EN_ConnectWindow_SetPort)
	self.label_3.setText(self.EN_ConnectWindow_Password)
	self.checkBox.setText(self.EN_ConnectWindow_EnableLogs_CheckBox)
	self.pushButton_2.setText(self.EN_ConnectWindow_OpenLogs_Button)

def SetConnectWindowLang(self):
	CWLang(self)
	CWSetLang(self)

#####

def AWLang(self): ###
	# English
	self.EN_AboutWindow_Title = config["en_us"]["AboutWindow_Title"]
	self.EN_AboutWindow_Developer = config["en_us"]["AboutWindow_Developer"]
	self.EN_AboutWindow_IconFrom = config["en_us"]["AboutWindow_IconFrom"]
	self.EN_AboutWindow_BugsReport = config["en_us"]["AboutWindow_BugsReport"]

def AWSetLang(self):

	if settings.language == "en_us":
		SetAboutWindowLangEN(self)

	elif settings.language == "ru_ru":
		pass

	else:
		print("Ошибка! этого языка пока нет в этой программе")

def SetAboutWindowLangEN(self):
	self.setWindowTitle(self.EN_AboutWindow_Title)
	self.label.setText(self.EN_AboutWindow_Developer)
	self.label_3.setText(self.EN_AboutWindow_IconFrom)
	self.label_7.setText(self.EN_AboutWindow_BugsReport)

def SetAboutWindowLang(self):
	AWLang(self)
	AWSetLang(self)