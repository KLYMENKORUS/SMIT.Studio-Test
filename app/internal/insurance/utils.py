from functools import wraps
from abc import ABCMeta, abstractmethod
from fastapi import HTTPException, status
from tortoise.exceptions import DoesNotExist


def doesnt_exist(message):

    def decorator(func):

        @wraps(func)
        async def wrapper(*args, **kwargs):
            try:
                return await func(*args, **kwargs)
            except DoesNotExist:
                raise HTTPException(
                    status_code=status.HTTP_404_NOT_FOUND,
                    detail=message.format(args[0].cargo_type.value, args[0].date)
                )
        return wrapper

    return decorator


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




