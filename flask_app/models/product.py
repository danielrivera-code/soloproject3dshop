from flask_app.config.mysqlconnection import connect
from flask_app.models import user
from flask import flash, session
from datetime import datetime
from pprint import pprint
current_time = datetime.now()


class Product:
    DB = 'solo_project'
    def __init__(self, data):
        self.id = data['id']
        self.product_name = data['product_name']
        self.description = data['description']
        self.link_to_image = data['link_to_image']
        self.product_price = data['product_price']
        self.product_available = data['product_available']
        self.posted_id = data['posted_id']
        self.product_creator_id = data['product_creator_id']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.poster = None
        self.creator = None

    @classmethod
    def update_product(cls, form_data, product_id):
        query = """
        UPDATE products
        SET product_name = %(product_name)s,
        description = %(description)s,
        link_to_image = %(link_to_image)s,
        product_price = %(product_price)s,
        product_available = %(product_available)s
        WHERE id = %(id)s;
        """
        data = form_data.to_dict()
        data['id'] = product_id
        connect(cls.DB).query_db(query, data)


    @classmethod
    def get_all_products_by_user(cls):
        query = """
        SELECT *
        FROM products
        WHERE posted_id = %(id)s
        """
        results = connect(cls.DB).query_db(query, {'id':session['user_id']})
        print(results)
        output = []
        for each_dict in results:
            output.append(cls(each_dict))
        return output


    @classmethod
    def get_by_id(cls, product_id):
        query = """
        SELECT *
        FROM products p
        JOIN users
        ON p.posted_id = users.id
        WHERE p.id = %(id)s;
        """
        
        data = {'id' : product_id}
        results = connect(cls.DB).query_db(query, data)
        print(results)
        this_product = cls(results[0])
        for each_dict in results:
            print(each_dict)
            poster_data = {
                "id" : each_dict['users.id'],
                "first_name" : each_dict['first_name'],
                "last_name" : each_dict['last_name'],
                "email" : each_dict['email'],
                "password" : None,
                "created_at" : each_dict['users.created_at'],
                "updated_at" : each_dict['users.updated_at']
            }
            this_product.poster = user.User(poster_data)
        return this_product

    @classmethod
    def get_all_products(cls):
        query = """
        SELECT *
        FROM products p
        JOIN users
        ON p.posted_id = users.id
        """
        
        results = connect(cls.DB).query_db(query)
        output = []
        for each_dict in results:
            this_product = cls(each_dict)
            print(each_dict)
            poster_data = {
                "id" : each_dict['users.id'],
                "first_name" : each_dict['first_name'],
                "last_name" : each_dict['last_name'],
                "email" : each_dict['email'],
                "password" : None,
                "created_at" : each_dict['users.created_at'],
                "updated_at" : each_dict['users.updated_at']
            }
            this_product.poster = user.User(poster_data)
            output.append(this_product)
        return output
    
    @classmethod
    def delete_by_id(cls, product_id):
        query = """
        DELETE
        FROM products
        Where id = %(id)s;
        """
        data = {"id": product_id}
        connect(cls.DB).query_db(query, data)


    @classmethod
    def save(cls, form_data):
        query = """
        INSERT INTO products
        (product_name, description, link_to_image, product_price, product_available, posted_id)
        VALUES (%(product_name)s, %(description)s, %(link_to_image)s, %(product_price)s, %(product_available)s, %(posted_id)s);
        """
        data = form_data.to_dict()
        data['posted_id'] = session['user_id']
        print(data)
        product_id = connect(cls.DB).query_db(query, data)
        print(product_id)

    @staticmethod
    def valid(form_data):
        is_valid = True
        if not form_data['product_name'].strip():
            is_valid = False
            flash('Product Name Required', 'product')
        elif len(form_data['product_name']) < 2:
            is_valid = False
            flash('Product Name must be at least 2 Char Min', 'product')
        
        if not form_data['description'].strip():
            is_valid = False
            flash('Description Required', 'product')
        elif len(form_data['description']) > 60:
            is_valid = False
            flash('Description Max 60 Characters', 'product')

        if not form_data['link_to_image'].strip():
            is_valid = False
            flash('Link to image Required', 'product')
        elif len(form_data['link_to_image']) < 2:
            is_valid = False
            flash('Link address must be longer', 'product')
        
        if not form_data['product_price'].strip():
            is_valid = False
            flash('Product Price Required', 'product')
        elif len(form_data['product_price']) < 1:
            is_valid = False
            flash('Price must be at least 2 Decimal Characters Min', 'product')
        
        if not form_data['product_available'].strip():
            is_valid = False
            flash('Product Availability Required', 'product')
        elif len(form_data['product_available']) < 0:
            is_valid = False
            flash('Availability must greater than or equal to 0', 'product')

        return is_valid
    
    @staticmethod
    def edit_valid(form_data):
        is_valid = True
        
        if not form_data['product_name'].strip():
            is_valid = False
            flash('Product Name Required', 'product')
        elif len(form_data['product_name']) < 2:
            is_valid = False
            flash('Product Name must be at least 2 Char Min', 'product')

        if not form_data['description'].strip():
            is_valid = False
            flash('Description Required', 'product')
        elif len(form_data['description']) > 60:
            is_valid = False
            flash('Description Max 60 Characters', 'product')

        if not form_data['link_to_image'].strip():
            is_valid = False
            flash('Link to image Required', 'product')
        elif len(form_data['link_to_image']) < 2:
            is_valid = False
            flash('Link address must be longer', 'product')
        
        if not form_data['product_price'].strip():
            is_valid = False
            flash('Product Price Required', 'product')
        elif len(form_data['product_price']) < 1:
            is_valid = False
            flash('Price must be at least 2 Decimal Characters Min', 'product')
        
        if not form_data['product_available'].strip():
            is_valid = False
            flash('Product Availability Required', 'product')
        elif len(form_data['product_available']) < 0:
            is_valid = False
            flash('Availability must greater than or equal to 0', 'product')

        return is_valid