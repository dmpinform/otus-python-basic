"""
Домашнее задание №3
Асинхронная работа с сетью и бд

доработайте функцию main, по вызову которой будет выполняться полный цикл программы
(добавьте туда выполнение асинхронной функции async_main):
- создание таблиц (инициализация)
- загрузка пользователей и постов
    - загрузка пользователей и постов должна выполняться конкурентно (параллельно)
      при помощи asyncio.gather (https://docs.python.org/3/library/asyncio-task.html#running-tasks-concurrently)
- добавление пользователей и постов в базу данных
  (используйте полученные из запроса данные, передайте их в функцию для добавления в БД)
- закрытие соединения с БД
"""
from jsonplaceholder_requests import get_date_from_url
from models import (
    engine,
    Base,
    User,
    Post,
    async_session,
)
import asyncio


async def create_tables():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)


async def create_users(users):
    async with async_session() as session:
        async with session.begin():
            for user in users:
                session.add(User(
                            id=user["id"],
                            name=user["name"],
                            username=user["username"],
                            email=user["email"]))


async def create_posts(posts):
    async with async_session() as session:
        async with session.begin():
            for post in posts:
                session.add(Post(
                                id=post["id"],
                                userid=post["userId"],
                                title=post["title"],
                                body=post["body"]))


async def async_main():
    await create_tables()
    users, posts = await get_date_from_url()
    await create_users(users)
    await create_posts(posts)
    await engine.dispose()


def main():
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
    asyncio.run(async_main())


if __name__ == "__main__":
    main()
