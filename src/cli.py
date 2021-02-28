# -*- encoding: utf-8 -*-
"""
@File    : cli.py
@Time    : 2021/2/28 10:13
@Author  : chise
@Email   : chise123@live.com
@Software: PyCharm
@info    :
"""
import typer
from src import settings
from src.apis.depends.db import get_db
app = typer.Typer()


@app.command()
def create_superuser(username: str, password: str, email: str):
    """
    创建超级用户
    """
    from src.models import User
    session = next(get_db())
    user = User(
        username=username,
        email=email,
    )
    user.set_password(password)
    session.add(user)
    session.commit()
    session.flush()
    print(f"创建{username}成功")


def main():
    app()


if __name__ == "__main__":
    main()
