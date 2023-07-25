import logging

from aiogram import types, Dispatcher

from handlers.message_handler import search_movie_by_text, handle_search_result


async def handle_search_query(message: types.Message):
    query = message.text.strip('/search').strip()
    search_result = await search_movie_by_text(query)
    await handle_search_result(message.from_user.id, search_result)


async def register_handlers(dispatcher: Dispatcher):
    dispatcher.register_message_handler(handle_search_query, commands=['search'])
