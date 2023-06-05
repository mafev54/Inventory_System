from pydantic import BaseModel, Field
from typing import Optional


class Product (BaseModel):
    id: Optional[int] = None
    name: str = Field(max_length=40, min_length=2, description="product name")
    brand: str = Field(max_length=40, min_length=2, description="brand name")
    description: str = Field(max_length=500, min_length=5, description="product description")
    price: float = Field(ge=100, le=None, description="price")
    entry_date: str = Field(max_length=60, min_length=4, description="entry date of products")
    availability: str = Field(max_length=60, min_length=2, description="if it is or not avaliability")
    available_quantity: int = Field(ge=100, le=None, description="quantity available")

class Config:
    schema_extra = {
        "example": {
            'id': 1,
            'name': 'red bull',
            'brand': 'Red Bull GmbH',
            'desciption': 'Red Bull is an energy drink distributed by the Austrian company Red Bull GmbH. It was created in the 1980s by the Austrian Dietrich Mateschitz, '
                          'from a formula conceived by the Thai Chaleo Yoovidhya, developing a unique marketing concept.',
            'price': 5550,
            'entry_date': '01/04/1987',
            'availability': 'yes',
            'available_quantity': '40'
        }
    }
