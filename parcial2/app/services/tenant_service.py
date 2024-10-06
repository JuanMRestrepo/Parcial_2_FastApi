from sqlalchemy.orm import Session

from app.repositories.tenant_repository import create_tenant, get_all_tenats, get_tenant_by_id
from app.schemas.tenant_schema import TenantRequest

def create_tenant_service(db: Session, tenant: TenantRequest):
    """
    create service
    :param db: Session from sqlalchemy
    :param tenant: tenant information
    :return: repository access
    """
    return create_tenant(db, tenant)

def get_all_tenants_service(db: Session):
    """
    get all tenants
    :param db: Session from sqlalchemy
    :return: repository access
    """
    return get_all_tenats(db)

def get_tenant_by_id_service(db: Session, tenant_id: str):
    """
    get tenant by id
    :param db: Session from sqlalchemy
    :param tenant_id: identifier of the tenant
    :return: repository access
    """
    return get_tenant_by_id(db, tenant_id)