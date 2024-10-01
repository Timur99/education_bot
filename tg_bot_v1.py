import json
import time
from aiogram import Bot, Dispatcher, types
from aiogram.types import ContentType
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
import asyncio
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.filters.command import Command
from aiogram.filters import Command
from aiogram.types import FSInputFile

import json
from pydub import AudioSegment
from aiogram import Bot, Dispatcher, types
from aiogram.types import FSInputFile
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, FSInputFile
from aiogram import F

import logging

from scriptss.config import load_credentials, DB_CREDENTIALS, TGRM_BOT_CREDENTIALS, OPENAI_API
from dotenv import load_dotenv
import os

from scriptss.llm_script import get_tasks

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Создаем обработчик для вывода в консоль
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.INFO)

# Добавляем обработчик к логгеру
logger.addHandler(console_handler)



# Загрузка переменных окружения
load_dotenv()

# Объект бота

TOKEN = os.getenv('TG', load_credentials(TGRM_BOT_CREDENTIALS)['tg_test'])
bot = Bot(token=TOKEN)

# Диспетчер
dp = Dispatcher()

logger.info("This is an informational message")
print("This is a print statement")


class UserSession:
    def __init__(self):
        self.name_profession = ''
        self.name = ''
        self.contact = ''
        self.experience = ''
        self.education = ''
        self.skills = ''
        self.read = ''
        self.state = 'start'
        self.json_user = ''
        self.cover_letter = ''


user_sessions = {}


def get_user_session(user_id):
    if user_id not in user_sessions:
        user_sessions[user_id] = UserSession()
    return user_sessions[user_id]


start_message = '''Привет! Это EduAI - твой ИИ-помощник в обучении. 
Команда чтобы начать /tasks'''


@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    await bot.send_message(message.chat.id, text=start_message)



@dp.message(Command("tasks"))
async def cover_letter(message: types.Message):
    user_id = message.from_user.id
    print(user_id)
    user_session = get_user_session(user_id)

    objects = 'python'
    rang = 'easy'

    result = get_tasks(objects, rang)

    first_button = InlineKeyboardButton(text="A", callback_data="1")
    second_button = InlineKeyboardButton(text="B", callback_data="2")
    third_button = InlineKeyboardButton(text="C", callback_data="3")
    four_button = InlineKeyboardButton(text="D", callback_data="4")
    keyboard = InlineKeyboardMarkup(inline_keyboard=[[first_button, second_button], [third_button,four_button]])

    sent_message = await bot.send_message(message.chat.id, result,
                                           reply_markup=keyboard)


# Запуск процесса поллинга новых апдейтов
async def main():
    try:
        await dp.start_polling(bot)
    except Exception as e:
        logger.error(f"Критическая ошибка в main(): {e}", exc_info=True)


if __name__ == "__main__":
    asyncio.run(main())
