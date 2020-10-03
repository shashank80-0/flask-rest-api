### DELETE /api/v1/delete_product_by_id  

Delete product(s) by *product_id* (INTEGER)

> - **URL:** `/api/v1/delete_product_by_id`
> - **Method:** DELETE
> - **Auth Required:** YES
> - **Request Data Type:** Array (or List) of integers
> - **Request Data Example:**
```json
[
    3,
    5,
    6
]
```
> ### Success Response
> - **Code:** 200
> - **Response Data Example:** 
```
Product(s) Deleted
```
> ### Error Respone
> - **Code:** 404
> - **Response Data Example:**
```
Object not found
```
> **Info:** POST received non-existing *product_name*

> - **Code:** 403
> - **Response Data Example:**
```
Product ids not received
```
> **Info:** POST received empty list

> - **Code:** 400
> - **Response Data Example:**
```
Invalid Parameter Received
```
> **Info:** POST received non integer value

### DELETE /api/v1/delete_product_by_name  

DELETE product(s) by *product_name* (STRING)

> - **URL:** `/api/v1/update_product_by_id`
>- **Method:** PATCH
> - **Auth Required:** YES
> - **Request Data Example:**
```json
[
    "Macbook",
    "Bean Bag",
    "Headphone"
]
```
> ### Success Response
> - **Code:** 200
> - **Response Data Example:** 
```
Product(s) Deleted
```
> ### Error Respone
> - **Code:** 404
> - **Response Data Example:**
```
Object not found
```
> **Info:** POST received non-existing product_name

> - **Code:** 403
> - **Response Data Example:**
```
Product names not received
```
> **Info:** POST received empty list



