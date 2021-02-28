# -*- encoding: utf-8 -*-
"""
@File    : db.py
@Time    : 2021/2/28 9:54
@Author  : chise
@Email   : chise123@live.com
@Software: PyCharm
@info    :
"""
# Dependency
from src.db import SessionLocal


def get_db():
    with SessionLocal() as db:
        yield db
