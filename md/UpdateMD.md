### PATCH /api/v1/update_product_by_id  

Update product(s) by *product_id* (INTEGER)

> - **URL:** `/api/v1/update_product_by_id`
> - **Method:** PATCH
> - **Auth Required:** YES
> - **Request Data Type:** Array (or List) of objects 
> - **Request Data Example:**
```json
[
    {   
        "product_id":10,
        "product_name":"Washing Machine",
        "quantity":2, 
        "price": 25000.0 
    },
    {   
        "product_id":9,
        "product_name":"Dryer", 
        "price": 2000.0,
        "discount":100 
    }
]
```
> ### Success Response
> - **Code:** 200
> - **Response Data Example:** 
```
Product(s) Updated
```
> ### Error Response
> - **Code:** 422
> - **Response Data Example:**
```
Mandatory field is missing
```
> **Info:** POST does not received *product_id*  

> - **Code:** 404
> - **Response Data Example:**
```
No record found
```
> **Info:** POST received empty list

### PATCH /api/v1/update_product_by_name  

Update product(s) by *product_id* (STRING)

> - **URL:** `/api/v1/update_product_by_id`
> - **Method:** PATCH
> - **Auth Required:** YES
> - **Request Data Example:**
```json
[
    {   
        "product_name":"Bean Bag", 
        "quantity":2, 
        "price": 20000.0 
    }, 
    {   
        "product_name": "Macbook",
        "brand_name":"Apple",
        "discount": 400.0,
        "quantity": 9
    }
]
```
> ### Success Response
> - **Code:** 200
> - **Response Data Example:** 
```
Product(s) Updated
```
> ### Error Response
> - **Code:** 422
> - **Response Data Example:**
```
Mandatory field is missing
```
**Info:** POST does not received *product_name*

> - **Code:** 404
> - **Response Data Example:**
```
No record found
```
>**Info:** POST received empty list
