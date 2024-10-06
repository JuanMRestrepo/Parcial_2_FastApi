import pytest
from fastapi.testclient import TestClient
from unittest.mock import patch
from app.main import app  # Asegúrate de que este sea el nombre correcto de tu archivo main.py
from app.schemas.tenant_schema import TenantDTO, TenantRequest

client = TestClient(app)

@pytest.fixture
def valid_tenant_request():
    return TenantRequest(
        id='123',
        name='John Doe',
        email='john.doe@example.com',
        phone='1234567890'
    )

@pytest.fixture
def mock_create_tenant_service(mocker):
    return mocker.patch('app.services.tenant_service.create_tenant_service')

@pytest.fixture
def mock_get_all_tenants_service(mocker):
    return mocker.patch('app.services.tenant_service.get_all_tenants_service')

def test_create_tenant_success(valid_tenant_request, mock_create_tenant_service):
    # Arrange
    mock_create_tenant_service.return_value = TenantDTO(
        id='123',
        name='John Doe',
        email='john.doe@example.com',
        phone='1234567890'
    )

    # Act
    response = client.post("/arrendatarios", json=valid_tenant_request.dict())

    # Assert
    assert response.status_code == 200
    assert response.json() == {
        "id": '123',
        "name": 'John Doe',
        "email": 'john.doe@example.com',
        "phone": '1234567890'
    }

def test_get_all_tenants_success(mock_get_all_tenants_service):
    # Arrange
    mock_get_all_tenants_service.return_value = [
        TenantDTO(id='123', name='John Doe', email='john.doe@example.com', phone='1234567890'),
        TenantDTO(id='456', name='Jane Smith', email='jane.smith@example.com', phone='0987654321')
    ]

    # Act
    response = client.get("/arrendatarios")

    # Assert
    assert response.status_code == 200
    assert len(response.json()) == 2
    assert response.json() == [
        {
            "id": '123',
            "name": 'John Doe',
            "email": 'john.doe@example.com',
            "phone": '1234567890'
        },
        {
            "id": '456',
            "name": 'Jane Smith',
            "email": 'jane.smith@example.com',
            "phone": '0987654321'
        }
    ]
