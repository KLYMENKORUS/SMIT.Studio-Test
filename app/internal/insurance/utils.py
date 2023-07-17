from functools import wraps
from abc import ABCMeta, abstractmethod
from fastapi import HTTPException, status
from tortoise.exceptions import DoesNotExist
from app.database import Insurance


# ********** DECORATORS **********
class InsuranceDoesNotExist:

    def __init__(self, message: str):
        self.message = message

    def __call__(self, func):
        @wraps(func)
        async def wrapper(*args, **kwargs):
            try:
                return await func(*args, **kwargs)
            except DoesNotExist:
                raise HTTPException(
                    status_code=status.HTTP_404_NOT_FOUND,
                    detail=self.message.format(args[1].cargo_type.value, args[1].date)
                )
        return wrapper


class InsuranceExists:

    def __init__(self, message: str):
        self.message = message

    def __call__(self, func):
        @wraps(func)
        async def wrapper(*args, **kwargs):
            if await Insurance.all().count():
                raise HTTPException(
                    status_code=status.HTTP_302_FOUND,
                    detail=self.message
                )
            else:
                return await func(*args, **kwargs)

        return wrapper


# ********** METACLASS **********
class MainService(metaclass=ABCMeta):

    @abstractmethod
    async def calculate_insurance(self, data):
        ...

    @abstractmethod
    async def all_by_cargo_type(self, cargo_type):
        ...

    @abstractmethod
    async def all_insurance(self):
        ...




