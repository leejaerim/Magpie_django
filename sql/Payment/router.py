from fastapi import APIRouter
from fastapi.requests import Request
from databases.core import Database
from fastapi.param_functions import Depends
from sql.Payment.models import payment
from sql.Payment.schema import PaymentCreateRequest
from datetime import datetime, timedelta
payment_router = APIRouter()


def get_db_conn(request: Request):
    return request.state.db_conn

@payment_router.get("/api/v1/payment",response_model=dict)
@payment_router.get("/api/v1/payment/{page}",response_model=dict)
async def stack_select(
        date : str,
        page : int = 1,
        limit : int = 9,
        db : Database = Depends(get_db_conn)
):
    offset = (page-1)*limit
    query = payment.select().where(payment.columns.reg_date.between(datetime.strptime(date, "%Y-%m-%d"), datetime.strptime(date, "%Y-%m-%d") + timedelta(days=1))).offset(offset).limit(limit)
    list = {}
    # list['total'] = len(await db.fetch_all(payment.select()))
    list['row'] = await db.fetch_all(query)
    list['total'] = len(list['row'])
    return list


@payment_router.post("/api/v1/payment",response_model=dict)
async def payment_create(
        req: PaymentCreateRequest,
        db: Database = Depends(get_db_conn),
):
    query = payment.insert()
    values = req.dict()
    values['reg_date'] = datetime.now()
    await db.execute(query, values)
    return {**req.dict()}