import os.path

from os import remove
from flask import Flask, request, jsonify, render_template, url_for, session, flash
from werkzeug.utils import redirect, secure_filename
from strgen import StringGenerator
from services import auth
from services import product
from services import category
from services import order

UPLOAD_FOLDER_PRODUCTS = 'static/storage/products/'
UPLOAD_FOLDER_USERS = 'static/storage/users/'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}

app = Flask(__name__)
app.secret_key = 'Clave_muy_secreta'
app.config['UPLOAD_FOLDER_PRODUCTS'] = UPLOAD_FOLDER_PRODUCTS
app.config['UPLOAD_FOLDER_USERS'] = UPLOAD_FOLDER_USERS


@app.route('/')
def index():
    products_list = index_list_products(6)
    products_qty = product_count()
    order_qty = order_count()
    client_qty = client_count()
    seller_qty = seller_count()
    if products_list:
        return render_template('public/index.html', title='Inicio', session=session,
                               products=products_list, products_qty=products_qty[0], order_qty=order_qty[0],
                               client_qty=client_qty[0], seller_qty=seller_qty[0])
    else:
        return render_template('public/index.html', title='Inicio', session=session, products='',
                               seller_qty=seller_qty[0], client_qty=client_qty[0],  order_qty=order_qty[0], products_qty=products_qty[0])


####################### LOGIN & SIGNUP #####################

@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if session:
        return redirect(url_for('index'))

    if request.method == 'POST':
        if not auth.user_login(request.form['email'], request.form['password']):
            error = 'Usuario y/o contraseña no válidos.'
        else:
            user_info = auth.user_login(request.form['email'], request.form['password'])
            session['email'] = request.form['email']
            session['id'] = user_info[0]['id']
            session['name'] = user_info[0]['name']
            session['lastname'] = user_info[0]['lastname']
            session['password'] = user_info[0]['password']
            session['profile_photo_url'] = user_info[0]['profile_photo_url']
            session['address'] = user_info[0]['address']
            session['country'] = user_info[0]['country']
            session['role_id'] = user_info[0]['role_id']
            session['company_name'] = user_info[0]['company_name']
            session['role'] = user_info[0]['role']
            return redirect(url_for('index'))
    return render_template('public/login/login.html', error=error, title="Acceder")


@app.route('/signup', methods=['POST', 'GET'])
def signup():
    error = None
    if request.method == 'POST':
        if 'profile_photo_url' in request.files:
            file = request.files['profile_photo_url']
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER_USERS'], filename))
            img_location = '../../' + UPLOAD_FOLDER_USERS + filename

            address = request.form['address'] + ', ' + request.form['city'] + ', ' + request.form['zip']

            user_response = auth.create_user(request.form['name'], request.form['lastname'], request.form['password'],
                                             request.form['email'], request.form['role_id'], address,
                                             request.form['country'],
                                             img_location, request.form['company_name'])
        if not user_response:
            error = 'El Email ya esta en uso. Pruebe con otro diferente.'
        else:
            session['id'] = user_response[0]['id']
            session['country'] = user_response[0]['country']
            session['address'] = user_response[0]['address']
            session['name'] = user_response[0]['name']
            session['lastname'] = user_response[0]['lastname']
            session['email'] = user_response[0]['email']
            session['role_id'] = user_response[0]['role_id']
            session['profile_photo_url'] = img_location
            session['company_name'] = user_response[0]['company_name']
            session['role'] = user_response[0]['role']

            return redirect(url_for('index'))
    return render_template('public/login/signup.html', error=error, title="Registrate")


@app.route('/logout')
def logout():
    if session:
        if auth.delete_session(session['email']):
            session.clear()
            return redirect(url_for('index'))
        else:
            session.clear()
            return redirect(url_for('index'))


####################### PRODUCTS #####################
# List all the products GET // List all the products by Category POST
@app.route('/products', methods=['POST', 'GET'])
def products():
    if request.method == 'GET':
        product_list = check_products()
        if not product_list:
            return render_template('public/products.html', title="Productos")
        else:
            return render_template('public/products.html', title="Productos", products=product_list,
                                   categories=list_categories())
    if request.method == 'POST':
        category_id = request.form['input-category']
        category_products = product.category_list_products(category_id)
        return category_products


# List all the info of a specific product by slug GET
@app.route('/products/<string:slug>')
def product_slug(slug):
    if request.method == 'GET':
        result = product.product_slug(slug)
        return render_template('public/product-info.html', title=result[0]['title'], product=result[0])


####################### ADMIN #####################
# DASHBOARD
@app.route('/admin', methods=['GET'])
def admin():
    if session and session['role_id']:
        return render_template('public/admin/index.html', title='Dashboard', session=session)
    else:
        return redirect(url_for('index', error="No tiene permiso para ingresar."))


# PROFILE
@app.route('/profile', methods=['POST', 'GET'])
def profile():
    if request.method == 'GET':
        if session and session['role_id']:

            return render_template('public/admin/profile.html', title='Mi Perfil', session=session)
        else:
            return redirect(url_for('index', error="No tiene permiso para ingresar."))

    if request.method == 'POST':
        if session and session['role_id']:
            if 'profile_photo_url' in request.files:
                file = request.files['profile_photo_url']
                randomName = StringGenerator("[\l\d]{14}").render_list(1, unique=True)
                filename = randomName[0]
                file.save(os.path.join(app.config['UPLOAD_FOLDER_USERS'], filename))
                img_location = '../../' + UPLOAD_FOLDER_USERS + filename

                if not auth.edit_user(request.form['name'], request.form['lastname'],
                                      request.form['email'], request.form['role_id'], request.form['address'],
                                      img_location):
                    error = 'El Email ya esta en uso. Pruebe con otro diferente.'
                else:
                    session['name'] = request.form['name']
                    session['lastname'] = request.form['lastname']
                    session['email'] = request.form['email']
                    session['role_id'] = request.form['role_id']
                    session['profile_photo_url'] = img_location

                    return redirect(url_for('index'))


