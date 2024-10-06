from datetime import datetime

from fastapi import HTTPException
from sqlalchemy.orm import Session

from app.repositories.pay_repository import create_pay, get_all_payments
from app.schemas.pay_schema import PayRequest, PayResponse
from app.services.tenant_service import get_tenant_by_id_service


def create_pay_service(db: Session, pay: PayRequest) -> PayResponse:
    """
    create service
    :param db: Session from sqlalchemy
    :param pay: pay information
    :return: response
    """
    try:
        # Parse date format
        pay_date = datetime.strptime(str(pay.payDate), "%Y-%m-%d")
    except ValueError:
        raise HTTPException(
            status_code=400,
            detail="Formato de fecha incorrecto")

    # El pago no puede ser en día par
    if pay_date.day % 2 == 0:
        raise HTTPException(
            status_code=400,
            detail="Lo siento, pero no se puede recibir el pago por decreto de administración")

    # Validar el arrendatario
    tenant = get_tenant_by_id_service(db, pay.tenantId)
    if not tenant:
        raise HTTPException(
            status_code=404,
            detail="Arrendatario no encontrado")

    # Crear el pago en la base de datos
    created_pay = create_pay(db, pay)

    # Comprobar el valor pagado y generar la respuesta adecuada
    if pay.valuePaid == 1000000:
        return PayResponse(
            Response="Gracias por pagar todo tu arriendo",
            id=created_pay.id,
            tenant_id=pay.tenantId,
            property_code=pay.propertyCode,
            value_paid=pay.valuePaid,
            pay_date=pay.payDate
        )
    elif pay.valuePaid < 1000000:
        missing = 1000000 - pay.valuePaid
        return PayResponse(
            Response=f"Gracias por tu abono, sin embargo, te hace falta pagar ${missing}",
            id=created_pay.id,
            tenant_id=pay.tenantId,
            property_code=pay.propertyCode,
            value_paid=pay.valuePaid,
            pay_date=pay.payDate)
    else:
        return PayResponse(
            Response="Error: El valor pagado excede el monto requerido")


def get_all_payments_service(db: Session):
    """
    get all pay service
    :param db: Session from sqlalchemy
    :return: repository access
    """
    return get_all_payments(db)
