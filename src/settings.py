# -*- encoding: utf-8 -*-
"""
@File    : settings.py
@Time    : 2021/2/28 0:26
@Author  : chise
@Email   : chise123@live.com
@Software: PyCharm
@info    :
"""
import os

import dotenv

DEBUG = True
dotenv.load_dotenv()
SECRET_KEY = os.getenv("SECRET_KEY")
SQLALCHEMY_DATABASE_URL = "mysql://todolist:todolist@localhost/todolist"
AUTH_TOKEN_URL = '/auth/token'
ALGORITHM = "HS256"  # 加密算法
ACCESS_TOKEN_EXPIRE_MINUTES = 30  # 过期时间
