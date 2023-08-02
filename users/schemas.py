from typing import Dict,Optional
from pydantic import BaseModel

class CreateUserRequest(BaseModel):
    username: str
    name: str
    surname: str
    age: int
    gender: str
class UpdateUserRequest(BaseModel):
    username: Optional[str] = None
    name: Optional[str] = None
    surname: Optional[str] = None
    age: Optional[int] = None
    gender: Optional[str] = None
