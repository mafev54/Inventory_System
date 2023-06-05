from pydantic import BaseModel, Field
from typing import Optional


class Product (BaseModel):
    id: Optional[int] = None
    name: str = Field(max_length=40, min_length=2, description="product name")
    brand: str = Field(max_length=40, min_length=2, description="brand name")
    description: str = Field(max_length=200, min_length=5, description="product description")
    price: float = Field(ge=100, le=None, description="price")
    entry_date: str = Field(max_length=60, min_length=5, description="entry date of products")
    availability: str = Field(max_length=60, min_length=5, description="if it is or not avaliability")
    available_quantity: int = Field(ge=100, le=None, description="quantity available")

class Config:
    schema_extra = {
        "example": {
            'id': 1,
            'name': 'Chocoramo',
            'brand': 'Ramo',
            'desciption': 'Chocoramo is the commercial name given to a rectangular-shaped chocolate-covered cake distributed by the Colombian food company Ramo.',
            'price': 2200,
            'entry_date': '1972 ',
            'availability': 'yes ',
            'available_quantity': '40 '
        }
    }
