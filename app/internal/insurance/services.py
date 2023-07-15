from decimal import Decimal
from app.database import Insurance
from .utils import MainService, InsuranceDoesNotExist
from .schemas import CalculateRequest


class Service(MainService):

    @classmethod
    @InsuranceDoesNotExist('There is no insurance with cargo type `{}` for date `{}`')
    async def calculate_insurance(cls, data: CalculateRequest) -> Decimal:
        """Calculates declared value with ensurance rate"""
        insurance = await Insurance.get(date=data.date, cargo_type=data.cargo_type.value)
        return data.declared_value * insurance.rate

    @classmethod
    async def all_by_cargo_type(cls, cargo_type: str) -> list[Insurance]:
        """Returns all the insurance for a given cargo type"""
        all_cargo_type = await Insurance.filter(cargo_type=cargo_type).all()
        return all_cargo_type

    @classmethod
    async def all_insurance(cls) -> list[Insurance]:
        """Returns all the insurance"""
        return await Insurance.all()

