from tortoise import Tortoise
from app.configuration import settings


class DBInitial:

    @classmethod
    async def init_db(cls) -> None:
        await Tortoise.init(config=settings.DB_CONFIG)
