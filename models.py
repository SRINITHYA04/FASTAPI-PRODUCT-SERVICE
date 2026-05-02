from pydantic import BaseModel, Field
from typing import Optional

class Product(BaseModel):
    id: int = Field(ge=1)
    name: str = Field(min_length=1 , max_length=50)
    price: float = Field(ge=1)
    description: str = Field(min_length=5, max_length=100)
    quantity: int 

 
class Products(BaseModel):
    name: Optional[str] = Field(default=None, min_length=1 , max_length=50)
    price: Optional[float] = Field(default=None,ge=1)
    description: Optional[str] = Field(default=None,min_length=5, max_length=100)
    quantity: Optional[int] =None
  

