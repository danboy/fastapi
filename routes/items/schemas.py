from pydantic import BaseModel
from typing import Optional, Union
from uuid import UUID

class ItemSchema(BaseModel):
    id: Optional[UUID] = None
    name: str
    active: bool = True
