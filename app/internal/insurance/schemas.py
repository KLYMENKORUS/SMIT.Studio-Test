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
    cargo_type: str = Field(..., examples=['Glass'])
    rate: Decimal = Field(..., examples=[0.04])
    date: datetime.date = Field(..., examples=[datetime.date(2023, 1, 1)])


class InsuranceResponseList(BaseModel):
    cargo_types: list[InsuranceResponse]

