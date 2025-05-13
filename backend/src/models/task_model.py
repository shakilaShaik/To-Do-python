from pydantic import BaseModel
from typing import Optional
class TaskModel(BaseModel):
    id:int
    description:str
    status:Optional[bool]=False
