import datetime
from decimal import Decimal
from pydantic import BaseModel, Field
from app.database import CargoTypes


class CalculateRequest(BaseModel):
    date: datetime.date
    cargo_type: CargoTypes
    declared_value: Decimal


class CalculateResponse(BaseModel):
    insurance_value: Decimal


class InsuranceResponse(BaseModel):
    cargo_type: str = Field(..., example='Glass')
    rate: Decimal = Field(..., example=0.04)
    date: datetime.date = Field(..., example=datetime.date(2023, 1, 1))


class InsuranceResponseList(BaseModel):
    cargo_types: list[InsuranceResponse]

