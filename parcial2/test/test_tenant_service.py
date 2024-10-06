import pytest
from unittest.mock import MagicMock
from sqlalchemy.orm import Session
from app.schemas.tenant_schema import TenantRequest
from app.services.tenant_service import create_tenant_service, get_all_tenants_service, get_tenant_by_id_service

@pytest.fixture
def db_session():
    # Crea un objeto de sesión simulado
    return MagicMock(spec=Session)

@pytest.fixture
def valid_tenant_request():
    return TenantRequest(
        id='123',
        name='John Doe',
        email='john.doe@example.com',
        phone='1234567890'
    )

def test_create_tenant_service(db_session, valid_tenant_request):
    # Arrange
    from app.repositories.tenant_repository import create_tenant
    create_tenant_mock = MagicMock(return_value=1)  # Simula que se devuelve el ID 1
    create_tenant.__code__ = create_tenant_mock.__code__  # Reemplaza la función real por el mock

    # Act
    tenant_id = create_tenant_service(db_session, valid_tenant_request)

    # Assert
    assert tenant_id == 1
    create_tenant_mock.assert_called_once_with(db_session, valid_tenant_request)

def test_get_all_tenants_service(db_session):
    # Arrange
    from app.repositories.tenant_repository import get_all_tenats
    get_all_tenats_mock = MagicMock(return_value=[
        {"id": 1, "name": "John Doe", "email": "john.doe@example.com", "phone": "1234567890"},
        {"id": 2, "name": "Jane Smith", "email": "jane.smith@example.com", "phone": "0987654321"}
    ])
    get_all_tenats.__code__ = get_all_tenats_mock.__code__  # Reemplaza la función real por el mock

    # Act
    tenants = get_all_tenants_service(db_session)

    # Assert
    assert len(tenants) == 2
    assert tenants[0]["name"] == "John Doe"
    assert tenants[1]["name"] == "Jane Smith"
    get_all_tenats_mock.assert_called_once_with(db_session)

def test_get_tenant_by_id_service(db_session):
    # Arrange
    from app.repositories.tenant_repository import get_tenant_by_id
    get_tenant_by_id_mock = MagicMock(return_value={"id": 1, "name": "John Doe", "email": "john.doe@example.com", "phone": "1234567890"})
    get_tenant_by_id.__code__ = get_tenant_by_id_mock.__code__  # Reemplaza la función real por el mock

    # Act
    tenant = get_tenant_by_id_service(db_session, "1")

    # Assert
    assert tenant["name"] == "John Doe"
    get_tenant_by_id_mock.assert_called_once_with(db_session, "1")
