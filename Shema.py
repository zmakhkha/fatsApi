
from pydantic import BaseModel
from sqlmodel import Field

class Blog(	BaseModel): 
	id: int| None = Field(default=None, primary_key=True)
	title: str = Field(index=True, max_length=100) 
	content: str= Field(max_length=5000)
	created_at: str | None = Field(default=None)

