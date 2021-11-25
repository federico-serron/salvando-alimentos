from data.data_base import BaseDeDatos

# CREATE
def create_order(id_user, products, date, payment, pickup):
    create_order_sql = f"""
        INSERT INTO orders(user_id, date, payment_method, pickup_time)
        VALUES({id_user}, '{date}', {payment}, '{pickup}')
    """

    bd = BaseDeDatos()
    bd.ejecutar_sql(create_order_sql)



# LIST
def list_orders():
    list_orders_sql = """
        SELECT * FROM orders
        WHERE status=1
    """

    bd = BaseDeDatos()
    return [{
        "id": row[0],
        "user_id": row[1],
        "date": row[2],
        "payment_method": row[3],
        "pickup_time": row[4]
    } for row in bd.ejecutar_sql(list_orders_sql)]


def list_user_orders(id_user):
    list_user_orders_sql = f"""
        SELECT * FROM orders
        WHERE status=1 AND user_id = {id_user}
    """

    bd = BaseDeDatos()
    return [{
        "id": row[0],
        "user_id": row[1],
        "date": row[2],
        "payment_method": row[3],
        "pickup_time": row[4]
    } for row in bd.ejecutar_sql(list_user_orders_sql)]


# DELETE
def delete_order(id_order):
    delete_order_sql = f"""
        DELETE FROM orders WHERE id={id_order}
    """

    bd = BaseDeDatos()
    bd.ejecutar_sql(delete_order_sql)



# COUNT
def order_count():
    order_count_sql = f"""
        SELECT count(*) FROM orders WHERE status=2
    """

    bd = BaseDeDatos()
    return [{"order_qty": row[0]} for row in bd.ejecutar_sql(order_count_sql)]