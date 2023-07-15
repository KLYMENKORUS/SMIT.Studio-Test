from decimal import Decimal
from app.database import Insurance
from .utils import doesnt_exist
from .schemas import CalculateRequest


@doesnt_exist('There is no insurance with cargo type `{}` for date `{}`')
async def calculate_insurance(data: CalculateRequest) -> Decimal:
    """Calculates declared value with ensurance rate"""
    insurance = await Insurance.get(date=data.date, cargo_type=data.cargo_type.value)
    return data.declared_value * insurance.rate
