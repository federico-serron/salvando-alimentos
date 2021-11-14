from flask import Flask, request, jsonify, render_template, url_for, session
from werkzeug.utils import redirect
from services import auth
from services import product
from services import category

app = Flask(__name__)
app.secret_key = 'Clave_muy_secreta'


@app.route('/')
def index():
    products_list = index_list_products(6)
    return render_template('public/index.html', title='Inicio', session=session, products=products_list)


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
            session['role_id'] = user_info[0]['role_id']
            return redirect(url_for('index'))
    return render_template('public/login/login.html', error=error, title="Acceder")


@app.route('/signup', methods=['POST', 'GET'])
def signup():
    error = None
    if request.method == 'POST':
        if not auth.create_user(request.form['name'], request.form['lastname'], request.form['password'],
                                request.form['email'], request.form['role_id'], request.form['address']):
            error = 'El Email ya esta en uso. Pruebe con otro diferente.'
        else:
            session['name'] = request.form['name']
            session['lastname'] = request.form['lastname']
            session['email'] = request.form['email']
            session['role_id'] = request.form['role_id']
            return redirect(url_for('index'))
    return render_template('public/login/signup.html', error=error, title="Registrate")


@app.route('/logout')
def logout():
    if session:
        if auth.delete_session(session['email']):
            session.clear()
            return redirect(url_for('index'))
        else:
            return "No se pudo cerrar sesion."


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


####################### ADMIN #####################
# DASHBOARD
@app.route('/admin', methods=['GET'])
def admin():
    if session and session['role_id']:
        return render_template('public/admin/index.html', title='Dashboard', session=session)
    else:
        return redirect(url_for('index', error="No tiene permiso para ingresar."))


# PROFILE
@app.route('/profile')
def profile():
    if session and session['role_id']:
        return render_template('public/admin/profile.html', title='Mi Perfil', session=session)
    else:
        return redirect(url_for('index', error="No tiene permiso para ingresar."))


# ORDERS
@app.route('/admin/orders')
def orders():
    if session and session['role_id']:
        return render_template('public/admin/orders.html', title='Mis órdenes', session=session)
    else:
        return redirect(url_for('index', error="No tiene permiso para ingresar."))


# PRODUCTS
@app.route('/admin/products')
def list_products():
    if session and session['role_id'] == 2:
        user_products = product.list_user_products(session['id'])
        return render_template('public/admin/products/list-products.html', title="Listado de productos", products=user_products)
    else:
        return redirect(url_for('index', error="No tiene permiso para ingresar."))


# CREATE A PRODUCT
@app.route('/admin/products/create', methods=['GET', 'POST'])
def create_product():
    if session and session['role_id'] == 2:
        if request.method == 'GET':
            return render_template('public/admin/products/create-product.html', title="Nuevo Producto", session=session)
    if request.method == 'POST':
        if not product.create_product(request.form['title'], request.form['description'], request.form['price'],
                                      request.form['expiring_date'], request.form['category_id'],
                                      request.form['image_url'],
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
        if not product.edit_product(request.form['title'], request.form['description'], request.form['price'],
                                      request.form['expiring_date'], request.form['category_id'],
                                      request.form['image_url'],
                                      request.form['available_quant'], request.form['pickup_time'],
                                      request.form['slug'],
                                      request.form['status'],
                                      request.form['user_id']):
            error = "No se pudo editar el producto."
            return redirect(url_for('edit_product'))
        else:
            return redirect(url_for('list_products'))


####################### CATEGORIES #####################
def list_categories():
    categories = category.list_categories()
    if len(categories) > 0:
        return categories
    else:
        return "No hay categorias disponibles."


if __name__ == '__main__':
    app.run(debug=True, port=5002)
