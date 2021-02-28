# -*- encoding: utf-8 -*-
"""
@File    : todo.py
@Time    : 2021/2/28 11:05
@Author  : chise
@Email   : chise123@live.com
@Software: PyCharm
@info    :
"""
from typing import List, Optional

from fastapi import APIRouter, Depends
from sqlalchemy import select
from sqlalchemy.orm import Session

from src.apis.depends.db import get_db
from src.models import User, Task
from src.schemas import CrateTaskSchema, ListTaskSchema, ResultListTaskSchema
from src.apis.depends.auth import get_current_active_user

todo_router = APIRouter(tags=['todo'])


@todo_router.post("/task")
def create_task(task: CrateTaskSchema):
    pass


@todo_router.get("/tasks", response_model=ResultListTaskSchema)
def get_tasks(
    last: Optional[int] = None,
    user: User = Depends(get_current_active_user), session: Session = Depends(get_db)):
    """
    加载数据
    :param user:
    :return:
    """
    if not last:
        tasks = session.execute(
            select(Task).where(User.id == user.id).limit(100)
        )


