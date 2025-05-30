from fastapi import FastAPI
from controllers import paymentController

app = FastAPI()

app.include_router(paymentController.payment_bp, prefix="/api", tags=["Payments"])


@app.get("/")
def read_root():
    return {"message": "API de Pagamento PayPal funcionando ✅"}
