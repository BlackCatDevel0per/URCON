import configparser

config = configparser.ConfigParser()  # создаём объекта парсера
config.read("src/data/config.ini")  # читаем конфиг

ip = str(config["DATA"]["ip"])
prt = int(config["DATA"]["prt"])
pswd = str(config["DATA"]["pswd"])