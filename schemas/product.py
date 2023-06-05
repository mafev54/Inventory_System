from pydantic import BaseModel, Field
from typing import Optional


class Product(BaseModel):
    id: Optional[int]=None
    name : str = Field(max_length=40, min_length=2,description="product name")
    brand : str = Field(max_length=30, min_length=2,description="brand name")
    description : str =Field(max_length=100, min_length=8,description="product description")
    price : float = Field(ge=100)
    entry_date : str = Field(max_length=50, min_length=5,description="product delivery date")
    availability : str = Field (max_length=3, min_length=1, description="product availability")
    available_quantity : int = Field (ge=1, le=10000000)


    class Config:
        schema_extra = {
            "example":{
                "id":1,
                'name':'red bull',
                'brand':'Red Bull GmbH',
                'description':'Red Bull is an energy drink distributed by the Austrian company Red Bull GmbH.',
                'price':5550,
                'entry_date':'01/04/1987',
                'availability':"yes", 
                'available_quantity':1000
            }
        }

