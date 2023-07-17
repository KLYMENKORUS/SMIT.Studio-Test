from httpx import AsyncClient
from http import HTTPStatus


async def test_create_insurance(client: AsyncClient):
    response = await client.post(url='/api/v1/insurance/create')
    assert response.status_code == HTTPStatus.OK


async def test_calculate(client: AsyncClient):
    data = {
        "date": "2020-06-01",
        "cargo_type": "Glass",
        "declared_value": 45
    }
    response = await client.post(url='/api/v1/insurance/calculate', json=data)
    assert response.status_code == HTTPStatus.OK
    assert response.json()['insurance_value'] == '1.80'


async def test_calculate_failed(client: AsyncClient):
    data = {
        "date": "2020-12-01",
        "cargo_type": "Glass",
        "declared_value": 45
    }
    response = await client.post(url='/api/v1/insurance/calculate', json=data)
    assert response.status_code == HTTPStatus.NOT_FOUND


async def test_all_by_cargo_type(client: AsyncClient):
    response = await client.get(url='/api/v1/insurance/all_by_cargo_type?cargo_type=Glass')
    assert response.status_code == HTTPStatus.OK
    assert len(response.json()['cargo_types']) == 2


async def test_all_insurance(client: AsyncClient):
    response = await client.get(url='/api/v1/insurance/all')
    assert response.status_code == HTTPStatus.OK