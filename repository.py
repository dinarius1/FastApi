from sqlalchemy import select

from schema import STaskAdd, STask
from database import new_session, TaskOrm

# Работает как ВЬЮШКА и тесно связано с СЕССИЕЙ то есть тут прописываем как должны отрабатываться запросы по добавлению задач (post запрос), и запрос по выведению всех задач (get запрос)

class TaskReposotiry:
    @classmethod
    async def add_one(cls, data: STaskAdd):
        async with new_session() as session:
            task_dict = data.model_dump()

            task = TaskOrm(**task_dict)
            session.add(task)
            await session.flush()
            await session.commit()
            return task.id

    @classmethod
    async def find_all(cls) -> list[STask]:
        async with new_session() as session:
            query = select(TaskOrm)
            result = await session.execute(query)
            task_models = result.scalars().all()
            task_schemas = [STask.model_validate(task_model) for task_model in task_models]
            return task_schemas



'''
Создаем запрос на добавления задачи
1. Для этого создаем класс и используем декоратор для функции создания задачи
2. Указывем data : STaskAdd, так как нужно чтобы мы указывали все поля, кроме id, так как она автоматически сама создается
3. Открываем нашу сессию, которую мы сами создали в файле с database, и говорим, чтобы в ней была записана такие действия
4. task_dict = data.model_dump(): Преобразует объект STaskAdd в словарь
5. task = TaskOrm(**task_dict): Создает новый объект TaskOrm, используя распаковку словаря task_dict
6. 
await session.flush(): Записывает все изменения, сделанные в текущей сессии, в базу данных, но не фиксирует их окончательно. Это позволяет получить присвоенный ID задачи (если он генерируется базой данных).

await session.commit(): Фиксирует все изменения, сделанные в сессии, в базе данных.
'''




