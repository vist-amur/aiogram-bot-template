from environs import Env

# Теперь используем вместо библиотеки python-dotenv библиотеку environs
env = Env()
env.read_env()

BOT_TOKEN = env.str("BOT_TOKEN")  # Забираем значение типа str
ADMINS = env.list("ADMINS")  # Тут у нас будет список из админов
IP = env.str("ip")  # Тоже str, но для айпи адреса хоста
PUB1C = env.str("pub1c")  # Адрес публикации базы 1С
LOGIN1C = env.str("login1c")  # Логин базы 1С
PASS1C = env.str("pass1c")  # Пароль пользователя 1С

