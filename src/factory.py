# -*- encoding: utf-8 -*-
"""
@File    : factory.py
@Time    : 2021/2/28 8:28
@Author  : chise
@Email   : chise123@live.com
@Software: PyCharm
@info    :
"""
from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

# def init_app(main_app: Starlette):
#     @main_app.on_event("startup")
#     async def startup() -> None:
#         await AsyncRedisUtil.init(**settings.REDIS)
#
#     @main_app.on_event("shutdown")
#     async def shutdown() -> None:
#         await AsyncRedisUtil.close()
from src import settings
from src.apis import todo_list_app


def create_app() -> FastAPI:
    """
    这里是创建app或导入其他app的地方
    :return:
    """
    app = FastAPI(title="ToDo List", debug=settings.DEBUG)
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )
    app.mount("/api", todo_list_app)
    # Sentry的插件
    # app.add_middleware(SentryAsgiMiddleware)
    return app
