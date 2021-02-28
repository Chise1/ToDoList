# -*- encoding: utf-8 -*-
"""
@File    : auth.py
@Time    : 2021/2/28 8:58
@Author  : chise
@Email   : chise123@live.com
@Software: PyCharm
@info    :
"""
from datetime import timedelta

from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from starlette import status

from src import settings
from src.apis.depends.auth import authenticate_user
from src.apis.depends.db import get_db
from src.schemas import LoginInfo
from src.utils.token import create_access_token

auth_router = APIRouter(tags=['auth'])


@auth_router.post("/auth/token")
def login(user_info: LoginInfo,db:Session=Depends(get_db)):
    """
    仅用于docs页面测试返回用
    """
    user = authenticate_user(db,user_info.username, user_info.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": user.username, "id": user.id}, expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer"}


@auth_router.post("/register")
def register_user(username: str, password: str, email: str):
    """
    注册用户
    :param username:
    :param password:
    :return:
    """
