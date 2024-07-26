from typing import Optional

from pydantic import BaseModel

# По факту это файл как сериализатор, в котором мы говорим, какие данные он должен обработать от таблицы TaskORM. Рассматривай ее как СХЕМУ АНАЛИЗА ТАБЛИЦ ДЛЯ ВЬЮШКИ

class STaskAdd(BaseModel):
    name: str
    description: Optional[str] = None

class STask(STaskAdd):
    id : int


class STaskId(BaseModel):
    ok: bool = True
    task_id: int