from pydantic import BaseModel, ConfigDict, ValidationError


class Model(BaseModel):

    field: int

m =  Model(field=20)
m.field = 30
print(m)

print()
print("Using frozen ...")
class Model(BaseModel):
    model_config = ConfigDict(frozen=True)
    field: int

m =  Model(field=20)
try:
    m.field = 30
except ValidationError as e:
    print(e)

print()
print("Using as key value pair...")
class Model(BaseModel):
    model_config = ConfigDict(frozen=False)
    field: int

m =  Model(field=20)
try:
    d = {m:"Not gonna work!"}
except TypeError as e:
    print(e)

print()
print("Using as key value pair again...")
class Model(BaseModel):
    model_config = ConfigDict(frozen=True)
    field: int

m =  Model(field=20)
try:
    d = {m:" It's all good!"}
    print(d)
except ValidationError as e:
    print(e)