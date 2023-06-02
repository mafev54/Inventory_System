from sqlalchemy import column, Integer, String, Float

from config.database import Base

class Product(Base):
    
    __tablename__ = "product"
    
    id = column(Integer,primary_key = True)
    name = column (String)
    brand = column (String)
    description = column (String)
    price = column (Float)
    entry_date = column (Integer)