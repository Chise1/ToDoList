# -*- encoding: utf-8 -*-
"""
@File    : auth.py
@Time    : 2021/2/28 9:04
@Author  : chise
@Email   : chise123@live.com
@Software: PyCharm
@info    :
"""
from typing import Any, List, Optional

from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError
from sqlalchemy import select
from sqlalchemy.orm import Session

from src import settings
from src.apis.depends.db import get_db
from src.models import User
from src.utils.token import decode_access_token

oauth2_scheme = OAuth2PasswordBearer(tokenUrl=settings.AUTH_TOKEN_URL)


def get_user(db: Session, username: str, ) -> Optional[User]:
    user = db.execute(
        select(User).where(User.username == username).where(User.is_active == True)
    ).scalar_one_or_none()
    return user


def authenticate_user(db: Session, username: str, password: str) -> Optional[User]:
    """
    验证密码
    """
    user = get_user(db, username)
    if not user:
        return None
    if not user.verify_password(password):
        return None
    return user


async def get_current_user(token: str = Depends(oauth2_scheme)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = decode_access_token(token)
        username: str = payload.get("sub")
        if username is None:
            raise credentials_exception
    except JWTError:
        raise credentials_exception
    user = await get_user(username=username)
    if user is None:
        raise credentials_exception
    return user


async def get_current_active_user(current_user: User = Depends(get_current_user)):
    if not current_user.is_active:
        raise HTTPException(status_code=400, detail="Inactive user")
    return current_user


async def get_superuser(current_user: User = Depends(get_current_active_user)):
    if not current_user.is_superuser:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN)
    return current_user


def get_user_has_perms(perms: List[Any]):
    """
    判定用户是否具有相关权限
    :param perms:
    :return:
    """

    async def user_has_perms(user: User = Depends(get_current_active_user)):
        if await user.has_perms(perms):
            return user
        else:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Incorrect username or password",
                headers={"WWW-Authenticate": "Bearer"},
            )

    return user_has_perms
