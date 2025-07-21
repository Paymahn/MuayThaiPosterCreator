from pydantic import BaseModel
from typing import Literal
import datetime

class Fighter(BaseModel):
    name : str
    nationality : str
    title_fight : bool = False
    gender: Literal['Male', 'Female']
    imageFile : str

class EventConfig(BaseModel):
    eventName : str
    eventDate : datetime.date
    fighters : list[Fighter]
    theme : str
    venue : str




