# Strict and Lax Coercion

from pydantic  import BaseModel, ConfigDict , ValidationError
import json
from pprint import pprint

class Model(BaseModel):
    field_1: str
    field_2: float
    field_3: list
    field_4: tuple

try:
    Model(field_1 = 100,field_2=1, field_3=(1,2,3), field_4=[1,2,3])
except ValidationError as e:
    print(e)

print()

print(Model(field_1 = "abc",field_2=1, field_3=(1,2,3), field_4=[1,2,3]))
print()

class Model(BaseModel):
    model_config = ConfigDict(strict=True)

    field_1: str
    field_2: float
    field_3: list
    field_4: tuple

print("Using model_config")
try:
    Model(field_1 = "abc", field_2=1, field_3=(1,2,3), field_4=[1,2,3])
except ValidationError as e:
    print(e)
print()


json_data = '''
{
    "field_1": true,
    "field_2": 10,
    "field_3": 1,
    "field_4": null,
    "field_5": [1,2,3],
    "field_6": ["a", "b","c"],
    "field_7": {"a":1, "b":2}
}
'''


class Model(BaseModel):
    """
    "field_1": bool
    "field_2": float
    "field_3": int
    "field_4": nullable string
    "field_5": tuple of integers
    "field_6": set of strings
    "field_7": dictionary
    """
    field_1: bool
    field_2: float
    field_3: int
    field_4: str | None
    field_5: tuple[int, ...] # ... about length
    field_6: set[str]
    field_7: dict

data = Model.model_validate_json(json_data)
print("Data")
print(data)
print(type(data.field_5)) # <class 'tuple'>, originally was a list
print()

# Changing values

json_data_modified = '''
{
    "field_1": true,
    "field_2": 10,
    "field_3": 1,
    "field_4": null,
    "field_5": [1,2, 3.5 ],
    "field_6": ["a", "b", 100],
    "field_7": {"a":1, "b":2}
}
'''
print("Data_modified")
try:
     Model.model_validate_json(json_data_modified)
except ValidationError as e:
    print(e)

