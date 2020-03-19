#!venv/bin/python
import logging
import config
import utils

from aiogram import Bot, Dispatcher, executor, types

logging.basicConfig(level=logging.INFO)

bot = Bot(token=config.token)
dp = Dispatcher(bot)

# Configure logging
logging.basicConfig(level=logging.INFO)


# if the text from user in the list
@dp.message_handler(text=['text1', 'text2'])
async def text_in_handler(message: types.Message):
    await message.answer("The message text equals to one of in the list!")\



# checks specified chat
@dp.message_handler(chat_id=205993908)
async def handle_specified(msg: types.Message):
    await msg.answer("You are an admin of the specified chat!")



# @dp.message_handler()
# async def echo(message: types.Message):
#     await message.reply(message.chat.id)


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
