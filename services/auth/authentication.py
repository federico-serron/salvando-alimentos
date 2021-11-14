from data.models import user as user_model
from datetime import datetime

def _existe_usuario(email, password):
    usuarios = user_model.obtener_usuarios_por_nombre_clave(email, password)
    return not len(usuarios) == 0


def _crear_sesion(id_usuario):
    hora_actual = datetime.now()
    # dd/mm/YY H:M:S
    dt_string = hora_actual.strftime("%d/%m/%Y %H:%M:%S")
    return user_model.crear_sesion(id_usuario, dt_string)


def obtener_usuarios():
    return user_model.obtener_usuarios()


def obtener_usuario(id_user):
    usuario = user_model.obtener_usuario(id_user)
    if len(usuario) == 0:
        raise Exception("El usuario no existe")
    return usuario


def create_user(name, lastname, email, password, role, address):
    if not _existe_usuario(email, password):
        user_model.create_user(name, lastname, email, password, role, address)
        user_info = user_model.obtener_usuarios_por_nombre_clave(email, password)
        _crear_sesion(user_info[0]['id'])
    else:
        raise Exception("El usuario ya existe.")


def update_user(id, name, lastname, password):
    user_model.update_user(id, name, lastname, password)


def delete_user(id_user):
    if not user_model.delete_user(id_user):
        raise Exception("No se pudo eliminar el usuario.")


def user_login(email, password):
    if _existe_usuario(email, password):
        user_info = user_model.obtener_usuarios_por_nombre_clave(email, password)
        _crear_sesion(user_info[0]['id'])
        return user_info
    else:
        raise Exception("El usuario no existe y/o la clave es incorrecta.")


def get_id_user_email(email):
    return user_model.get_id_user_email(email)[0]


def delete_session(id_user):
    user_model.delete_session(id_user)