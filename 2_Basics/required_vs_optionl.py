from pydantic import BaseModel
from typing import Deque, List, Optional, Tuple

class Circle(BaseModel):
    center: Optional[tuple] = None
    radius: int

print(Circle.model_fields)
print()

class Circle(BaseModel):
    center: Optional[tuple] = [int, int]
    radius: int

print(Circle.model_fields)
print()
print(Circle(center=[0,0],radius=1))
print()
data = {'radius':1}
data_json = '{"radius":1}'
print(Circle.model_validate(data))
print(Circle.model_validate_json(data_json))
