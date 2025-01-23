from pydantic import BaseModel, ConfigDict, ValidationError, Field


class Model(BaseModel):
    id_: int = Field(alias="id")
    last_name: str = Field(alias="lastName")

json_data = '''
    {
        "id":100,
        "lastName":"Gauss"

    }
'''

m = Model.model_validate_json(json_data)
print(m)
print()
print("We need to user the aliases on the new instances also...")
print(Model(id=200, lastName="Math")) # right
print()
print("If we try to use the name instead...")
try:
    print(Model(id_=200, last_name="Math")) # wrong
except ValidationError as e:
    print(e)

print()
print("To access the fields by using Pyhton, we use the name...")
print(m.id_)
print(m.last_name)
print(hasattr(m, "last_name")) # True
print(hasattr(m, "lastName")) # False
print()

print("Adding default values...")
class Model2(BaseModel):
    id_: int = Field(alias="id", default=100)
    last_name: str = Field(alias="lastName")

m2 = Model2(lastName="USDCoin")
print(m2)
print()
print("Serializing...")
print(m2.model_dump()) # Uses the field name
print(m2.model_dump_json())

print()
print("Getting by alias ...")
class Person(BaseModel):
    id_: int = Field(alias="id")
    first_name: str | None = Field(alias="firstName", default=None)
    last_name: str = Field(alias="lastName")
    age: int | None = None

isaac = Person(id=1, firstName="Isaac", lastName="Newton", age=84)
print(isaac)
print(isaac.model_dump())
print("using by alias")
print(isaac.model_dump(by_alias=True))
print(isaac.model_dump_json(by_alias=True))

print()
print(Person.model_fields)