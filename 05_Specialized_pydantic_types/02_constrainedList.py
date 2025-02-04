from pydantic import BaseModel, PositiveInt, ValidationError
import logging

class Circle(BaseModel):
    center: tuple[int, int] = (0,0)
    radius: PositiveInt = 1

class Sphere(BaseModel):
    center: tuple[int, int] | tuple[int, int, int] = (0,0)
    radius: PositiveInt = 1

print(Sphere(center=(1,1), radius=10))
print(Sphere(center=(1,1, 2), radius=10))
try:
    Sphere(center=(1,2,3,4))
except ValidationError as e:
    logging.error(e)

print()
print()

from pydantic import conlist



# class Sphere(BaseModel):
#     center: conlist(item_type: int, min_length:2, max_length:3) = [0,0]
#     radius: PositiveInt = 1

print(Sphere(center=(1,1), radius=10))
