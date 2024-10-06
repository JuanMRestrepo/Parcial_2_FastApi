import pytest
from fastapi import FastAPI, HTTPException
from fastapi.testclient import TestClient
from unittest.mock import patch
from app.main import app  # Asegúrate de que este sea el nombre correcto de tu archivo main.py
from app.schemas.pay_schema import PayRequest, PayResponse, PayDTO

client = TestClient(app)

@pytest.fixture
def valid_pay_request():
    return PayRequest(
        tenantId='1',
        propertyCode='ABC123',
        valuePaid=1000000,
        payDate='2024-10-05'
    )

@pytest.fixture
def mock_pay_service(mocker):
    return mocker.patch('app.services.pay_service.create_pay_service')

@pytest.fixture
def mock_get_all_payments_service(mocker):
    return mocker.patch('app.services.pay_service.get_all_payments_service')

def test_create_pay_success(valid_pay_request, mock_pay_service):
    # Arrange
    mock_pay_service.return_value = PayResponse(
        Response="Gracias por pagar todo tu arriendo",
        id=1,
        tenant_id='1',
        property_code='ABC123',
        value_paid=1000000,
        pay_date=valid_pay_request.payDate.isoformat()
    )

    # Act
    response = client.post("/pagos", json={
        'tenantId': valid_pay_request.tenantId,
        'propertyCode': valid_pay_request.propertyCode,
        'valuePaid': valid_pay_request.valuePaid,
        'payDate': valid_pay_request.payDate.isoformat()  # Convertir a string aquí
    })

    # Assert
    assert response.status_code == 200
    # Verifica otros aspectos de la respuesta aquí


def test_create_pay_invalid_date_format(valid_pay_request, mock_pay_service):
    # Arrange
    valid_pay_request.payDate = '2024-10-xx'  # Formato de fecha incorrecto
    mock_pay_service.side_effect = HTTPException(status_code=400, detail="Formato de fecha incorrecto")

    # Act
    response = client.post("/pagos", json=valid_pay_request.dict())

    # Assert
    assert response.status_code == 400
    assert response.json() == {"detail": "Formato de fecha incorrecto"}

def test_get_all_payments(mock_get_all_payments_service):
    # Arrange
    mock_get_all_payments_service.return_value = [
        PayDTO(id=1, tenantId='1', propertyCode='ABC123', valuePaid=1000000, payDate='2024-10-05'),
        PayDTO(id=2, tenantId='2', propertyCode='XYZ456', valuePaid=500000, payDate='2024-10-06')
    ]

    # Act
    response = client.get("/pagos")

    # Assert
    assert response.status_code == 200
    assert len(response.json()) == 2
    assert response.json() == [
        {
            "id": 1,
            "tenantId": '1',
            "propertyCode": 'ABC123',
            "valuePaid": 1000000,
            "payDate": '2024-10-05'
        },
        {
            "id": 2,
            "tenantId": '2',
            "propertyCode": 'XYZ456',
            "valuePaid": 500000,
            "payDate": '2024-10-06'
        }
    ]