# ORDERS
@app.route('/admin/orders')
def orders():
    if session and session['role_id']:
        return render_template('public/admin/orders.html', title='Mis órdenes', session=session)
    else:
        return redirect(url_for('index', error="No tiene permiso para ingresar."))


# PRODUCTS
# List all the ACTIVE products of the logged in user
@app.route('/admin/products')
def list_products():
    if session and session['role_id'] == 2:
        user_products = product.list_user_products(session['id'])
        return render_template('public/admin/products/list-products.html', title="Listado de productos",
                               subtitle="Activos", products=user_products)
    else:
        return redirect(url_for('index', error="No tiene permiso para ingresar."))


# List all the EXPIRED products of the logged in user
@app.route('/admin/products/expired')
def expired_products():
    if session and session['role_id'] == 2:
        user_products = product.list_user_expired_products(session['id'])
        return render_template('public/admin/products/list-products.html', title="Productos vencidos",
                               subtitle="Vencidos", products=user_products)
    else:
        return redirect(url_for('index', error="No tiene permiso para ingresar."))


# CREATE A PRODUCT
@app.route('/admin/products/create', methods=['GET', 'POST'])
def create_product():
    if session and session['role_id'] == 2:
        if request.method == 'GET':
            if list_categories():
                categories = list_categories()
            else:
                categories = {"id": 1,
                              "name": "No hay categorias disponibles"}
            return render_template('public/admin/products/create-product.html', title="Nuevo Producto", session=session,
                                   categories=categories)

        if request.method == 'POST':
            if 'image_url' not in request.files:
                flash('No hay campo de subida de archivo en el formulario!')
                return redirect(request.url)
            file = request.files['image_url']
            if file:
                randomName = StringGenerator("[\l\d]{14}").render_list(1, unique=True)
                filename = randomName[0]
                file.save(os.path.join(app.config['UPLOAD_FOLDER_PRODUCTS'], filename))
                img_location = UPLOAD_FOLDER_PRODUCTS + filename

            if not product.create_product(request.form['title'], request.form['description'], request.form['price'],
                                          request.form['expiring_date'], request.form['category_id'],
                                          img_location,
                                          request.form['available_quant'], request.form['pickup_time'],
                                          request.form['slug'],
                                          request.form['status'],
                                          request.form['user_id']):
                error = "No se pudo crear el producto."
                return redirect(url_for('create_product'))
            else:
                return redirect(url_for('list_products'))


# EDIT A PRODUCT
@app.route('/admin/products/edit/<string:slug>', methods=['GET', 'POST'])
def edit_product(slug):
    if session and session['role_id'] == 2:
        if request.method == 'GET':
            producto = product.product_slug(slug)
            return render_template('public/admin/products/edit-product.html', title="Editar Producto",
                                   session=session,
                                   product=producto[0])
    if request.method == 'POST':
        if not product.edit_product(request.form['product_id'], request.form['title'], request.form['description'],
                                    request.form['price'],
                                    request.form['expiring_date'],
                                    request.form['available_quant'],
                                    request.form['slug'],
                                    request.form['status'],
                                    request.form['user_id']):
            error = "No se pudo editar el producto."
            return error
        else:
            return redirect(url_for('list_products'))


# DELETE A PRODUCT
@app.route('/admin/products/delete', methods=['POST'])
def delete_product():
    if session and session['role_id'] == 2:
        if request.method == 'POST':
            if product.delete_product(request.form['product_id']):
                remove(request.form['image_url'])
                return redirect(url_for('list_products'))

    return redirect(url_for('list_products'))


####################### CATEGORIES #####################
def list_categories():
    categories = category.list_categories()
    if len(categories) > 0:
        return categories
    else:
        return "No hay categorias disponibles."


# EXTRA FUNCTIONS
# Checks if there are or are not products in the table 'products'
def check_products():
    if product.list_products():
        products_list = product.list_products()
        return products_list
    else:
        product_list = None
        return product_list


# Brings specified quantity of products
def index_list_products(quant):
    product_list = product.index_list_products(quant)
    if not product_list:
        product_list = None
        return product_list
    else:
        return product_list


# Check if user is owner of the specified product
def user_owns(user_id):
    if product.user_owns(user_id):
        return True
    else:
        return False


# Brings the Products quantity to be shown at Index
def product_count():
    product_count = product.product_count()
    if product_count:
        return product_count
    else:
        return False


# Brings the Orders Done quantity to be shown at Index
def order_count():
    order_count = order.order_count()
    if order_count:
        return order_count
    else:
        return False


# Brings the Users Clients quantity to be shown at Index
def client_count():
    client_count = auth.client_count()
    if client_count:
        return client_count
    else:
        return False


# Brings the Users Seller quantity to be shown at Index
def seller_count():
    seller_count = auth.seller_count()
    return seller_count
    # if seller_count > 0:
    #     return seller_count
    # else:
    #     return seller_count


if __name__ == '__main__':
    app.run(debug=True, port=5002)
