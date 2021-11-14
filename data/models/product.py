from data.data_base import BaseDeDatos


# CREATE NEW PRODUCT
def create_product(title, description, price, expiring_date, category_id, image_url, available_quant, pickup_time, slug,
                   status, user_id):
    create_product_sql = f""" INSERT INTO products(title, description, price, expiring_date, category_id, image_url, 
    available_quant, pickup_time, slug, status, user_id) 
    VALUES ('{title}', '{description}', '{price}', '{expiring_date}', '{category_id}', '{image_url}', '{available_quant}', '{pickup_time}', '{slug}', '{status}', {user_id}) 
    """

    bd = BaseDeDatos()
    bd.ejecutar_sql(create_product_sql)


# LIST ALL THE PRODUCTS
def list_products():
    list_products_sql = """
        SELECT * FROM products WHERE status=1 ORDER BY id ASC
    """

    bd = BaseDeDatos()
    bd._crear_conexion()
    cursor = bd.conexion.cursor()
    cursor.execute(list_products_sql)

    query_result = [dict(line) for line in
                    [zip([column[0] for column in cursor.description], row) for row in cursor.fetchall()]]

    bd._cerrar_conexion()

    return query_result


# LIST SPECIFIED QUANTITY OF PRODUCTS
def index_list_products(quant):
    index_list_products_sql = f""" SELECT id, title, description, price, category_id, image_url, available_quant, 
    slug FROM products WHERE status=1 ORDER BY id ASC LIMIT {quant} 
    """

    bd = BaseDeDatos()
    return [{
        "id": row[0],
        "title": row[1],
        "description": row[2],
        "price": row[3],
        "category_id": row[4],
        "image_url": row[5],
        "available_quant": row[6],
        "slug": row[7]
    } for row in bd.ejecutar_sql(index_list_products_sql)]


# LIST PRODUCTS OF A SPECIFIED CATEGORY
def category_list_products(category_id):
    sql_category_list_products = f"""
        SELECT * FROM products
        WHERE category_id='{category_id}'
    """

    bd = BaseDeDatos()
    bd._crear_conexion()
    cursor = bd.conexion.cursor()
    cursor.execute(sql_category_list_products)

    query_result = [dict(line) for line in
                    [zip([column[0] for column in cursor.description], row) for row in cursor.fetchall()]]

    bd._cerrar_conexion()

    return query_result


# EDIT A PRODUCT
def edit_product(id, title, description, price):
    edit_product_sql = f"""
        UPDATE products SET title='{title}', description='{description}', price={price} WHERE id={id}
    """

    bd = BaseDeDatos()
    bd.ejecutar_sql(edit_product_sql)


# DELETE A PRODUCT
def delete_product(id):
    delete_product_sql = f'DELETE FROM products WHERE id={id}'

    bd = BaseDeDatos()
    bd.ejecutar_sql(delete_product_sql)


# LIST ALL THE INFO OF A SPECIFIED PRODUCT BY SLUG
def product_slug(slug):
    product_slug_sql = f"""
        SELECT * FROM products
        WHERE slug = '{slug}'
    """

    bd = BaseDeDatos()
    return [{
        "id": row[0],
        "title": row[1],
        "description": row[2],
        "price": row[3],
        "expiring_date": row[4],
        "category_id": row[5],
        "image_url": row[6],
        "available_quant": row[7],
        "pickup_time": row[8],
        "slug": row[9],
        "status": row[10]
    } for row in bd.ejecutar_sql(product_slug_sql)]

def list_user_products(user_id):
    user_products = f"""
        SELECT * FROM products
        WHERE user_id = {user_id}
    """

    bd = BaseDeDatos()
    return [{
        "id": row[0],
        "title": row[1],
        "description": row[2],
        "price": row[3],
        "expiring_date": row[4],
        "category_id": row[5],
        "image_url": row[6],
        "available_quant": row[7],
        "pickup_time": row[8],
        "slug": row[9],
        "status": row[10]
    } for row in bd.ejecutar_sql(user_products)]