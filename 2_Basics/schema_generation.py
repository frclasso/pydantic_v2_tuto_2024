# JSON Schema Generation
from pydantic import BaseModel

class Model(BaseModel):
    field_1: int | None = None
    field_2: str = "Python"

print(Model.model_json_schema())
print()

from pprint import pprint

pprint(Model.model_json_schema())