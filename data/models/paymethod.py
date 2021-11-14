from data.data_base import BaseDeDatos


# CREATE
def create_paymethod(name):
    create_paymethod_sql = f"INSERT INTO payment_methods(name) VALUES('{name}')"

    bd = BaseDeDatos()
    bd.ejecutar_sql(create_paymethod_sql)


# LIST
def list_paymethod():
    list_paymethod_sql = "SELECT * FROM payment_methods"

    bd = BaseDeDatos()
    return [{
        "id": row[0],
        "name": row[1]
    } for row in bd.ejecutar_sql(list_paymethod_sql)]


# UPDATE
def update_paymethod(id, name):
    update_paymethod_sql = f"UPDATE payment_methods SET name='{name}' WHERE id={id}"

    bd = BaseDeDatos()
    bd.ejecutar_sql(update_paymethod_sql)


# DELETE
def delete_paymethod(id_paymethod):
    bd = BaseDeDatos()
    bd.ejecutar_sql(f"DELETE FROM payment_methods WHERE id={id_paymethod}")