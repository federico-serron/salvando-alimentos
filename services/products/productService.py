from data.models import product as product_model


def create_product(title, description, price, expiring_date, category_id, image_url, available_quant, pickup_time, slug,
                   status, user_id):

    product_model.create_product(title, description, price, expiring_date, category_id, image_url, available_quant,
                                 pickup_time, slug, status, user_id)


def list_products():
    return product_model.list_products()


def index_list_products(quant):
    return product_model.index_list_products(quant)


def category_list_products(category_id):
    return product_model.category_list_products(category_id)


def edit_product(id, title, description, price):
    product_model.edit_product(id, title, description, price)


def delete_product(id):
    product_model.delete_product(id)


def product_slug(slug):
    return product_model.product_slug(slug)


def list_user_products(user_id):
    return product_model.list_user_products(user_id)
