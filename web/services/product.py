import requests
from web.services import api_rest


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


def create_product(title, description, price, expiring_date, category_id, image_url, available_quant, pickup_time, slug,
                   status, user_id):
    body = {"title": title,
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