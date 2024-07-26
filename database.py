from typing import Optional

from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column

# Файл по созданию бд и его подключению к приложению. Здесь прописывается как выглядит полная модель таблицы TaskORM и функция create_tables и drop_tables



#async_sessionmaker - фабрика по созданию сессий, позволяет проводить транзакции

# Создаем наш асинхронный движок, который позволяет работать с бд путем отправления запроса

engine = create_async_engine(
    'sqlite+aiosqlite:///tasks.db'
)
'''
sqlite - название бд
aiosqlite - драйвер
tasks.db - название файла, где будет вся наша бд
'''

new_session = async_sessionmaker(engine, expire_on_commit=False)
# создаем новую сессию, где будет запущен наш движок

class Model(DeclarativeBase):
    pass

class TaskOrm(Model):
    __tablename__ = 'tasks'

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]
    description: Mapped[Optional[str]]

    #Cоздаем таблицу и описываем, какие должны у него быть поля

async def create_tables():
    async with engine.begin() as conn:
        await conn.run_sync(Model.metadata.create_all)

#  создаем асинхронную функцию, тк у нас асинхронный драйвер, где говорим, что нужно создать таблицу, которую мы просписали сверху


async def delete_tables():
    async with engine.begin() as conn:
        await conn.run_sync(Model.metadata.drop_all)

#функция по удалению всей таблицы