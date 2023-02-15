from pydantic import BaseModel
from typing import List
from BaseModels import SchedulesBaseModels

class User(BaseModel):
    email: str
    password: str

class User_Schedule(BaseModel):
    email: str
    schedules: List[SchedulesBaseModels.Schedules]