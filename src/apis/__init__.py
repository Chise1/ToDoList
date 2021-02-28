# -*- encoding: utf-8 -*-
"""
@File    : __init__.py.py
@Time    : 2021/2/28 0:27
@Author  : chise
@Email   : chise123@live.com
@Software: PyCharm
@info    :
"""
from fastapi import FastAPI

from src.apis.routes.auth import auth_router
from src.apis.routes.todo import todo_router

todo_list_app = FastAPI(title="ToDo list")
todo_list_app.include_router(auth_router)
todo_list_app.include_router(todo_router)