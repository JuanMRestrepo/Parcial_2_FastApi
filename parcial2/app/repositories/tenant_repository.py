from sqlalchemy.orm import Session

from app.models.tenant import TenantORM
from app.schemas.tenant_schema import TenantRequest

def create_tenant(db: Session, tenant: TenantRequest):
    """
    creates a new tenant
    :param db: Session from sqlalchemy
    :param tenant: tenant information
    :return: newly created tenant
    """
    db_tenant = TenantORM(**tenant.dict())
    db.add(db_tenant)
    db.commit()
    db.refresh(db_tenant)
    return db_tenant

def get_all_tenats(db: Session):
    """
    obtains all tenants
    :param db: Session from sqlalchemy
    :return: all tenants in DB
    """
    return db.query(TenantORM).all()

def get_tenant_by_id(db: Session, id: str):
    """
    obtains a tenant by id
    :param id:identifier of the tenant
    :return: a tenant whit compaitble id
    """
    return db.query(TenantORM).filter_by(id=id).first()