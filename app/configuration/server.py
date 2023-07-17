from fastapi import FastAPI
from tortoise.contrib.fastapi import register_tortoise
from app.configuration.routes import __routes__
from app.configuration import settings


class Server:

    __app: FastAPI

    def __init__(self, app):
        self.__app = app
        self.__register_tortoise(self.__app)
        self.__register_routes(self.__app)

    def get_app(self) -> FastAPI:
        return self.__app

    def __register_tortoise(self, app):
        register_tortoise(
            app=app,
            config=settings.DB_CONFIG,
            generate_schemas=False
        )

    @staticmethod
    def __register_routes(app):
        __routes__.register_routes(app)
