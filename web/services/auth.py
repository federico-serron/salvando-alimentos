import requests

from . import api_rest


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
<<<<<<< HEAD
    try:
        response = requests.get(f'{api_rest.API_URL}/users/sellercount')
        response.raise_for_status()
        data = response.json()
        print(f"API Response: {data}")
        return data
    except requests.exceptions.RequestException as e:
        print(f"Error en seller_count: {e}")
        return False
    except ValueError as e:
        print(f"Error decodificando JSON: {e}")
        return False
=======
    response = requests.get(f'{api_rest.API_URL}/users/sellercount')
    if response.status_code == 200:
        return response.json()
    else:
        return 0
>>>>>>> 30223b473ac5504d3bcd46b8e46b4714468dd0d5
