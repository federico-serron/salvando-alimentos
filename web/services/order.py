import requests
from . import api_rest


def list_products():
    response = requests.get(f'{api_rest.API_URL}/products')
    if response.status_code == 200:
        return response.json()
    else:
        return False



def index_list_products(quant):
    response = requests.get(f'{api_rest.API_URL}/products/{quant}')
    if response.status_code == 200:
        return response.json()
    else:
        return False



def user_owns(user_id):
    response = requests.get(f'{api_rest.API_URL}/products/owns/{user_id}')
    if response.status_code == 200:
        return True
    else:
        return False



def category_list_products(category_id):
    body = {"category_id": category_id}
    response = requests.post(f'{api_rest.API_URL}/products/category', json=body)
    if response.status_code == 200:
        return response.json()
    else:
        return False


def product_slug(slug):
    response = requests.get(f'{api_rest.API_URL}/product/{slug}')
    if response.status_code == 200:
        return response.json()
    else:
        return False


def list_user_products(id):
    body = {"user_id": id}
    response = requests.post(f'{api_rest.API_URL}/products/user', json=body)
    if response.status_code == 200:
        return response.json()
    else:
        return False


def list_user_expired_products(id):
    body = {"user_id": id}
    response = requests.post(f'{api_rest.API_URL}/products/user/expired', json=body)

    if response.status_code == 200:
        return response.json()
    else:
        return False



def create_product(title, description, price, expiring_date, category_id, image_url, available_quant, pickup_time, slug,
                   status, user_id):
    body = {
            "title": title,
            "description": description,
            "price": price,
            "expiring_date": expiring_date,
            "category_id": category_id,
            "image_url": image_url,
            "available_quant": available_quant,
            "pickup_time": pickup_time,
            "slug": slug,
            "status": status,
            "user_id": user_id
            }
    response = requests.post(f'{api_rest.API_URL}/products', json=body)
    if response.status_code == 200:
        return True
    else:
        return False


def edit_product(product_id, title, description, price, expiring_date, available_quant, slug, status, user_id):
    body = {"product_id": product_id,
            "title": title,
            "description": description,
            "price": price,
            "expiring_date": expiring_date,
            "available_quant": available_quant,
            "status": status,
            "user_id": user_id
            }

    response = requests.put(f'{api_rest.API_URL}/products/{slug}', json=body)

    if response.status_code == 200:
        return True
    else:
        return False



def delete_product(id_product):
    response = requests.delete(f'{api_rest.API_URL}/products/{id_product}')

    if response.status_code == 200:
        return True
    else:
        return False



def order_count():
    response = requests.get(f'{api_rest.API_URL}/orders/count')
    if response.status_code == 200:
        return response.json()
    else:
        return False