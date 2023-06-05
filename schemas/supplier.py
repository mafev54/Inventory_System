from pydantic import BaseModel,Field
from typing import Optional

class Supplier(BaseModel):
    id: Optional[int]= None
    name :str = Field (max_length= 40, min_length=2, description="Supplier name")
    address : str = Field (max_length=40, min_length=2, description = "address of the supplier")
    phone : int = Field(ge=1, description="phone of supplier")
    email : str = Field (max_length=40, min_length=2, description = "email of supplier")


class Config: 
    schema_extra = {
        "example":{
            'id':1, 
            'name':'red bull', 
            'address':'Red Bull GmbH',
            'phone': 6017494949,
            'email': 'recepcion@redbull.com.' 
        }
    }
    