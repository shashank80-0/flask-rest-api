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
> - **Info:** POST received non-existing *product_id*
> - **Response Data Example:**
```
Object not found
```
> - **Code:** 403
>  -**Info:** POST received empty list
> - **Response Data Example:**
```
Product ids not received
```
> - **Code:** 400
> - **Info:** POST received non integer value  
> - **Response Data Example:**
```
Invalid Parameter Received
```

### DELETE /api/v1/delete_product_by_name  

DELETE product(s) by *product_name* (STRING)

> - **URL:** `/api/v1/delete_product_by_name`
>- **Method:** DELETE
> - **Auth Required:** YES
> - **Request Data Type:** Array (or List) of strings
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
> ### Error Response
> - **Code:** 404
> - **Info:** POST received non-existing *product_name*
> - **Response Data Example:**
```
Object not found
```
> - **Code:** 403
> - **Info:** POST received empty list
> - **Response Data Example:**
```
Product names not received
```




