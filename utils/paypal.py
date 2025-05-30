import requests
from requests.auth import HTTPBasicAuth
from .config import Config


def get_access_token():
    url = 'https://api-m.sandbox.paypal.com/v1/oauth2/token'
    headers = {'Accept': 'application/json', 'Accept-Language': 'en_US'}
    data = {'grant_type': 'client_credentials'}

    response = requests.post(url, headers=headers, data=data,
                             auth=HTTPBasicAuth(Config.PAYPAL_CLIENT_ID, Config.PAYPAL_CLIENT_SECRET))
    response.raise_for_status()
    return response.json()['access_token']


def create_order(access_token, value, currency):
    url = 'https://api-m.sandbox.paypal.com/v2/checkout/orders'
    headers = {
        'Content-Type': 'application/json',
        'Authorization': f'Bearer {access_token}'
    }
    data = {
        "intent": "CAPTURE",
        "purchase_units": [
            {
                "amount": {
                    "currency_code": currency,
                    "value": value
                }
            }
        ]
    }

    response = requests.post(url, headers=headers, json=data)
    response.raise_for_status()
    return response.json()


def capture_order(access_token, order_id):
    url = f'https://api-m.sandbox.paypal.com/v2/checkout/orders/{order_id}/capture'
    headers = {
        'Content-Type': 'application/json',
        'Authorization': f'Bearer {access_token}'
    }

    response = requests.post(url, headers=headers)
    response.raise_for_status()
    return response.json()
