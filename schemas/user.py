from pydantic import BaseModel
from typing import Optional

class User(BaseModel):
    id: Optional[int | str | None]
    name: str
    password: str
    email: str

class UserBeforeAfter(BaseModel):
    before: User
    after: User