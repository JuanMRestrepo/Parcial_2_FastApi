from datetime import date
from typing import Optional

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
    id: int
    tenantId: str
    propertyCode: str
    valuePaid: float
    payDate: date


class PayResponse(BaseModel):
    """
    Data Transfer Object (DTO) for representing order information.
    """
    Response: str
    id: Optional[int] = None
    tenantId: Optional[str] = None
    propertyCode: Optional[str] = None
    valuePaid: Optional[float] = None
    payDate: Optional[date] = None

    class Config:
        """
        Pydantic configuration to enable from_attributes mode.
        """
        from_attributes = True  # Cambia orm_mode a from_attributes
