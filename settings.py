import configparser

config = configparser.ConfigParser()  # создаём объекта парсера
config.read("src/data/settings.ini")  # читаем конфиг

logs = str(config["SETTINGS"]["logs"])