# -*- encoding: utf-8 -*-
"""
@File    : password.py
@Time    : 2021/2/28 8:36
@Author  : chise
@Email   : chise123@live.com
@Software: PyCharm
@info    :
"""
# 主要用来处理密码加密
import binascii
import hashlib

from src import settings


def make_password(raw_password: str) -> str:
    """
    加密密码,返回加密的密码值和随机盐
    :param raw_password:
    :return:
    """
    password = hashlib.pbkdf2_hmac(
        "sha256", raw_password.encode("utf-8"), settings.SECRET_KEY.encode("utf-8"), 16
    )  # 随机生成盐值
    return binascii.hexlify(password).decode()


def verify_password(
    raw_password: str,
    password: str,
) -> bool:
    """
    验证密码是否正确
    :param raw_password:要验证的密码
    :param password:数据库存储的密码
    :param random_salt_b64:数据库存储的随机盐
    :return:
    """
    random_salt = settings.SECRET_KEY.encode("utf-8")
    raw_password = hashlib.pbkdf2_hmac("sha256", raw_password.encode("utf-8"), random_salt, 16)
    if binascii.hexlify(raw_password).decode() == password:
        return True
    else:
        return False
