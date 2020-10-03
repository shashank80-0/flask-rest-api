### POST /api/v1/get_all_products  

Add new product(s)

> - **URL:** `/api/v1/add_product`
> - **Method:** POST
> - **Auth Required:** YES
> - **Request Data Type:** Array (or List) of objects 
> - **Request Data Example:**
```json
[
    {
        "product_name": "Headphones", 
        "brand_name": "Sony", 
        "category_name": "Speakers", 
        "price": 40000.0, 
        "discount": 300.0,
        "quantity": 5
    }, 
    {
        "product_name": "Pen Drive",
        "brand_name": "Kingston",
        "category_name": "Accessory",
        "price": 45000.0,
        "discount": 400.0,
        "quantity": 9
    }
]
```
> ### Success Response
> - **Code:** 200
> - **Response Data Example:** 
```
Product(s) Added
```
> ### Error Response
> - **Code:** 422
> - **Info:** POST does not received required fields (*product_name,brand_name,category_name,quantity,price,discount*)
> - **Response Data Example:**
```
Mandatory field is missing
```
