from pydantic import BaseModel, EmailStr

class TenantRequest(BaseModel):
    """
    Model representing a new order request
    """
    id : str
    fullName: str
    email : EmailStr
    phone: str

class TenantDTO(BaseModel):
    """
    Data Transfer Object (DTO) for representing order information.
    """
    id: str
    fullName: str
    email: EmailStr
    phone: str

    class Config:
        """
        Pydantic configuration to enable from_attributes mode.
        """
        from_attributes = True  # Cambia orm_mode a from_attributes