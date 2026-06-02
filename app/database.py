# Файл отвечает за соединение с PostgreSQL
from sqlalchemy.ext.asyncio import (
    AsyncSession,
    async_sessionmaker,
    create_async_engine,
)
from sqlalchemy.orm import DeclarativeBase

from app.config import settings


engine = create_async_engine(settings.database_url, echo=True) # подключение к базе

async_session_maker = async_sessionmaker( # создаёт сессию для запросов
    engine,
    class_=AsyncSession,
    expire_on_commit=False,
)


class Base(DeclarativeBase): # базовый класс для всех моделей
    pass


async def get_async_session(): # функция, которую FastAPI будет использовать в роутах
    async with async_session_maker() as session:
        yield session
