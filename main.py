from database import create_tables, delete_tables
from contextlib import asynccontextmanager
from fastapi import FastAPI
from router import router as task_router

# Главный файл, который запускает наше приложение. Мы здесь прописываем функцию lifespan - цикл работы приложения, который производит функцию по созданию и дропанию таблиц, то есть нашу бд

@asynccontextmanager
async def lifespan(app: FastAPI):
    await delete_tables()
    print("База очищена")
    await create_tables()
    print("База готова к рабое")
    yield
    print('Выключено')


app = FastAPI(lifespan=lifespan)

app.include_router(task_router)