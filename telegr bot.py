from aiogram import Bot, types
from aiogram import Bot, Dispatcher, executor, types
from aiogram.utils import executor
from dotenv import load_dotenv
load_dotenv()


import os

token = '5658654960:AAEl6z70cVwh1iQPyLSN6UO51oYkBFqCCHI'
bot = Bot(token)
dp = Dispatcher(bot)


# @dp.message_handler() # Сюда попадаю сообщения
# async def echo_send(message : types.Message):
#     if message.text == "привет":
#         await message.answer("И тебе привет")
#     # await message.answer(message.text) # просто отвечает
#     # await message.reply (message.text) # комментирует входящее сообщение
#     await bot.send_message(message.from_user.id, message.text)# отправляет в личку, если написал уже

@dp.message_handler(commands = ['start', 'help']) # кнопки старт и хелп
async def command_start(message : types.Message):
    try: #Если не получится отправить в личку, так как бот в личку сам писать не может
        await bot.send_message(message.from_user.id, 'Приятного аппетита')
        await message.delete()
    except:
         message.reply('Общение с ботом через лс, напишите ему: https://t.me/Electronic_shopBot')

@dp.message_handler(commands = ['Режим_работы']) # кнопки старт и хелп
async def open_comand(message : types.Message):
    await bot.send_message(message.from_user.id, 'Вс-Чт с 9:00 до 23:00')

@dp.message_handler(commands = ['Расположение']) # кнопки старт и хелп
async def open_comand(message : types.Message):
    await bot.send_message(message.from_user.id, 'Уральская 41')



executor.start_polling(dp, skip_updates=True) # когда бот не онлайн не отвечает на прошлые сообщеения
