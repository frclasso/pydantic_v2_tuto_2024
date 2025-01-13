from pydantic import BaseModel, ValidationError
from typing import List, Optional


class Model(BaseModel):
    fields: int
print("Erro 1 ========================")
try:
    Model(fields=None)
except ValidationError as e:
    print(e)

print("Erro 2 ========================")
try:
    Model()
except ValidationError as e:
    print(e)

print("Erro 3 ========================")

class Model2(BaseModel):
    field: Optional[int] = None

print(Model2(field='1'))

print(Model2(field=None))

print("4 ========================")

class Model(BaseModel):
     field: int | None = None   #Python 3.10.12

print(Model2(field='1'))

print(Model2(field=None))

print("Union ...")
from typing import Union

class Model3(BaseModel):
     field: Union[int, None] = None  # Best pratice , mesmo que field: int | None = None

print(Model3(field=0))

print(Model3(field=None))

print("bad option ...")
from typing import Optional

class Model4(BaseModel):
     field: Optional[int] #  required=True

print(Model4.model_fields)
print(Model4(field=0))

print(Model4(field=None))

print("Setting default None")
class Model4(BaseModel):
     field: Optional[int] = None  #  required=False

print(Model4.model_fields)
print(Model4(field=0))

print(Model4(field=None))
