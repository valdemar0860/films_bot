import logging

from aiogram import executor, Dispatcher

import config

from init_bot_and_dispatcher import dp
from handlers import message_handler, error_handler, command_handler


async def aiogram_on_startup_polling(dispatcher: Dispatcher) -> None:
    await message_handler.register_handlers(dispatcher)
    await error_handler.register_handlers(dispatcher)
    await command_handler.register_handlers(dispatcher)


def main() -> None:
    if config.USE_WEBHOOK:
        pass
    else:
        logging.basicConfig(level=logging.INFO)
        executor.start_polling(dp, skip_updates=True, on_startup=aiogram_on_startup_polling)


if __name__ == '__main__':
    main()
