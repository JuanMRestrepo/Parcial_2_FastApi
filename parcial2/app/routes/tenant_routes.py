from typing import List

from fastapi import APIRouter, Depends

from sqlalchemy.orm import Session

from app.config.config import get_db
from app.schemas.tenant_schema import TenantDTO, TenantRequest
from app.services.tenant_service import create_tenant_service, get_all_tenants_service, get_tenant_by_id_service

router = APIRouter()

@router.post(path="/arrendatarios", response_model=TenantDTO)
def create_tenant(tenant: TenantRequest, db : Session = Depends(get_db)):
    """
    route for creating a tenant
    :param tenant: tenant information
    :param db: Session with the config db
    :return: create service
    """
    return create_tenant_service(db, tenant)

@router.get(path="/arrendatarios", response_model=List[TenantDTO])
def get_tenants(db: Session = Depends(get_db)):
    """
    route for getting all tenants
    :param db: Session with the config db
    :return: get all service
    """
    tenants = get_all_tenants_service(db)
    return tenants
