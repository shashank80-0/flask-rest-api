# RESTAPI Documentation

This REST API is created in FLASK  

## How to set up

> Update app.config['SQLALCHEMY_DATABASE_URI'] variable to point to your mysql database
 >> **Format example** - mysql+pymysql://*username*:*password*@*hostname*:*port*/*database_name*

> Install the dependencies mentioned in the requirements.txt
 >> `pip install -r requirements.txt`

> Run below command line to start API
```
python main.py
```

## API ENDPOINTS

### POST /api/v1/authenticate_user  

Provide the user with Auth Key

> - **Request Data Type** - Object
> - **Request Data Example** - 
```
{
    "username" : *your username*, 
    "password" : *yourpassword*
}
```
> ### Success Response
> - **Response Data Example** - 
```
*Auth Token* 
```
> ### Error Response
> - **Code:** 403
> - **Response Data Example:**
```
Username not found in database
Incorrect Password
```
> **Info:** *username* or *password* is incorrect

## All endpoints require Authentication  

**Important:** header = `{"Authorization" : Bearer {your Auth Token}}` must be present to use API

### GET /api/v1/get_all_products  

Get the details of all the products in the database.

> - **URL:** `/api/v1/get_all_products`
> - **Method:** GET
> - **Auth Required:** YES

> ### Success Response
> - **Code:** 200
> - **Response Data Example:**
```json
[
    {
        "product_id": 2, 
        "product_name": "Notebook", 
        "brand_id": 3, 
        "category_id": 3, 
        "price": 40000.0, 
        "discount": 300.0,
        "quantity": 5, 
        "created_at": "2020-10-02 15:01:28", 
        "updated_at": "2020-10-02 21:58:45"
    }, 
    {
        "product_id": 3,
        "product_name": "Logitech",
        "brand_id": 3,
        "category_id": 3,
        "price": 45000.0,
        "discount": 400.0,
        "quantity": 9,
        "created_at": "2020-10-02 15:42:58",
        "updated_at": "2020-10-02 21:58:45"
    }
]
```

- [ADD PRODUCTS](md/AddMD.md)  

- [UPDATE PRODUCTS](md/UpdateMD.md)  

- [DELETE PRODUCTS](md/DeleteMD.md)  

- [FILTER PRODUCTS](md/FilterMD.md)  



