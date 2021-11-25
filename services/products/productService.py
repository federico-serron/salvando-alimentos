from data.models import product as product_model
from datetime import datetime


def create_product(title, description, price, expiring_date, category_id, image_url, available_quant, pickup_time, slug,
                   status, user_id):

    product_model.create_product(title, description, price, expiring_date, category_id, image_url, available_quant,
                                 pickup_time, slug, status, user_id)


def list_products():
    hora_actual = datetime.now()
    # dd/mm/YY H:M:S
    dt_string = hora_actual.strftime("%Y-%m-%d")
    return product_model.list_products(dt_string)


def index_list_products(quant):
    hora_actual = datetime.now()
    # dd/mm/YY H:M:S
    dt_string = hora_actual.strftime("%Y-%m-%d")
    return product_model.index_list_products(quant, dt_string)



def user_owns(user_id):
    result = product_model.user_owns(user_id)
    if len(result[0]) > 1:
        return True
    else:
        return False


def category_list_products(category_id):
    hora_actual = datetime.now()
    # dd/mm/YY H:M:S
    dt_string = hora_actual.strftime("%Y-%m-%d")
    return product_model.category_list_products(category_id, dt_string)


def edit_product(product_id, title, description, price, expiring_date, available_quant, slug, status):
    product_model.edit_product(product_id, title, description, price, expiring_date, available_quant, slug, status)



def delete_product(id):
    product_model.delete_product(id)


def product_slug(slug):
    return product_model.product_slug(slug)


def list_user_products(user_id):
    hora_actual = datetime.now()
    # dd/mm/YY H:M:S
    dt_string = hora_actual.strftime("%Y-%m-%d")
    return product_model.list_user_products(user_id, dt_string)



def list_user_expired_products(user_id):
    hora_actual = datetime.now()
    # dd/mm/YY H:M:S
    dt_string = hora_actual.strftime("%Y-%m-%d")
    return product_model.list_user_expired_products(user_id, dt_string)



def product_count():
    hora_actual = datetime.now()
    # dd/mm/YY H:M:S
    dt_string = hora_actual.strftime("%Y-%m-%d")
    return product_model.product_count(dt_string)