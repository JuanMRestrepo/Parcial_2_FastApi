from sqlalchemy.orm import Session

from app.models.pay import PayORM
from app.schemas.pay_schema import PayRequest


def create_pay(db: Session, pay: PayRequest):
    """
    creates a new pay
    :param db: Session from sqlalchemy
    :param pay: pay information
    :return: the newly created pay
    """
    db_pay = PayORM(
        tenantId=pay.tenantId,
        propertyCode=pay.propertyCode,
        valuePaid=pay.valuePaid,
        payDate=pay.payDate
    )
    db.add(db_pay)
    db.commit()
    db.refresh(db_pay)
    return db_pay


def get_all_payments(db: Session):
    """
    obtains all pays
    :param db: Session from sqlalchemy
    :return: all payments in db
    """
    return db.query(PayORM).all()
