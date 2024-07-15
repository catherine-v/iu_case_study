from typing import Optional
from pydantic import BaseModel


class ProductSchema(BaseModel):
    id: str
    categories_hierarchy: list[str]
    generic_name: str
    nutriscore_score: Optional[int] = None
    quantity: str
    origins: str
    allergens: str
