import configparser

config = configparser.ConfigParser()  # создаём объекта парсера
config.read("src/data/settings.ini")  # читаем конфиг

AppVersion = config["SETTINGS"]["appversion"]
logs = str(config["SETTINGS"]["logs"])
language = str(config["SETTINGS"]["lang"])