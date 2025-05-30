from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from utils import paypal


payment_bp = APIRouter()


class PaymentRequest(BaseModel):
    amount: float
    currency: str = "USD"  # Default USD


@payment_bp.post("/create-payment")
def create_payment(payment: PaymentRequest):
    try:
        token = paypal.get_access_token()
        order = paypal.create_order(token, str(payment.amount), payment.currency)
        return {"status": "created", "order": order}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@payment_bp.post("/capture-payment/{order_id}")
def capture_payment(order_id: str):
    try:
        token = paypal.get_access_token()
        capture = paypal.capture_order(token, order_id)
        return {"status": "captured", "details": capture}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
