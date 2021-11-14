import sqlite3

sql_table_categories = '''
CREATE TABLE IF NOT EXISTS categories (
    id	INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL
)
'''


sql_table_roles = '''
CREATE TABLE IF NOT EXISTS roles (
    id	INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL
)
'''


sql_table_payment_methods = '''
CREATE TABLE IF NOT EXISTS payment_methods (
    id	INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL
)
'''


sql_table_users = '''
CREATE TABLE IF NOT EXISTS users (
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    lastname TEXT NOT NULL,
    email TEXT UNIQUE NOT NULL,
    password TEXT NOT NULL,
    role_id INTEGER DEFAULT 1 NOT NULL,
    profile_photo_url TEXT,
    address TEXT NOT NULL,
    FOREIGN KEY(role_id) REFERENCES roles(id)
)
'''


sql_table_products = '''
CREATE TABLE IF NOT EXISTS products (
    id	INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    description TEXT NOT NULL,
    price REAL NOT NULL,
    expiring_date NUMERIC NOT NULL,
    category_id INTEGER NOT NULL,
    image_url TEXT NOT NULL,
    available_quant INTEGER NOT NULL,
    pickup_time NUMERIC NOT NULL,
    slug TEXT UNIQUE NOT NULL,
    status INTEGER NOT NULL,
    user_id INTEGER NOT NULL,
    FOREIGN KEY(category_id) REFERENCES category(id),
    FOREIGN KEY(user_id) REFERENCES users(id)
    
)
'''


sql_table_orders = '''
CREATE TABLE IF NOT EXISTS orders (
    id	INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER NOT NULL,
    date NUMERIC NOT NULL,
    payment_method INTEGER NOT NULL,
    pickup_time NUMERIC NOT NULL,
    status INTEGER DEFAULT 1 NOT NULL,
    FOREIGN KEY(user_id) REFERENCES users(id),
    FOREIGN KEY(payment_method) REFERENCES payment_methods(id)
)
'''

sql_table_ratings = '''
CREATE TABLE IF NOT EXISTS ratings (
    id	INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER NOT NULL,
    product_id INTEGER NOT NULL,
    rating INTEGER NOT NULL,
    comment TEXT NOT NULL,
    date NUMERIC NOT NULL,
    FOREIGN KEY(user_id) REFERENCES users(id),
    FOREIGN KEY(product_id) REFERENCES products(id)
)
'''


sql_table_products_orders = '''
CREATE TABLE IF NOT EXISTS products_orders (
    id	INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    order_id INTEGER NOT NULL,
    product_id INTEGER NOT NULL,
    FOREIGN KEY (order_id) REFERENCES orders(id),
    FOREIGN KEY (product_id) REFERENCES products(id)
)
'''


sql_table_user_payment_methods = '''
CREATE TABLE IF NOT EXISTS products_orders (
    id	INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER NOT NULL,
    payment_method_id INTEGER NOT NULL,
    FOREIGN KEY (user_id) REFERENCES users(id),
    FOREIGN KEY (payment_methods_id) REFERENCES payment_methods(id)
)
'''


sql_table_products_payment_methods = '''
CREATE TABLE IF NOT EXISTS products_payment_methods (
    id	INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    product_id INTEGER NOT NULL,
    payment_method_id INTEGER NOT NULL,
    FOREIGN KEY (product_id) REFERENCES products(id),
    FOREIGN KEY (payment_method_id) REFERENCES payment_methods(id)
)
'''

sql_table_sessions = '''
CREATE TABLE sessions(
 id INTEGER PRIMARY KEY,
 id_user TEXT,
 date_time TEXT,
 FOREIGN KEY(id_user) REFERENCES users(id) 
)
'''


if __name__ == '__main__':
    try:
        print('Creating Data Base..')
        conexion = sqlite3.connect('../../salvando_alimentos.db')

        print('Creating Tables..')
        conexion.execute(sql_table_categories)
        conexion.execute(sql_table_roles)
        conexion.execute(sql_table_payment_methods)
        conexion.execute(sql_table_users)
        conexion.execute(sql_table_products)
        conexion.execute(sql_table_orders)
        conexion.execute(sql_table_ratings)
        conexion.execute(sql_table_products_orders)
        conexion.execute(sql_table_user_payment_methods)
        conexion.execute(sql_table_products_payment_methods)
        conexion.execute(sql_table_sessions)

        conexion.close()
        print('Set up Succefully Done')
    except Exception as e:
        print(f'Error creating data base: {e}', e)
