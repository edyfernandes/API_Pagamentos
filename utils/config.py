import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    PAYPAL_CLIENT_ID = os.getenv("AW19tXfzfHPcLuD4VQeQbgN8MRC-CGmI1VmNPT6JO-JRRmAnt36RlVU0kU5U_YzFdvHGK0HIF83tqRWQ")
    PAYPAL_CLIENT_SECRET = os.getenv("EHHuSbF6oG_fLbgpWnB7ZV8OL4OdwsU6BTR_Mu9cAefpbyXT4w5R_sp3MWRAmSx8yx3qrWQ6HAwp5GHS")