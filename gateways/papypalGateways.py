from interfaces.payment_gateway_interface import PaymentGatewayInterface


class PayPalGateway(PaymentGatewayInterface):
    def pay(self, data: dict) -> dict:
        # Simulação de pagamento com PayPal
        return {
            "status": "success",
            "provider": "PayPal",
            "valor": data.get("valor"),
            "moeda": data.get("moeda"),
            "descricao": data.get("descricao")
        }
