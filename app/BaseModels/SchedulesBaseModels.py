from pydantic import BaseModel
from datetime import datetime

class Schedules(BaseModel):
    title: str
    date: datetime