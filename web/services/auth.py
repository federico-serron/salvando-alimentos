import requests

from web.services import api_rest


def user_login(email, password):
    body = {"email": email,
            "password": password}
    response = requests.post(f'{api_rest.API_URL}/login', json=body)
    # Solo verificamos el codigo de la respuesta en este caso
    if response.status_code == 200:
        return response.json()


def create_user(name, lastname, password, email, role, address, country,  profile_photo_url, company_name):
    body = {"name": name,
            "lastname": lastname,
            "password": password,
            "email": email,
            "role": role,
            "address": address,
            "country": country,
            "profile_photo_url": profile_photo_url,
            "company_name": company_name
            }
    response = requests.post(f'{api_rest.API_URL}/signup', json=body)
    # Al igual que en el caso de la validacion, simplificamos el manejo de errores
    if response.status_code == 200:
        return response.json()
    else:
        return False


def list_users():
    response = requests.get(f'{api_rest.API_URL}/users')
    return response.json()


def delete_session(email):
    body = {
        "email": email
    }
    response = requests.post(f'{api_rest.API_URL}/logout', json=body)
    return response.status_code == 200



def client_count():
    response = requests.get(f'{api_rest.API_URL}/users/clientcount')
    if response.status_code == 200:
        return response.json()
    else:
        return False



def seller_count():
    response = requests.get(f'{api_rest.API_URL}/users/sellercount')
    if response.status_code == 200:
        return response.json()
    else:
        return 0