from data.data_base import BaseDeDatos


# CREATE
def create_category(name):
    create_category_sql = f"""
        INSERT INTO categories(name) VALUES('{name}')
    """

    bd = BaseDeDatos()
    bd.ejecutar_sql(create_category_sql)


# LIST
def list_categories():
    list_categories_sql = """
        SELECT * FROM categories
        ORDER BY name ASC
    """

    bd = BaseDeDatos()
    return [{"id": row[0],
             "name": row[1]}
            for row in bd.ejecutar_sql(list_categories_sql)]


# UPDATE
def update_category(id_category, name):
    update_category_sql = f"UPDATE categories SET name='{name}' WHERE id={id_category}"

    bd = BaseDeDatos()
    bd.ejecutar_sql(update_category_sql)


# DELETE
def delete_category(id_category):
    delete_category_sql = f"DELETE FROM categories WHERE id={id_category}"

    bd = BaseDeDatos()
    bd.ejecutar_sql(delete_category_sql)