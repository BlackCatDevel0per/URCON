import os

def CheckAppDataDir():

	if os.path.exists("src") == False: # Ошибка при отцутствии ресурсов программы

		pass

def CheckDataDir():

	if os.path.exists("src/data") == False:

		os.mkdir("src/data")

def CheckConf():

	if os.path.isfile("src/data/config.ini") == False:

		sip = "0.0.0.0"
		sprt = "19132"
		spswd = "password"

		conf = text_file = open("src/data/config.ini", "w")

		text_file.write("[DATA]")

		text_file.write("\nip = " + sip )

		text_file.write("\nprt = " + sprt)

		text_file.write("\npswd = " + spswd )

		conf.close()

def CheckSettings():

	if os.path.isfile("src/data/settings.ini") == False:

		conf = text_file = open("src/data/settings.ini", "w")

		text_file.write("[SETTINGS]")

		text_file.write("\nlogs = False") # logs

		conf.close()

def CheckLogsDir():

	if os.path.exists("logs") == False:

		os.mkdir("logs")

def CheckAll():

	CheckAppDataDir()
	CheckDataDir()
	CheckConf()
	CheckSettings()
	CheckLogsDir()
# Проверка OS
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
