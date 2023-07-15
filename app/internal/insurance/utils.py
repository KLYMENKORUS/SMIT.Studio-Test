from functools import wraps
from abc import ABCMeta, abstractmethod
from fastapi import HTTPException, status
from tortoise.exceptions import DoesNotExist
from .schemas import InsuranceResponseList, InsuranceResponse


async def formatted_response(insurances: list) -> InsuranceResponseList:
    """Format a response"""
    return InsuranceResponseList(cargo_types=[InsuranceResponse(
        cargo_type=item.cargo_type,
        rate=item.rate,
        date=item.date
    ) for item in insurances])


class InsuranceDoesNotExist:

    def __init__(self, message):
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




