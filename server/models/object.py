
from typing import Optional
from pydantic import BaseModel
from datetime import datetime

class CreateObjectRequest(BaseModel):
    field_one: str
    field_two: int
    created_at: datetime = datetime.now()

class UpdateObjectRequest(BaseModel):
    field_one: str | None = None
    field_two: int | None = None