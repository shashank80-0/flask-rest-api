"""Contains all the util functions used in the API."""

import datetime
import logging

import jwt

from main import app
from main import db
from models import Brand
from models import Category


def check_brand(brand_name):
    """
    Checks if brand is available in database already, else adds and returns id
    :param brand_name: Name of the brand to search in database.
    :return: int: Id of the brand that already exists/is inserted in the database.
    """
    brand = Brand.query.filter_by(brand_name=brand_name).first()
    if brand is None:
        # Brand doesn't exist in database, so insert it and return brand_id
        new_brand = Brand(brand_name=brand_name)
        db.session.add(new_brand)
        db.session.flush()
        brand_id = Brand.query.filter_by(brand_name=brand_name).first().brand_id
    else:
        # Brand already exists in database, so return brand_id
        brand_id = brand.brand_id
    return brand_id


def check_category(category_name):
    """
    Checks if category is available in database already, else adds and returns id
    :param category_name: Name of the category to search in database.
    :return: int: Id of the category that already exists/is inserted in the database.
    """
    category = Category.query.filter_by(category_name=category_name).first()
    if category is None:
        # Category doesn't exist in database, so insert it and return category_id
        new_category = Category(category_name=category_name)
        db.session.add(new_category)
        db.session.flush()
        category_id = Category.query.filter_by(category_name=category_name).first().category_id
    else:
        # Category already exists in database, so return category_id
        category_id = category.category_id
    return category_id


def encode_auth_token(username):
    """
    Generates the Auth Token
    :param username: Username to be encoded in JWT token for authentication.
    :return: string: Encoded JWT token
    """
    try:
        payload = {
            'exp': datetime.datetime.utcnow() + datetime.timedelta(days=1),
            'iat': datetime.datetime.utcnow(),
            'sub': username
        }
        return jwt.encode(
            payload,
            app.config.get('SECRET_KEY'),
            algorithm='HS256'
        )
    except Exception as e:
        logging.error("Couldn't generate JWT Token")
        return e


def decode_auth_token(auth_token):
    """
    Decodes the auth token
    :param auth_token: Authentication token received in request
    :return: integer|string/None
    """
    try:
        payload = jwt.decode(auth_token, app.config.get('SECRET_KEY'))
        return payload['sub']
    except jwt.ExpiredSignatureError:
        # TODO: Raise
        return None
    except jwt.InvalidTokenError:
        # TODO: Raise
        return None
