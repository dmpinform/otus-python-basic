import aiohttp
import asyncio
import requests
from loguru import logger
import json

# async def main():
#
#     async with aiohttp.ClientSession() as session:
#
#         pokemon_url = 'https://jsonplaceholder.typicode.com/users'
#         async with session.get(pokemon_url) as resp:
#             pokemon = await resp.json()
#             print(pokemon)
#
# asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
# asyncio.run(main())
logger.info("Start")

response = requests.get("https://jsonplaceholder.typicode.com/users")
todos = response.json()

response = requests.get("https://jsonplaceholder.typicode.com/posts")
todos1 = response.json()

logger.info("Finish")

#print(todos[0]["userId"])

# json_object = json.loads(str(users))
# pairs = json_object.items()

# file = open("url_response.txt", "w", encoding="UTF-8")
# with file as f_obj:
#      f_obj.write(json.dumps(result, indent=2, ensure_ascii=False))

# print(pairs.id)
