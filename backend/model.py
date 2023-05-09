from pydantic import BaseModel #type: ignore

class Todo(BaseModel):
    title: str
    description: str