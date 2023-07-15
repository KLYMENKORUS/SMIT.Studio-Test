import datetime
from decimal import Decimal
from pydantic import BaseModel
from app.database import CargoTypes


class CalculateRequest(BaseModel):
    date: datetime.date
    cargo_type: CargoTypes
    declared_value: Decimal


class CalculateResponse(BaseModel):
    insurance_value: Decimal

