


'''
Explanation:

from fastapi import FastAPI: Imports the FastAPI class.
app = FastAPI(): Creates an application instance (used by Uvicorn to run the server).
@app.get("/"): Defines the root (/) route for GET requests.
def read_root(): A function that runs when the route is accessed.
return {"message": "Hello World"}: Returns a JSON response.

Standard HTTP methods: Operations on resources are performed using well-defined methods:
GET: Retrieve data
POST: Create new data
PUT: Update existing data
DELETE: Remove data
'''



# to run it on server use :       python -m uvicorn main:app --reload
from fastapi import FastAPI, Request
from mockdata import products
from dtos import productsDTO

# Create FastAPI app instance
app = FastAPI()

# Define a simple GET endpoint
@app.get("/")
def home():
    return {"message": "Hello World"}

# '''# contact path 
# @app.get("/contact")
# def contact():
#     return {'contact' : 'this is our contact route'}
# '''

# import the mocked data and return 
@app.get('/products')
def get_products():
    return products

# visit this for result : http://127.0.0.1:8000/products




#==============================================================================================
# if you want to access specific id from the product you can get it by path and query parameter
#4 Path Parameters & Query Parameters


# path params
@app.get('/product/{product_id}')
def get_one_product(product_id:int):

# if product is available for given id  return product else error msg
    for oneproduct in products:
        if oneproduct.get('id') == product_id:
            return oneproduct
    return {
        'error' : 'prduct not found for this id'
    }

# :http://127.0.0.1:8000/product/1



# query parameter
'''@app.get("/greet")
def get_greet(name:str, age:int):
    return {
        'greet': f'Hello {name} your age is {age} , how are you'
    }

# :http://127.0.0.1:8000/greet?name=hamid&age=21'''

# if we have nth number of request we import "from fastapi import FastAPI, request"
@app.get("/greet")
def get_greet(request:Request):
    query_params = dict(request.query_params)
    return {
        'greet': f'Hello {query_params.name} your age is {query_params.age} , how are you'
    }
#http://127.0.0.1:8000/greet?name=hamid&age=21





#==============================================================================================
# different https method

# GET: to get something from the server 
# POST: where client send data to server to store it in database
# PUT: client send some data and data_id to update the data on server
# DELETE :  client send some data and data_id to delete the data on server



# POST:

@app.post('/create_product')
def create_product(product_data: productsDTO):
    product_data = product_data.model_dump()      # pydentic object to convert normal data into dictinoary
    products.append(product_data)                   # this will append data mockdata and store
    print(product_data)
    return {'status' : 'product created succesfully',"data":products }

#i get this data from the postman body:    {'id': 3, 'name': 'banana', 'price': 1500, 'count': 30}


# you can send data from client to backend using body, header-header_request and query parameter
# 1 = request boyd : body and with the pydantic




# PUT:
@app.put('/update_product/{product_id}')
def update_product(product_data: productsDTO, product_id:int):  # send data and id for update
    for index, oneproduct in enumerate(products):
        if oneproduct.get("id") == product_id:
            products[index] = product_data.model_dump()
            return {'status' : 'product updated succesfully', 'product':product_data}

    return {
            'error' : 'prduct not found for this id'
    }

# http://127.0.0.1:8000/update_product/2




# DELETE
@app.delete('/delete_product/{product_id}')
def delete_product(product_id:int):
    for index, oneproduct in enumerate(products):
        if oneproduct.get("id") == product_id:
            deleted_product = products.pop(index)
            return {'status' : 'product updated succesfully', 'product': deleted_product}

    return {
        'error' : 'prduct not found for this id'
    }
