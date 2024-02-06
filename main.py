
import asyncio
import aiogram

import config

TOKEN = config.TOKEN
dp = aiogram.Dispatcher()


async def main() -> None:
    bot = aiogram.Bot(TOKEN)
    await dp.start_polling(bot)


@dp.message(aiogram.filters.CommandStart())
async def command_start_handler(message: aiogram.types.Message) -> None:
    await message.answer("Прайс-аггрегатор")


if __name__ == "__main__":
    asyncio.run(main())

