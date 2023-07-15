from fastapi import APIRouter
from .schemas import CalculateRequest, CalculateResponse
from .services import calculate_insurance


router = APIRouter(prefix='/api/v1/insurance')


@router.post('/calculate', response_model=CalculateResponse)
async def calculate(data: CalculateRequest) -> CalculateResponse:
    insurance = await calculate_insurance(data)
    return CalculateResponse(insurance_value=insurance)