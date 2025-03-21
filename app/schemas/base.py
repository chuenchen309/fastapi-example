from pydantic import BaseModel, Field
from typing import Optional, Union, List, Dict
from enum import Enum

class GenderEnum(str, Enum):
    male = 'male'
    female = "female"
    other = "other"

class TemplateModel(BaseModel):
    name: str
    age: int = 18
    language: str = Field(default="zh-TW")
    gender: GenderEnum = GenderEnum.male
