"""
создайте асинхронные функции для выполнения запросов к ресурсам (используйте aiohttp)
"""
import asyncio
from aiohttp import ClientSession
from loguru import logger

USERS_DATA_URL = "https://jsonplaceholder.typicode.com/users"
POSTS_DATA_URL = "https://jsonplaceholder.typicode.com/posts"
urls = [USERS_DATA_URL, POSTS_DATA_URL]


async def fetch_json(session: ClientSession, url: str) -> dict:
    async with session.get(url) as response:
        return await response.json()


async def fetch_date(url):
    async with ClientSession() as session:
        result = await fetch_json(session, url)
    return result


async def get_date_from_url():
    tasks = [
        asyncio.create_task(fetch_date(url))
        for url in urls
    ]
    return await asyncio.gather(*tasks)





