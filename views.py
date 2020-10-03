"""Contains FLask handlers for all REST requests for this API"""

import constants
import datetime
import helpers
import json

import errors
from flask import Response
from flask import request
from main import app
from main import db
from models import Brand
from models import Category
from models import Product
from models import User


def format_response(data, status):
    """Formats API response as JSON data."""
    return Response(json.dumps(data), status)


@app.before_request
def check_auth_token():
    """Verifies requests using JWT token in headers."""
    # /api/v1/authenticate_user is Open endpoint, and doesn't require Oauth token
    if 'authenticate_user' not in request.base_url:
        auth_header = request.headers.get('Authorization')
        try:
            if auth_header:
                auth_token = auth_header.split(" ")[1]
                decoded_token = helpers.decode_auth_token(auth_token)
                if not decoded_token:
                    raise errors.AuthTokenInvalidError
            else:
                raise errors.AuthTokenMissingError
        except errors.AuthTokenInvalidError:
            return format_response("Invalid Auth Token", 403)
        except errors.AuthTokenMissingError:
            return format_response("Auth Token missing", 403)


@app.route('/api/v1/authenticate_user', methods=['POST'])
def authenticate_user():
    """Authenticates a user by verifying username and password."""
    request_data = request.get_json()
    username = request_data["username"]
    password = request_data["password"]
    user = User.query.filter_by(username=username).first()
    try:
        if user:
            if user.password == password:
                # TODO: Encryption/Decryption of User Credentials
                return helpers.encode_auth_token(username)
            else:
                raise errors.IncorrectPasswordError
        else:
            raise errors.UserNotFoundError
    except errors.UserNotFoundError:
        return format_response("Username not found in database", 403)
    except errors.IncorrectPasswordError:
        return format_response("Incorrect Password", 403)


@app.route('/api/v1/get_all_products', methods=['GET'])
def get_all_products():
    """Fetches all products that exist in database."""
    products = Product.query.all()
    products_list = [product.as_dict() for product in products]
    return format_response(products_list, 200)


@app.route('/api/v1/add_product', methods=["POST"])
def add_product():
    """Adds a new product to the database."""
    new_products = request.get_json()
    for new_product in new_products:
        try:
            if set(new_product.keys()) != set(constants.MANDATORY_PRODUCT_FIELDS):
                raise errors.InvalidRequestParametersError
            brand_id = helpers.check_brand(new_product['brand_name'])
            category_id = helpers.check_category(new_product['category_name'])
            float(new_product['price'])
            float(new_product['discount'])
            int(new_product['discount'])
            int(new_product['price'])
        except ValueError:
            raise errors.InvalidRequestParametersError
        except errors.InvalidRequestParametersError:
            return format_response('Mandatory field is missing', 422)
        products = Product(
            product_name=new_product['product_name'],
            price=new_product['price'],
            discount=new_product['discount'],
            quantity=new_product['quantity'],
            created_at=datetime.datetime.now(),
            updated_at=datetime.datetime.now(),
            brand_id=brand_id,
            category_id=category_id
        )
        db.session.add(products)
    db.session.commit()
    return format_response("Product(s) Added", 200)


@app.route('/api/v1/update_product_by_id', methods=['PATCH'])
def update_product_by_id():
    """Updates an already existing product in the database by ID."""
    update_products = request.get_json()
    for update_product in update_products:
        try:
            if 'product_id' not in update_product.keys():
                raise errors.InvalidRequestParametersError
            product = Product.query.filter_by(product_id=update_product['product_id']).first()
            if product is None:
                raise errors.ObjectNotFoundError
        except errors.InvalidRequestParametersError:
            return format_response('Mandatory field is missing', 422)
        except errors.ObjectNotFoundError:
            return format_response('No record found', 404)
        for key in update_product.keys():
            if key == 'product_id' or key not in set(constants.MANDATORY_PRODUCT_FIELDS):
                pass
            elif key == 'brand_name':
                product.brand_id = helpers.check_brand(update_product[key])
            elif key == 'category_name':
                product.category_id = helpers.check_category(update_product[key])
            else:
                setattr(product, key, update_product[key])
        product.updated_at = datetime.datetime.now()
        db.session.flush()
    db.session.commit()
    return format_response("Product(s) Updated", 200)


@app.route('/api/v1/update_product_by_name', methods=['PATCH'])
def update_product_by_name():
    """Updates an already existing product in the database by name."""
    update_products = request.get_json()
    for update_product in update_products:
        try:
            if 'product_name' not in update_product.keys():
                raise errors.InvalidRequestParametersError
            product = Product.query.filter_by(product_name=update_product['product_name']).first()
            if product == None:
                raise errors.ObjectNotFoundError
        except errors.InvalidRequestParametersError:
            return format_response('Mandatory field is missing', 422)
        except errors.ObjectNotFoundError:
            return format_response('No record found', 404)
        for key in update_product.keys():
            if key == 'product_id' or key not in set(constants.MANDATORY_PRODUCT_FIELDS):
                pass
            elif key == 'brand_name':
                product.brand_id = helpers.check_brand(update_product[key])
            elif key == 'category_name':
                product.category_id = helpers.check_category(update_product[key])
            else:
                setattr(product, key, update_product[key])
        product.updated_at = datetime.datetime.now()
        db.session.flush()
    db.session.commit()
    return format_response("Product(s) Updated", 200)


