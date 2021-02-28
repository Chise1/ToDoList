# -*- encoding: utf-8 -*-
"""
@File    : models.py
@Time    : 2021/2/28 8:29
@Author  : chise
@Email   : chise123@live.com
@Software: PyCharm
@info    :
"""

from sqlalchemy import Boolean, Column, Integer, String, DateTime, ForeignKey

from src.db import Base
from src.utils.password import make_password, verify_password
from datetime import datetime


class User(Base):
    __tablename__ = "user"
    id = Column(Integer, primary_key=True)
    username = Column(String(30), unique=True)
    password = Column(String(128), nullable=True)
    email = Column(String(128), nullable=False)
    is_active = Column(Boolean(), default=True)

    def set_password(self, raw_password: str):
        """
        设置密码
        :param raw_password:
        :return:
        """
        self.password = make_password(raw_password)

    def verify_password(self, raw_password: str) -> bool:
        """
        验证密码
        :param raw_password:
        :return:
        """
        return verify_password(raw_password, self.password)

    def __str__(self):
        return self.username


class Task(Base):
    __tablename__ = 'task'
    user_id = Column(ForeignKey('user.id'))
    id = Column(Integer, primary_key=True)
    checked = Column(Boolean(), default=False)
    created_time = Column(DateTime, default=datetime.now)
    finished_time = Column(DateTime)
