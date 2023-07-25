import logging
from aiogram import types, Dispatcher
from aiogram.types import InputFile

from init_bot_and_dispatcher import bot
from movie_search import MovieSearch, MovieSearchResult

logging.basicConfig(level=logging.INFO)


async def send_welcome(message: types.Message):
    await message.reply("Hi! I'm the movie search bot. Send me a screenshot or description of a movie "
                        "you want me to search for.")


async def search_movie_by_image(file_url):
    # implement image search logic
    return MovieSearchResult("Sample Movie", "2021",
                             "https://www.imdb.com/title/tt0000000", "") # sample MovieSearchResult


async def search_movie_by_text(query):
    search_result = MovieSearch(query)
    await search_result.search()
    return search_result.results


async def send_movie_result(user_id, result, file_url=None):
    caption = f"{result.title} ({result.year})\n{result.link}"
    img_url = result.img_url

    if file_url:
        await bot.send_photo(user_id, InputFile(file_url), caption=caption)
        # await delete_image(file_url)
    elif img_url:
        await bot.send_photo(user_id, img_url, caption=caption)
    else:
        await bot.send_message(user_id, caption)


async def handle_search_result(user_id, search_result, file_url=None):
    if not search_result:
        await bot.send_message(user_id, "Sorry, I couldn't find anything.")
        return

    for result in search_result:
        await send_movie_result(user_id, result, file_url)

        # save the search result to the user's search history
        # await save_search_result(user_id, result.title, result.year, result.link, result.img_url)


async def handle_screenshot(message):
    photo = message.photo[-1]
    file_id = photo.file_id
    file = await bot.get_file(file_id)
    file_url = bot.get_file_url(file.file_path)
    search_result = await search_movie_by_image(file_url)
    await handle_search_result(message.from_user.id, search_result, file_url)


async def register_handlers(dispatcher: Dispatcher):
    dispatcher.register_message_handler(send_welcome, commands=['start', 'help'])
    dispatcher.register_message_handler(handle_screenshot, content_types=['photo'])




