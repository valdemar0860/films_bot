# import os
# import asyncpg
#
# # connect to the PostgresSQL database
# # database_url = os.environ['DATABASE_URL']
# # db_pool = asyncpg.create_pool(database_url)
#
#
#
# async def save_search_result(user_id, movie_title, movie_year, movie_imdb_url, movie_img_url, success=True):
#     async with db_pool.acquire() as conn:
#         await conn.execute(
#             """
#                 INSERT INTO search_history (user_id, movie_title, movie_year, movie_imdb_url, movie_img_url, success)
#                 VALUES ($1, $2, $3, $4, $5, $6)
#             """,
#             user_id, movie_title, movie_year, movie_imdb_url, movie_img_url, success
#         )
