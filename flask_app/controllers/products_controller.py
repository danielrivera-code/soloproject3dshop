from flask_app import app
from flask import redirect, render_template, request, session, flash
from flask_app.models.user import User
from flask_app.models.product import Product
from datetime import datetime


@app.route('/products/dashboard')
def products_dashboard():
    if session['user_id']:
        session.pop('form_input', None)
        this_user = User.get_by_id(session['user_id'])
        session['user_name'] = f"{this_user.first_name} {this_user.last_name}"
        return render_template('dashboard.html', user_products = Product.get_all_products()  )
    return redirect('/')

@app.route('/products/create', methods=['post'])
def products_create():
    if session['user_id']:
        print(request.form)
        session['form_input'] = request.form.to_dict()
        if Product.valid(request.form):
            Product.save(request.form)
            session.pop('form_input', None)
            return redirect('/products/dashboard')
        return redirect('/products/new')
    return redirect('/')

@app.route('/products/remove_product/<int:product_id>')
def products_remove_product(product_id):
    if session['user_id']:
        Product.delete_by_id(product_id)
        return redirect('/products/dashboard')
    return redirect('/')

@app.route('/products/details/<int:product_id>')
def product_details(product_id):
    if session['user_id']:
        return render_template('details.html', product = Product.get_by_id(product_id) )
    return redirect('/')

@app.route('/products/edit/<int:product_id>')
def product_edit(product_id):
    if session['user_id']:
        return render_template('edit.html', product = Product.get_by_id(product_id) )
    return redirect('/')


@app.route('/products/update/<int:product_id>', methods=['post'])
def products_update(product_id):
    if session['user_id']:
        if Product.edit_valid(request.form):
            Product.update_product(request.form, product_id)
            return redirect('/products/dashboard')
        return redirect(f'/products/edit/{product_id}')
    return redirect('/')

@app.route('/products/show')
def products_show():
    if session['user_id']:
        session.pop('form_input', None)
        this_user = User.get_by_id(session['user_id'])
        session['user_name'] = f"{this_user.first_name} {this_user.last_name}"
        return render_template('created_products.html', user_products = Product.get_all_products()  )
    return redirect('/')



@app.route('/products/new')
def products_new():
    if session['user_id']:
        if 'form_input'not in session:
            session['form_input'] = {
            'destination' : '',
            'pick_up' : '',
            'ride_date' : '',
            'details' : '',
        }
        this_user = User.get_by_id(session['user_id'])
        session['user_name'] = f"{this_user.first_name} {this_user.last_name}"
        return render_template('create_products.html', form_input = session['form_input']
        )
    return redirect('/')

@app.route('/products/cart/<int:product_id>')
def product_cart(product_id):
    if session['user_id']:
        return render_template('cart_product.html', product = Product.get_by_id(product_id) )
    return redirect('/')