from data.data_base import BaseDeDatos


def obtener_usuario(id_user):
    obtener_usuario_sql = f"""
        SELECT id, name, lastname, email, password, role_id, address, country 
        FROM users 
        WHERE id = {id_user}
    """
    bd = BaseDeDatos()
    return [{"id": row[0],
             "name": row[1],
             "lastname": row[2],
             "email": row[3],
             "password": row[4],
             "role_id": row[5],
             "address": row[6],
             "country": row[7]
             } for row in bd.ejecutar_sql(obtener_usuario_sql)]


def obtener_usuarios():
    obtener_usuarios_sql = f"""
        SELECT id, name, lastname, email, role_id 
        FROM users
    """
    bd = BaseDeDatos()
    return [{"id": row[0],
             "name": row[1],
             "lastname": row[2],
             "email": row[3],
             "role_id": row[4]
             } for row in bd.ejecutar_sql(obtener_usuarios_sql)]


def obtener_usuarios_por_nombre_clave(email, password):
    obtener_usuario_sql = f"""
            SELECT u.id, u.name, u.lastname, u.email, u.password, u.role_id, u.profile_photo_url, 
            u.address, u.country, u.company_name, r.name 
            FROM users u JOIN roles r ON u.role_id = r.id
            WHERE u.email='{email}' AND u.password='{password}'
        """
    bd = BaseDeDatos()
    return [{"id": row[0],
             "name": row[1],
             "lastname": row[2],
             "email": row[3],
             "password": row[4],
             "role_id": row[5],
             "profile_photo_url": row[6],
             "address": row[7],
             "country": row[8],
             "company_name": row[9],
             "role": row[10]
             } for row in bd.ejecutar_sql(obtener_usuario_sql)]


def crear_sesion(id_user, dt_string):
    crear_sesion_sql = f"""
               INSERT INTO sessions(id_user, date_time)
               VALUES ('{id_user}', '{dt_string}')
        """
    bd = BaseDeDatos()
    return bd.ejecutar_sql(crear_sesion_sql)


def obtener_sesion(id_sesion):
    obtener_sesion_sql = f"""
        SELECT id, id_user, date_time FROM sessions WHERE id = {id_sesion}
    """
    bd = BaseDeDatos()
    return [{"id": registro[0],
             "id_user": registro[1],
             "date_time": registro[2]}
            for registro in bd.ejecutar_sql(obtener_sesion_sql)]


def create_user(name, lastname, email, password, role, address, country, profile_photo_url, company_name):
    create_user_sql = f"""
        INSERT INTO users(name, lastname, email, password, role_id, address, country, profile_photo_url, company_name) 
        VALUES ('{name}', '{lastname}', '{email}', '{password}', {role}, '{address}', '{country}', 
        '{profile_photo_url}', '{company_name}') 
    """

    bd = BaseDeDatos()
    bd.ejecutar_sql(create_user_sql)


def update_user(id, name, lastname, password):
    update_user_sql = f"""
        UPDATE users SET name='{name}', lastname='{lastname}', password='{password}' 
        WHERE id={id}
    """

    bd = BaseDeDatos()
    bd.ejecutar_sql(update_user_sql)


def delete_user(id_user):
    delete_user_sql = f"""
        DELETE FROM users WHERE id={id_user}
    """
    bd = BaseDeDatos()
    bd.ejecutar_sql(delete_user_sql)


def get_id_user_email(email):
    get_id_user_email_sql = f"""
        SELECT id
        FROM users
        WHERE email = '{email}'
    """

    bd = BaseDeDatos()
    return [{
        "id": row[0]
    } for row in bd.ejecutar_sql(get_id_user_email_sql)]


def delete_session(id_user):
    delete_session_sql = f"""
        DELETE FROM sessions
        WHERE id_user='{id_user}'
    """
    bd = BaseDeDatos()
    bd.ejecutar_sql(delete_session_sql)


def client_count():
    client_count_sql = f"""
        SELECT count(*) FROM users WHERE role_id=1
    """

    bd = BaseDeDatos()
    return [{"client_qty": row[0]} for row in bd.ejecutar_sql(client_count_sql)]


def seller_count():
    seller_count_sql = f"""
        SELECT count(*) FROM users WHERE role_id=2
    """

    bd = BaseDeDatos()
    return [{"seller_qty": row[0]} for row in bd.ejecutar_sql(seller_count_sql)]

# def user_login(user_name, password):
#     user_login_sql = f"""
#         SELECT * FROM users WHERE user_name='{user_name}' AND password='{password}'
#     """
#     bd = BaseDeDatos()
#     bd._crear_conexion()
#     cursor = bd.conexion.cursor()
#     cursor.execute(user_login_sql)
#
#     query_result = [ dict(line) for line in [ zip([ column[0] for column in cursor.description ], row) for row in cursor.fetchall() ] ]
#
#     bd._cerrar_conexion()
#
#     return query_result
