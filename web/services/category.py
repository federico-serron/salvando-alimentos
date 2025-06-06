import requests
from . import api_rest


def list_categories():
    response = requests.get(f'{api_rest.API_URL}/categories')
    if response.status_code == 200:
        return response.json()
    else:
        return False

