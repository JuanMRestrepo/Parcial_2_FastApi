from sqlalchemy import Column, String
from app.config.config import Base

class TenantORM(Base):
    """
    create model for db table
    """
    __tablename__ = "tenants"
    id = Column(String, primary_key=True, index=True)
    fullName = Column(String, index=True)
    email = Column(String, unique=True)
    phone = Column(String)
