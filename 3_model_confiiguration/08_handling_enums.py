from enum import Enum

class Color(Enum):
    red = "Red"
    green = "Green"
    blue = "Blue"
    orange = "Orange"
    yellow = "Yellow"
    cyan = "Cyan"
    white = "White"
    black = "Black"

print(Color.red.value)
print(type(Color.red))


from pydantic import BaseModel, ConfigDict, ValidationError

class Model(BaseModel):
    color: Color

print(Model(color=Color.red))

# deserilizing json
data = """
{
    "color": "Blue"
}
"""
print(Model.model_validate_json(data))

# With we use some value not present in the Enum content, we receive a ValidationError
data = """
{
    "color": "Magenta"
}
"""
try:
    Model.model_validate_json(data)
except ValidationError as e:
    print(e)

print()
print("Serializing json...")
data = """
{
    "color": "Red"
}
"""
m = Model.model_validate_json(data)
print(m.model_dump())
print(m.model_dump_json())

print()
output = m.model_dump()
print(output)
import json
# json.dumps(output)  # Error


print()
print("Using enum values ...")
class Model(BaseModel):
    model_config = ConfigDict(use_enum_values=True)

    color: Color

m2 = Model(color=Color.cyan)
print(m2)
print(type(m2.color))
print(m2.model_dump())
print(m2.model_dump_json())

print()
print("Default values ...")
class Model(BaseModel):
    model_config = ConfigDict(use_enum_values=True)
    color: Color = Color.red # default value

m3 = Model()
print(m3)
m4 = Model(color=Color.blue)
print(m4)

print()
print("Getting the values ...")
class Model(BaseModel):
    model_config = ConfigDict(use_enum_values=True)
    color: Color = Color.red.value # setting the value

m5 = Model()
print(m5)

print()
print("Validating values using validate_defaults function ...")
class Model(BaseModel):
    model_config = ConfigDict(use_enum_values=True, validate_default=True)
    color: Color = Color.red

m6 = Model()
print(m6)