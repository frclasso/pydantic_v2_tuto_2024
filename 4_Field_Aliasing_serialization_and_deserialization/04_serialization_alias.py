from pydantic import BaseModel, ConfigDict, ValidationError, Field

response_json = '''
    {
        "ID":100,
        "FirstName":"Isaac",
        "lastname":"Newton"
    }
'''

class Person(BaseModel):
    id_: int = Field(alias="ID")
    first_name: str = Field(alias="FirstName")
    last_name: str = Field(alias="lastname")

p = Person.model_validate_json(response_json)
print(p)
print(p.model_dump())
print(p.model_dump(by_alias=True))

print()
print("Overwirting the serialization method ...")
class Person(BaseModel):
    id_: int = Field(alias="ID", serialization_alias="id")
    first_name: str = Field(alias="FirstName", serialization_alias="firstName")
    last_name: str = Field(alias="lastname", serialization_alias="lastName")

p2 = Person.model_validate_json(response_json)
print(f'__P2:\n', p2)
print(p2.model_dump())
print(p2.model_dump(by_alias=True))
print(Person.model_fields)