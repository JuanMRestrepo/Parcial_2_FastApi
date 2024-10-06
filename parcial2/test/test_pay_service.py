import pytest
from unittest.mock import MagicMock
from fastapi import HTTPException
from app.schemas.pay_schema import PayRequest
from app.services.pay_service import create_pay_service
from app.models.pay import PayORM

# Fixtures para crear un mock de la base de datos y el objeto PayRequest
@pytest.fixture
def mock_db():
    return MagicMock()

@pytest.fixture
def valid_pay_request():
    return PayRequest(
        tenantId='11111',
        propertyCode='ABC123',
        valuePaid=1000000,
        payDate='2024-10-05'
    )

@pytest.fixture
def invalid_pay_request():
    return PayRequest(
        tenantId='11111',
        propertyCode='ABC123',
        valuePaid=500000,
        payDate='2024-10-05'
    )

@pytest.fixture
def mock_tenant_service(mocker):
    return mocker.patch('app.services.tenant_service.get_tenant_by_id_service')

@pytest.fixture
def mock_create_pay(mocker):
    return mocker.patch('app.repositories.pay_repository.create_pay')

def test_create_pay_success(mock_db, valid_pay_request, mock_tenant_service, mock_create_pay):
    # Arrange
    mock_tenant_service.return_value = True  # Simula que el inquilino fue encontrado
    mock_create_pay.return_value = PayORM(id=1, **valid_pay_request.dict())

    # Act
    response = create_pay_service(mock_db, valid_pay_request)

    # Assert
    assert response.id == 1
    assert response.Response == "Gracias por pagar todo tu arriendo"
    assert response.value_paid == 1000000

def test_create_pay_partial_success(mock_db, invalid_pay_request, mock_tenant_service, mock_create_pay):
    # Arrange
    mock_tenant_service.return_value = True  # Simula que el inquilino fue encontrado
    mock_create_pay.return_value = PayORM(id=2, **invalid_pay_request.dict())

    # Act
    response = create_pay_service(mock_db, invalid_pay_request)

    # Assert
    assert response.id == 2
    assert response.Response == "Gracias por tu abono, sin embargo, te hace falta pagar $500000"

def test_create_pay_invalid_date_format(mock_db, invalid_pay_request, mock_tenant_service):
    # Arrange
    invalid_pay_request.payDate = '2024-10-xx'  # Formato de fecha incorrecto
    mock_tenant_service.return_value = True  # Simula que el inquilino fue encontrado

    # Act & Assert
    with pytest.raises(HTTPException) as exc:
        create_pay_service(mock_db, invalid_pay_request)
    assert exc.value.status_code == 400
    assert exc.value.detail == "Formato de fecha incorrecto"

def test_create_pay_even_day(mock_db, valid_pay_request, mock_tenant_service):
    # Arrange
    valid_pay_request.payDate = '2024-10-06'  # Día par
    mock_tenant_service.return_value = True  # Simula que el inquilino fue encontrado

    # Act & Assert
    with pytest.raises(HTTPException) as exc:
        create_pay_service(mock_db, valid_pay_request)
    assert exc.value.status_code == 400
    assert exc.value.detail == "Lo siento, pero no se puede recibir el pago por decreto de administración"

def test_create_pay_tenant_not_found(mock_db, valid_pay_request, mock_tenant_service):
    # Arrange
    mock_tenant_service.return_value = None  # Simula que el inquilino no fue encontrado

    # Act & Assert
    with pytest.raises(HTTPException) as exc:
        create_pay_service(mock_db, valid_pay_request)
    assert exc.value.status_code == 404
    assert exc.value.detail == "Arrendatario no encontrado"
