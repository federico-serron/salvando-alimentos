from data.data_base import BaseDeDatos

def _rating_exists(id):
    query = f"SELECT id, product_id, rating FROM ratings WHERE id={id}"
    bd = BaseDeDatos()

    return [{
        "id": row[0],
        "product_id": row[1],
        "rating": row[2]
    } for row in bd.ejecutar_sql(query)]


# CREATE
def create_rating(id_user, product_id, rating, comment, date):
    create_rating_sql = F"""
        INSERT INTO ratings(user_id, product_id, rating, comment, date)
        VALUES({id_user}, {product_id}, {rating}, '{comment}', '{date}')
    """
    bd = BaseDeDatos()
    bd.ejecutar_sql(create_rating_sql)


# LIST
def list_ratings():
    list_ratings_sql = "SELECT * FROM ratings"

    bd = BaseDeDatos()
    return [{
        "id": row[0],
        "user_id": row[1],
        "product_id": row[2],
        "rating": row[3],
        "comment": row[4],
        "date": row[5]
    } for row in bd.ejecutar_sql(list_ratings_sql)]


# UPDATE
def update_rating(id_comment, rating, comment, date):
    update_rating_sql = f"""
        UPDATE ratings SET rating = {rating}, comment='{comment}', date='{date}'
        WHERE id={id_comment} 
    """

    bd = BaseDeDatos()
    bd.ejecutar_sql(update_rating_sql)


# DELETE
def delete_rating(id_rating):
    delete_rating_sql = f"DELETE FROM ratings WHERE id={id_rating}"

    bd = BaseDeDatos()
    bd.ejecutar_sql(delete_rating_sql)
