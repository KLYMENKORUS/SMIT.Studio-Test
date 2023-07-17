from http import HTTPStatus
from typing import Annotated

from fastapi import APIRouter, Depends

from .schemas import CalculateRequest, CalculateResponse, InsuranceResponseList, \
    SuccessInsuranceCreate, InsuranceResponse
from .services import Service
from app.database import CargoTypes


async def formatted_response(insurances: list) -> InsuranceResponseList:
    """Format a response"""
    return InsuranceResponseList(cargo_types=[InsuranceResponse(
        cargo_type=item.cargo_type,
        rate=item.rate,
        date=item.date
    ) for item in insurances])


router = APIRouter(prefix='/api/v1/insurance', tags=['insurance'])


class InsuranceService:

    @staticmethod
    @router.post('/create', response_model=SuccessInsuranceCreate)
    async def create_insurance(service: Annotated[Service, Depends(Service)]) -> SuccessInsuranceCreate:
        await service.create_insurance()

        return SuccessInsuranceCreate(
            status=HTTPStatus.OK,
            message='insurance successfully created'
        )

    @staticmethod
    @router.post('/calculate', response_model=CalculateResponse)
    async def calculate(data: CalculateRequest, service: Annotated[Service, Depends(Service)]) -> CalculateResponse:
        insurance = await service.calculate_insurance(data)
        return CalculateResponse(insurance_value=round(insurance, 2))

    @staticmethod
    @router.get('/all_by_cargo_type', response_model=InsuranceResponseList)
    async def all_by_cargo_type(
            cargo_type: CargoTypes, service:
            Annotated[Service, Depends(Service)]
    ) -> InsuranceResponseList:
        cargo_types = await service.all_by_cargo_type(cargo_type)
        return await formatted_response(cargo_types)

    @staticmethod
    @router.get('/all', response_model=InsuranceResponseList)
    async def all_insurance(service: Annotated[Service, Depends(Service)]) -> InsuranceResponseList:
        insurances = await service.all_insurance()
        return await formatted_response(insurances)
