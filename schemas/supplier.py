from pydantic import BaseModel,Field
from typing import Optional

class Supplier(BaseModel):
    id: Optional[int]= None
    name :str = Field (max_length= 40, min_length=2, description="Supplier name")
    address : str = Field (max_length=40, min_length=2, description = "the brand and product name")
    phone : int = Field(ge=1, description="llave foranea de pelicula")
    email : str = Field (max_length=40, min_length=2, description = "the brand and product name")


class Config: 
    schema_extra = {
        "example":{
            'id':1, 
            'name':'Chocoramo', 
            'brand':'Ramo',
            'desciption': 'Chocoramo is the commercial name given to a rectangular-shaped chocolate-covered cake distributed by the Colombian food company Ramo.',
            'price': 2200, 
            'entry_date': '1972 ' 
        }
    }
    