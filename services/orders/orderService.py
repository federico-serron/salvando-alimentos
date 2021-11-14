from datetime import datetime
from data.models import order as order_model

def _set_date_time():
    # dd/mm/YY H:M:S
    dt_string = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    return dt_string

# CREATE
def create_order(id_user, products, payment, pickup):
    date = _set_date_time()
    order_model.create_order(id_user, products, date, payment, pickup)


# LIST
def list_orders():
    return order_model.list_orders()

def list_user_orders(id_user):
    return order_model.list_user_orders(id_user)


# DELETE
def delete_order(id_order):
    order_model.delete_order(id_order)