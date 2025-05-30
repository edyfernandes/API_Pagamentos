# app.py

from flask import Flask
from controllers.paymentController import payment_bp

app = Flask(__name__)
app.register_blueprint(payment_bp)

if __name__ == '__main__':
    app.run(debug=True)
