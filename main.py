import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command

# ВСТАВТЕ СВІЙ ТОКЕН СЮДИ
API_TOKEN = '1973181689:AAHxfpNNr3Mof5jjJPLIvWSfmCiKFc5TPQU'

bot = Bot(token=API_TOKEN)
dp = Dispatcher()

@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    await message.answer("Привіт! Я твій планувальник. Давай складемо план на рік?")

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