@app.route('/api/v1/delete_product_by_id', methods=['DELETE'])
def delete_product_by_id():
    """Deletes an already existing product in the database by id."""
    product_ids = request.get_json()
    try:
        if not product_ids:
            raise errors.InvalidRequestParametersError
    except errors.InvalidRequestParametersError:
        return format_response('Product ids not received', 403)
    for product_id in product_ids:
        try:
            int(product_id)
        except ValueError:
            return format_response('Invalid Parameters Received', 400)
        try:
            product = Product.query.filter_by(product_id=product_id).first()
            if product is not None:
                db.session.delete(product)
                db.session.flush()
            else:
                raise errors.ObjectNotFoundError
        except errors.ObjectNotFoundError:
            return format_response('Object not found', 404)
    db.session.commit()
    return format_response("Product(s) deleted", 200)


@app.route('/api/v1/delete_product_by_name', methods=['DELETE'])
def delete_product_by_name():
    """Deletes a list of product names from the database."""
    product_names = request.get_json()
    try:
        if not product_names:
            raise errors.InvalidRequestParametersError
    except errors.InvalidRequestParametersError:
        return format_response('Product names not received', 403)
    for product_name in product_names:
        try:
            product = Product.query.filter_by(product_name=product_name).first()
            if product is not None:
                db.session.delete(product)
                db.session.flush()
            else:
                raise errors.ObjectNotFoundError
        except errors.ObjectNotFoundError:
            return format_response('Object not found', 404)
    db.session.commit()
    return format_response("Product(s) deleted", 200)


@app.route('/api/v1/get_product_by_id', methods=['POST'])
def get_product_by_id():
    """Fetches a product by it's id."""
    product_ids = request.get_json()
    try:
        if not product_ids:
            raise errors.InvalidRequestParametersError
    except errors.InvalidRequestParametersError:
        return format_response('Product IDs not received', 403)
    products_list = []
    for product_id in product_ids:
        try:
            product = Product.query.filter_by(product_id=product_id).first()
            if not product:
                raise errors.ObjectNotFoundError
            else:
                products_list.append(product.as_dict())
        except errors.ObjectNotFoundError:
            return format_response('Object not found', 404)
    return format_response(products_list, 200)


@app.route('/api/v1/get_product_by_name', methods=['POST'])
def get_product_by_name():
    """Fetches a single/list of products by names."""
    product_names = request.get_json()
    try:
        if product_names is None:
            raise errors.InvalidRequestParametersError
    except errors.InvalidRequestParametersError:
        return format_response("Product names not received", 403)
    products_list = []
    for product_name in product_names:
        try:
            product = Product.query.filter_by(product_name=product_name).first()
            if not product:
                raise errors.ObjectNotFoundError
            else:
                products_list.append(product.as_dict())
        except errors.ObjectNotFoundError:
            return format_response('Object not found', 404)
    return format_response(products_list, 200)


@app.route('/api/v1/get_product_by_brand', methods=['POST'])
def get_product_by_brand():
    """Fetches a single/list of products by brand names."""
    brand_names = request.get_json()
    try:
        if brand_names is None:
            raise errors.InvalidRequestParametersError
    except errors.InvalidRequestParametersError:
        return format_response("Brand names not received", 403)
    products_dict = {}
    for brand_name in brand_names:
        brand = Brand.query.filter_by(brand_name=brand_name).first()
        brand_list = []
        if brand is None:
            products_dict[brand_name] = brand_list
        else:
            products = Product.query.filter_by(brand_id=brand.brand_id).all()
            for product in products:
                brand_list.append(product.as_dict())
            products_dict[brand_name] = brand_list
    return format_response(products_dict, 200)


@app.route('/api/v1/get_product_by_category', methods=['POST'])
def get_product_by_category():
    """Fetches a single/list of products by category names."""
    category_names = request.get_json()
    try:
        if category_names is None:
            raise errors.InvalidRequestParametersError
    except errors.InvalidRequestParametersError:
        return format_response("Category names not received", 403)
    products_dict = {}
    for category_name in category_names:
        category = Category.query.filter_by(category_name=category_name).first()
        category_list = []
        if category is None:
            category_list = []
            products_dict[category_name] = category_list
        else:
            products = Product.query.filter_by(category_id=category.category_id).all()
            for product in products:
                category_list.append(product.as_dict())
        products_dict[category_name] = category_list
    return format_response(products_dict, 200)


@app.route('/api/v1/get_product_by_price_range', methods=['POST'])
def get_product_by_price_range():
    """Fetches a single/list of products by price range."""
    price_range = request.get_json()
    try:
        if len(price_range) != 2:
            raise errors.InvalidRequestParametersError
        param_1 = float(price_range[0])
        param_2 = float(price_range[1])
    except ValueError:
        return format_response("Invalid Request Parameters", 422)
    except errors.InvalidRequestParametersError:
        return format_response("Invalid Request Parameters", 422)
    min_price = min(param_1, param_2)
    max_price = max(param_1, param_2)
    products = db.session.execute(constants.PRICE_RANGE_QUERY, {'minimum': min_price, 'maximum': max_price})
    products_list = []
    for product in products:
        product = dict(product)
        product['created_at'] = str(product['created_at'])
        product['updated_at'] = str(product['updated_at'])
        products_list.append(product)
    return format_response(products_list, 200)


@app.route('/api/v1/get_product_by_minimum_discount', methods=['POST'])
def get_product_by_minimum_discount():
    """Fetches a single/list of products by minimum discount percentage."""
    discounts = request.get_json()
    products_list = []
    for discount in discounts:
        try:
            discount = float(discount)
        except ValueError:
            return format_response("Invalid Parameters Received", 400)
        products = db.session.execute(constants.MINIMUM_DISCOUNT_QUERY, {'minimum': discount})
        for product in products:
            product = dict(product)
            product['created_at'] = str(product['created_at'])
            product['updated_at'] = str(product['updated_at'])
            products_list.append(product)
    return format_response(products_list, 200)



