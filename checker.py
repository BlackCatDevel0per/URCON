import os, shutil

def CheckAppDataDir():

	current_dir = os.getcwd()
	homedir = os.path.expanduser("~")
	apppath_for_unix = '/.local/share/URCON/'

	if not os.path.exists(homedir + apppath_for_unix + 'src'):
		shutil.copytree(current_dir + '/src', homedir + apppath_for_unix + 'src')
"""
	if not os.path.exists("src"): # Ошибка при отцутствии ресурсов программы

		print("Error! NO /src!!!")
"""
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

		from version import APP_VERSION

		text_file.write("\nappversion = " + APP_VERSION) # app version
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
# Проверка OS
try:
	CheckAll()
except:
	if os.name == 'posix':
		current_dir = os.getcwd()
		home = os.path.expanduser("~")
		apppath_unix = '/.local/share/URCON/'

		if not os.path.exists(home + apppath_unix + 'src'): # проверка существования директории src в /.local/share
			shutil.copytree(current_dir + '/src', homedir + apppath_for_unix + 'src') # копирование файлов в /.local/share/URCON

		os.chdir(home + apppath_unix) # Смена директории программы
		CheckAll()

	if os.name == 'nt':
		pf = 'C://Program Files (x86)/'
		apppath_uis = 'URCON/'
		os.chdir(pf + apppath_uis)
		CheckAll()
