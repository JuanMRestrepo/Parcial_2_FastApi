from sqlalchemy import Column, String, Numeric, Date, ForeignKey, Integer

from app.config.config import Base


class PayORM(Base):
    """
    create model for db table
    """
    __tablename__ = 'payments'
    id = Column(Integer, primary_key=True, index=True)
    tenantId = Column(String, ForeignKey('tenants.id'))
    propertyCode = Column(String)
    valuePaid = Column(Numeric)
    payDate = Column(Date)
