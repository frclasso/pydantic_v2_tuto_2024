from pydantic import BaseModel, PositiveInt,ValidationError
import logging

class Circle(BaseModel):
    center: tuple[int, int] = (0,0)
    radius: PositiveInt = 1

print(Circle())
print(Circle(radius=2))
print(Circle(center=(1,1), radius=2))
print()
try:
    Circle(center=(0.5, 0.5), radius=0)
except ValueError as e:
    logging.error(e)
print()
print(Circle.model_fields)