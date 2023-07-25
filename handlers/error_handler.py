import logging

from aiogram import Dispatcher
from aiogram.utils.exceptions import BotBlocked, ChatNotFound, UserDeactivated, MessageToDeleteNotFound

import config
from init_bot_and_dispatcher import bot, dp


@dp.errors_handler()
async def error_handler(update, error):
    logging.exception(f"update {update} caused error {error}")
    if isinstance(error, BotBlocked):
        return True
    elif isinstance(error, ChatNotFound):
        return True
    elif isinstance(error, UserDeactivated):
        return True
    elif isinstance(error, MessageToDeleteNotFound):
        return True
    else:
        await bot.send_message(chat_id=config.ADMIN_CHAT_ID, text=f"Unhandled exception: {error}")
        return False


async def register_handlers(dispatcher: Dispatcher):
    dispatcher.register_errors_handler(error_handler)
