from fastapi import APIRouter
from .schemas import CalculateRequest, CalculateResponse, InsuranceResponseList
from .services import Service
from .utils import formatted_response
from app.database import CargoTypes


router = APIRouter(prefix='/api/v1/insurance', tags=['insurance'])


class InsuranceService:

    @staticmethod
    @router.post('/calculate', response_model=CalculateResponse)
    async def calculate(data: CalculateRequest) -> CalculateResponse:
        insurance = await Service.calculate_insurance(data)
        return CalculateResponse(insurance_value=insurance)

    @staticmethod
    @router.get('/all_by_cargo_type', response_model=InsuranceResponseList)
    async def all_by_cargo_type(cargo_type: CargoTypes) -> InsuranceResponseList:
        cargo_types = await Service.all_by_cargo_type(cargo_type)
        return await formatted_response(cargo_types)

    @staticmethod
    @router.get('all', response_model=InsuranceResponseList)
    async def all_insurance() -> InsuranceResponseList:
        insurances = await Service.all_insurance()
        return await formatted_response(insurances)
