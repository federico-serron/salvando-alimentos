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
def list_products(dt_string):
    list_products_sql = f"""
        SELECT p.id, p.title, p.description, p.category_id, p.image_url, p.slug, u.company_name
        FROM products p JOIN users u ON p.user_id = u.id
        WHERE status=1 AND expiring_date > '{dt_string}' ORDER BY p.id DESC
    """

    bd = BaseDeDatos()
    return [{
        "id": row[0],
        "title": row[1],
        "description": row[2],
        "category_id": row[3],
        "image_url": row[4],
        "slug": row[5],
        "company_name": row[6]
    } for row in bd.ejecutar_sql(list_products_sql)]


# LIST SPECIFIED QUANTITY OF PRODUCTS
def index_list_products(quant, dt_string):
    index_list_products_sql = f""" SELECT id, title, description, price, image_url, slug 
    FROM products WHERE status=1 AND expiring_date > '{dt_string}' ORDER BY id DESC LIMIT {quant} 
    """

    bd = BaseDeDatos()
    return [{
        "id": row[0],
        "title": row[1],
        "description": row[2],
        "price": row[3],
        "image_url": row[4],
        "slug": row[5]
    } for row in bd.ejecutar_sql(index_list_products_sql)]



# CHECKS AND RETURN IF USER OWNS SPECIFIED PRODUCT
def user_owns(user_id):
    user_owns_sql = f"""
        SELECT id FROM products WHERE user_id={user_id}
    """

    bd = BaseDeDatos()
    bd._crear_conexion()
    cursor = bd.conexion.cursor()
    cursor.execute(user_owns_sql)

    query_result = [dict(line) for line in
                    [zip([column[0] for column in cursor.description], row) for row in cursor.fetchall()]]

    bd._cerrar_conexion()





# LIST PRODUCTS OF A SPECIFIED CATEGORY
def category_list_products(category_id, dt_string):
    sql_category_list_products = f"""
        SELECT * FROM products
        WHERE category_id='{category_id}' AND expiring_date > '{dt_string}'
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
def edit_product(product_id, title, description, price, expiring_date, available_quant, slug, status):
    edit_product_sql = f"""
        UPDATE products SET title='{title}', description='{description}', price={price}, expiring_date='{expiring_date}',
         available_quant={available_quant}, slug='{slug}', status={status} 
         WHERE id={product_id}
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
        SELECT p.id, p.title, p.description, p.price, p.expiring_date, p.category_id, p.image_url, p.available_quant, 
        p.pickup_time, p.slug, p.status, p.user_id, c.name, u.company_name, u.address FROM products p
        JOIN categories c ON p.category_id = c.id
        JOIN users u ON p.user_id = u.id    
        WHERE p.slug = '{slug}'
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
        "status": row[10],
        "user_id": row[11],
        "c_name": row[12],
        "company_name": row[13],
        "address": row[14]
    } for row in bd.ejecutar_sql(product_slug_sql)]

def list_user_products(user_id, dt_string):
    user_products = f"""
        SELECT * FROM products
        WHERE user_id = {user_id} AND expiring_date > '{dt_string}'
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



def list_user_expired_products(user_id, dt_string):
    expired_user_products = f"""
        SELECT * FROM products
        WHERE user_id = {user_id} AND expiring_date <= '{dt_string}'
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
    } for row in bd.ejecutar_sql(expired_user_products)]


def product_count(dt_string):
    product_count_sql = f"""
        SELECT count(*) FROM products WHERE expiring_date > '{dt_string}' 
    """
    bd = BaseDeDatos()
    return [{"product_count": row[0]} for row in bd.ejecutar_sql(product_count_sql)]