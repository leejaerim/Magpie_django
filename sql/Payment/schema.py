from pydantic import BaseModel


class PaymentCreateRequest(BaseModel):
    value: int