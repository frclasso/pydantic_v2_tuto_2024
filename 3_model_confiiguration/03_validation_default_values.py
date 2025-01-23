from pydantic  import BaseModel, ConfigDict , ValidationError
import json
from pprint import pprint

class Model(BaseModel):
    field_1: int = None  # no sense, will be ignored and coerced to null
    field_2: str = 100   # no sense, will be ignored and coerced to integer

print(Model()) # field_1=None field_2=100

try:
    Model(field_1=None, field_2=100)
except ValidationError as e:
    print(e)

print()
print("Validatiting defaults")
class Model(BaseModel):
    model_config = ConfigDict(validate_default=True)  # by default it's False

    field_1: int = None 
    field_2: str = 10

try:
    Model()
except ValidationError as e:
    print(e)