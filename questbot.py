from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor



bot = Bot(token="5854637694:AAFj7adRQdGoNnDZpFtD4HeqMrhseKMlP0c")
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def process_start_command(message: types.Message):
    await message.reply("Hello! Enter 3 numbers you got as result of your quest.")


@dp.message_handler(commands=['help'])
async def process_help_command(message: types.Message):
    await message.reply(""" Enter 3 numbers you got as result of your quest!
answer shoud be XXX format (for example 123)""")

@dp.message_handler()
async def echo_message(msg: types.Message):
    ans ='172'
    if ans == msg.text:
        await bot.send_message(msg.from_user.id, """Good Job! You have completed your quest!
Now go to Chess Club for the task 4
Chess Club is located in the 3rd block on the 1st floor
        """)
    else:
        await bot.send_message(msg.from_user.id, "Incorrect code! Try again!")



if __name__ == '__main__':
    executor.start_polling(dp)
    

