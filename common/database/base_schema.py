from pydantic import BaseModel
from common.utils import to_camel_case


class Base(BaseModel):
    class Config:
        orm_mode = True
        alias_generator = to_camel_case
        allow_population_by_field_name = True
