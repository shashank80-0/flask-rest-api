"""Constants module is used to store constants used frequently."""

MANDATORY_PRODUCT_FIELDS = ['product_name', 'brand_name', 'category_name', 'price', 'quantity', 'discount']
FOREIGN_FIELDS = ['brand_name', 'category_name']
MINIMUM_DISCOUNT_QUERY = 'SELECT * FROM product where (discount/price)*100 >= :minimum'
PRICE_RANGE_QUERY = 'SELECT * FROM product WHERE price >= :minimum and price <= :maximum ORDER BY price'
