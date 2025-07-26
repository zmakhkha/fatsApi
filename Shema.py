from sqlmodel import SQLModel, Field
from typing import Optional

class Blog(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    title: str = Field(index=True, max_length=100)
    content: str = Field(max_length=5000)
    created_at: Optional[str] = Field(default=None)
