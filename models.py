"""Initializes all model classes based on their MySQL tables."""

from main import db


class Brand(db.Model):
    """Represents Brand table in database"""
    brand_id = db.Column(db.Integer, primary_key=True, nullable=False, autoincrement=True)
    brand_name = db.Column(db.String(45), unique=True, nullable=False)

    def as_dict(self):
        """Converts object to dictionary for easier parsing"""
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}


class Category(db.Model):
    """Represents Category table in database"""
    category_id = db.Column(db.Integer, primary_key=True, nullable=False, autoincrement=True)
    category_name = db.Column(db.String(45), unique=True, nullable=False)

    def as_dict(self):
        """Converts object to dictionary for easier parsing"""
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}


class Product(db.Model):
    """Represents Product table in database"""
    product_id = db.Column(db.Integer, primary_key=True, nullable=False, autoincrement=True)
    product_name = db.Column(db.String(45), nullable=False)
    brand_id = db.Column(db.Integer, db.ForeignKey(Brand.brand_id), nullable=False)
    category_id = db.Column(db.Integer, db.ForeignKey(Category.category_id), nullable=False)
    price = db.Column(db.Float, nullable=False)
    discount = db.Column(db.Float, nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
    created_at = db.Column(db.DateTime, nullable=False)
    updated_at = db.Column(db.DateTime, nullable=False)
    fk_product_brand_brand_id = db.relationship("Brand", backref=db.backref('fk_product_brand_brand_id'), lazy=False)
    fk_product_category_category_id = db.relationship("Category", backref=db.backref('fk_product_category_category_id'),
                                                      lazy=False)

    def as_dict(self):
        """Converts object to dictionary for easier parsing"""
        result = {}
        for c in self.__table__.columns:
            if c.name in ('created_at', 'updated_at'):
                result[c.name] = str(getattr(self, c.name))
            else:
                result[c.name] = getattr(self, c.name)
        return result


class User(db.Model):
    """Represents User table in database"""
    # TODO: Encryption/Decryption of User Credentials
    username = db.Column(db.String(45), primary_key=True, nullable=False)
    password = db.Column(db.String(45), nullable=False)


db.create_all()
