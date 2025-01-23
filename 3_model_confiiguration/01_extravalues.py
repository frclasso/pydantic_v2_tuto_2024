from pydantic import BaseModel, ValidationError, ConfigDict

class Model(BaseModel):
    filed_1: int


m = Model(filed_1=10, filed_2=20)
print(m.model_fields)
print(dict(m))
print(type(m.model_extra))
print()

print("Extra ignore...")
class Model2(BaseModel):
    model_config = ConfigDict(extra="ignore")
    filed_1: int

m2 = Model2(filed_1=10, filed_2=20)
print(m2.model_fields)
print(dict(m2))
print(m2.__dict__)
print(m2.model_extra)
print(type(m2.model_extra))
print()

print("Extra forbid...")
class Model3(BaseModel):
    model_config = ConfigDict(extra="forbid")
    filed_1: int
try:
    Model3(filed_1=10, filed_2=20)
except ValidationError as e:
    print(e)

print()
print("Extra allow...")
class Model4(BaseModel):
    model_config = ConfigDict(extra="allow")
    filed_1: int

m4 = Model4(filed_1=10, filed_2=20)
print(m4.model_fields)
print(dict(m4))
print(m4.model_fields_set)
print(m4.model_extra)
print(Model4.model_config)
