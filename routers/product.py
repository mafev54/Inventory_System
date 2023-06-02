from fastapi import APIRouter, Path, Query
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.encoders import jsonable_encoder

from service.product import ProductService
from schemas.product import Product
from config.database import Session 


product_router = APIRouter()

@product_router.get('/product_hello', tags=['product'], status_code=200)
def get_product_hello():
    #funcion to check the route
    return HTMLResponse('<h1>Hola desde la ruta d genres</h1>1')

@product_router.get('/product', tags = ['product'], status_code=200)
def get_product():
    db = Session()
    result = ProductService(db).get_product()
    return JSONResponse(content=jsonable_encoder(result), status_code= 200)

@product_router.get('/product_for_id', tags=['product'],status_code=200)
def get_product_for_id(id:int):
    db = Session()
    result = ProductService(db).get_for_id(id)
    return JSONResponse(content=jsonable_encoder(result), status_code= 200)

@product_router.post('/product',tags=['product'], status_code=201)
def create_product(product:Product):
    db = Session()
    ProductService(db).create_product(product)
    return JSONResponse(content={"message":"genre created successfully",'status_code':201})

@product_router.put('/product{id}',tags=['product'])
def update_product(id:int,product:Product):
    db = Session()
    result = ProductService(db).get_for_id(id)
    if not result:
        return JSONResponse(content={"message":"genre don't gound","status_code":404})
    ProductService(db).update_genre(product)
    return JSONResponse(content={"message":"genre update successfully",'status_code':202}, status_code=200)


@product_router.delete('/product{id}', tags=['product'])
def delete_product(id:int):
    db = Session()
    result = ProductService(db).get_for_id(id)
    if not result:
        return JSONResponse(content={"message":"genre don't gound","status_code":404})
    ProductService(db).delete_product(id)
    return JSONResponse(content={"message":"genre delete successfully",'status_code':200}, status_code=200)