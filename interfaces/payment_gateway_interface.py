from abc import ABC, abstractmethod


class PaymentGatewayInterface(ABC):
    @abstractmethod
    def pay(self, data: dict) -> dict:
        pass
