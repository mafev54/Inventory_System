from fastapi import APIRouter, Path, Query
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.encoders import jsonable_encoder

from service.supplies import SuppliesService
from schemas.supplies import Supplies
from config.database import Session 

supplie_router = APIRouter()

@supplie_router.get('/supplie_hello', tags=['supplie'], status_code=200)
def get_supplie_hello():
    #funcion to check the route
    return HTMLResponse('<h1>Hello from the supplies route</h1>1')

@supplie_router.get('/supplie', tags = ['supplie'], status_code=200)
def get_supplie():
    db = Session()
    result = SuppliesService(db).get_supplie()
    return JSONResponse(content=jsonable_encoder(result), status_code= 200)

@supplie_router.get('/supplie_for_id', tags=['supplie'],status_code=200)
def get_supplie_for_id(id:int):
    db = Session()
    result = SuppliesService(db).get_for_id(id)
    return JSONResponse(content=jsonable_encoder(result), status_code= 200)

@supplie_router.post('/supplie',tags=['supplie'], status_code=201)
def create_supplie(supplie:Supplies):
    db = Session()
    SuppliesService(db).create_supplie(supplie)
    return JSONResponse(content={"message":"supplies created successfully",'status_code':201})

@supplie_router.put('/supplie{id}',tags=['supplie'])
def update_supplie(id:int, data :Supplies):
    db = Session()
    result = SuppliesService(db).get_for_id(id)
    if not result:
        return JSONResponse(content={"message":"supplies don't found","status_code":404})
    SuppliesService(db).update_supplie(data, id)
    return JSONResponse(content={"message":"supplies update successfully",'status_code':202}, status_code=200)

@supplie_router.delete('/supplie{id}', tags=['supplie'])
def delete_supplie(id:int):
    db = Session()
    result = SuppliesService(db).get_for_id(id)
    if not result:
        return JSONResponse(content={"message":"supplies don't found","status_code":404})
    SuppliesService(db).delete_supplie(id)
    return JSONResponse(content={"message":"supplies delete successfully",'status_code':200}, status_code=200)