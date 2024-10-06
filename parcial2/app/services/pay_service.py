from datetime import datetime

from fastapi import HTTPException
from sqlalchemy.orm import Session

from app.repositories.pay_repository import create_pay
from app.schemas.pay_schema import PayRequest, PayResponse
from app.services.tenant_service import get_tenant_by_id_service


def create_pay_service(db: Session, pay : PayRequest) -> PayResponse:
    """
    create service
    :param db: Session from sqlalchemy
    :param pay: pay information
    :return: response
    """
    try:
        # Formato de la fecha
        date = datetime.strptime(str(pay.payDate), "%Y-%m-%d")
    except ValueError:
        raise HTTPException(status_code=400, detail="Formato de fecha incorrecto")
    #El pago no sea dia par
    if date.day % 2 == 0:
        raise HTTPException(status_code=400,detail="Lo siento, pero no se puede recibir el pago por decreto de administración")

    #Validar el arrendatario
    tenant = get_tenant_by_id_service(db,pay.tenantId)
    if not tenant:
        raise HTTPException(status_code=404, detail="Arrendatario no encontrado")
    #Crear el pago
    create_pay(db, pay)
    #Comprovar el valor pagado y generar la respuesta
    if pay.valuePaid == 1000000:
        return PayResponse(Response="Gracias por pagar todo tu arriendo")
    elif pay.valuePaid < 1000000:
        missing = 1000000 - pay.valuePaid
        return PayResponse(Response=f"Gracias por tu abono, sin embargo, recuerda que te hace falta pagar ${missing}")
    else:
        return PayResponse(Response="Gracias por pagar todo tu arriendo")

def get_all_payments_service(db: Session):
    """
    get all pay service
    :param db: Session from sqlalchemy
    :return: repository access
    """
    return get_all_payments_service(db)