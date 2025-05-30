from interfaces.payment_gateway_interface import PaymentGatewayInterface


class PaymentService:
    def __init__(self, gateway: PaymentGatewayInterface):
        self.gateway = gateway

    def pay(self, data: dict) -> dict:
        return self.gateway.pay(data)
