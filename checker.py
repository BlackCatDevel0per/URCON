import os

def CheckAppDataDir():

	if not os.path.exists("src"): # Ошибка при отцутствии ресурсов программы

		print("Error! NO /src!!!")

def CheckDataDir():

	if not os.path.exists("src/data"):

		os.mkdir("src/data")

def CheckConf():

	if not os.path.isfile("src/data/config.ini"):

		sip = "0.0.0.0"
		sprt = "19132"
		spswd = "password"

		conf = text_file = open("src/data/config.ini", "w")

		text_file.write("[DATA]")

		text_file.write("\nip = " + sip )

		text_file.write("\nprt = " + sprt)

		text_file.write("\npswd = " + spswd )

		conf.close()

def CheckLanguageFile():
	if not os.path.isfile("src/languages/en_us.ini"):
		print("Language file not found")

def CheckSettings():

	if not os.path.isfile("src/data/settings.ini"):

		conf = text_file = open("src/data/settings.ini", "w")

		text_file.write("[SETTINGS]")

		text_file.write("appversion = VERSION =)") # app version

		text_file.write("\nlogs = False") # logs

		text_file.write("\nlang = en_us") # language

		conf.close()

def CheckLogsDir():

	if not os.path.exists("logs"):

		os.mkdir("logs")

def CheckAll():

	CheckAppDataDir()
	CheckDataDir()
	CheckConf()
	CheckLanguageFile()
	CheckSettings()
	CheckLogsDir()
# Проверка OS (пока временная)
try:
	CheckAll()
except:
	if os.name == 'posix':
		pass
	if os.name == 'nt':
		pf = 'C://Program Files (x86)/'
		apppath = 'URCON/'
		os.chdir(pf + apppath)
		CheckAll()
