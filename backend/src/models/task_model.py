from pydantic import BaseModel
from typing import Optional
class TaskModel(BaseModel):
   
    description:str
    status:Optional[bool]=False
