import telebot
from config import (
    bot_config,
    db_config,
)


bot = telebot.TeleBot(bot_config.TOKEN.get_secret_value());

