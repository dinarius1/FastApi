from typing import Annotated
from fastapi import APIRouter, Depends
from schema import STaskAdd, STask, STaskId

from repository import TaskReposotiry

# Продолжение обработки данных от ВЬЮШКИ. Прописываем какая именно функция должна срабатывать при определенном запросе, и как данные должны отображаться

router = APIRouter(
    prefix='/tasks',
    tags=['Таски']
)


@router.post('')
async def add_task(
        task : Annotated[STaskAdd, Depends()]
) -> STaskId:    # ВОТ ЭТО АННОТАЦИЯ, КОТОРАЯ ГОВОРИТ ЧТО ДОЛЖНО ВЕРНУТЬСЯ СИЛЬНО ВЛИЯЕТ НА ФОРМАТ ДАННЫХ, КОТОРЫЕ МЫ ПОЛУЧАЕМ ПРИ ОБРАЩЕНИИ К ЭТОМУ ЗАПРОСУ. Потому что Фастапи смотрит на то, точно ли формат данных, которые мы указали в аннотаци совпадает с форматом выхода данных.

    # Кроме того, ОНО НЕПОСРЕДСТВЕННО СВЯЗЫВАЕТ ЗАПРОС со СХЕМОЙ, которая должна прилететь от этого запроса

    #task : STaskAdd - можно так, но придется все самому вручную воодить в Swagger, поэтому лучше исопльзовать такой формат, более красивое введение данных при запросе

    task_id = await TaskReposotiry.add_one(task)
    return {'ok' : True, 'task_id' : task_id}

@router.get('')
async def get_task() -> list[STask]:
    tasks = await TaskReposotiry.find_all()
    return tasks