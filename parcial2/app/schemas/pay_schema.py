from datetime import date
from pydantic import BaseModel, Field

class PayRequest(BaseModel):
    """
    Model representing a new order request
    """
    tenantId: str
    propertyCode: str
    valuePaid: float = Field(..., gt=1, le=1000000)
    payDate: date

class PayDTO(BaseModel):
    """
    Data Transfer Object (DTO) for representing order information.
    """
    id : int
    tenant_id: str
    property_code: str
    value_paid: float
    pay_date: date

    class Config:
        """
        Pydantic configuration to enable from_attributes mode.
        """
        from_attributes = True  # Cambia orm_mode a from_attributes

class PayResponse(BaseModel):
    """
    Response for representing order value paid information.
    """
    Response: str