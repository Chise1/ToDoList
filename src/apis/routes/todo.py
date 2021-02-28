# -*- encoding: utf-8 -*-
"""
@File    : todo.py
@Time    : 2021/2/28 11:05
@Author  : chise
@Email   : chise123@live.com
@Software: PyCharm
@info    :
"""
from fastapi import APIRouter

from src.schemas import CrateTaskSchema

todo_router = APIRouter(tags=['todo'])

@todo_router.post("/task")
def create_task(task:CrateTaskSchema):
    pass