from fastapi import APIRouter
from .schemas import CalculateRequest, CalculateResponse,\
    InsuranceResponseList, InsuranceResponse
from .services import Service


router = APIRouter(prefix='/api/v1/insurance')


class InsuranceService:

    @staticmethod
    @router.post('/calculate', response_model=CalculateResponse)
    async def calculate(data: CalculateRequest) -> CalculateResponse:
        insurance = await Service.calculate_insurance(data)
        return CalculateResponse(insurance_value=insurance)

    @staticmethod
    @router.get('/all_by_cargo_type', response_model=InsuranceResponseList)
    async def all_by_cargo_type(cargo_type: str) -> InsuranceResponseList:
        cargo_types = await Service.all_by_cargo_type(cargo_type)
        return InsuranceResponseList(cargo_types=[InsuranceResponse(
            cargo_type=item.cargo_type,
            rate=item.rate,
            date=item.date
        ) for item in cargo_types])
