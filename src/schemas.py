# -*- encoding: utf-8 -*-
"""
@File    : schemas.py
@Time    : 2021/2/28 9:50
@Author  : chise
@Email   : chise123@live.com
@Software: PyCharm
@info    :
"""
from pydantic import BaseModel


class LoginInfo(BaseModel):
    username: str
    password: str


class CrateTaskSchema(BaseModel):
    content: str
