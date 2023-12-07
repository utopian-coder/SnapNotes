from pydantic import BaseModel

class NoteModel(BaseModel):
    title: str
    description: str