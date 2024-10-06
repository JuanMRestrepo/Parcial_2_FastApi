from typing import List

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.config.config import get_db
from app.schemas.pay_schema import PayDTO, PayRequest
from app.services.pay_service import create_pay_service, get_all_payments_service

router = APIRouter()

@router.post(path="/pagos", response_model=PayDTO)
def create_pay(pay: PayRequest, db : Session = Depends(get_db)):
    """
    route of create pay
    :param pay: pay information
    :param db: Session with the config db
    :return: create service
    """
    return create_pay_service(db, pay)

@router.get(path="/pagos", response_model=List[PayDTO])
def get_all_payments(db : Session = Depends(get_db)):
    """
    route of get payments
    :param db: Session with the config db
    :return: list of payments
    """
    payments = get_all_payments_service(db)
    return payments
