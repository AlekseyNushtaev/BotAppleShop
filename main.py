import asyncio
import logging
from aiogram import Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage

import handlers
from bot import bot

logger: logging.Logger = logging.getLogger(__name__)


async def main() -> None:
    """
    Основная функция запуска бота.
    Настраивает логирование, хранилище и запускает поллинг.
    """
    logging.basicConfig(
        level=logging.INFO,
        format='%(filename)s:%(lineno)d %(levelname)-8s [%(asctime)s] - %(name)s - %(message)s'
    )
    logging.info('Starting bot')

    storage: MemoryStorage = MemoryStorage()
    dp: Dispatcher = Dispatcher(storage=storage)
    dp.include_router(handlers.router)

    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())
