from pydantic import BaseModel,Field
from typing import Optional

class Supplies(BaseModel):
    id: Optional[int]= None
    product_id :int = Field(ge=1, description="llave foranea de pelicula")
    address : int = Field(ge=1, description="llave foranea de pelicula")
    purchase_price : float = Field(ge=1, description="llave foranea de pelicula")
    
    
class Config: 
    schema_extra = {
        "example":{
            'id':1, 
            'product_id':'1', 
            'address':'2',
            'purchase_price': '3.4.'
        }
    }
    