from pydantic import BaseModel, ConfigDict, Field, ValidationError

class Model(BaseModel):

    id_: int = Field(alias="id")
    first_name: str = Field(alias="firstName")

try:
    Model(id_=1, first_name="Isaac")
except ValidationError as e:
    print(e)

print()
data = {
    "id_": 10,
    "first_name": "Isaac"
}
try:
    Model.model_validate(data)
except ValidationError as e:
    print(e)

print()
print("Adding populate_by_name function ...")
class Model(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    id_: int = Field(alias="id")
    first_name: str = Field(alias="firstName")

try:
    m1 = Model(id_=11, first_name="Jacov")
    print(m1)
    print(repr(m1))
except ValidationError as e:
    print(e)

print()
data = {
    "id_": 20,
    "first_name": "Jacov"
}
try:
    m2 = Model.model_validate(data)
    print(m2)
    print(repr(m2))
except ValidationError as e:
    print(e)

print()
print("Now we can use both, field name or alias ...")
print(Model(id_=2, first_name="Abrahm"))
print(Model(id=2, first_name="Abrahm"))
print(Model(id_=2, firstName="Abrahm"))
print(Model(id=2, firstName="Abrahm"))

print()
from pydantic.alias_generators import to_camel

class Person(BaseModel):
    model_config = ConfigDict(
        alias_generator=to_camel,
        populate_by_name=True,
        extra="forbid"
    )
    id_: int = Field(alias="id", default=1)
    first_name: str | None= None
    last_name: str
    age: int | None = None

p = Person(id_=2, first_name="Noah", last_name="God's Man", age=500)
print(p)
print()
json_data = '''
    {
        "id_": 2,
        "first_name": "Noah",
        "last_name":"God's Man",
        "age":500
    }
'''
print(Person.model_validate_json(json_data))
print(p.model_dump())
print(p.model_dump(by_alias=True))
