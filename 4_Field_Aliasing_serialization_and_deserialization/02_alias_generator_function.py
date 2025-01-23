from pydantic import BaseModel, ConfigDict, ValidationError,Field
from pydantic.alias_generators import to_camel, to_pascal, to_snake

print(to_camel("last_name"))
print(to_snake("lastName"))
print(to_pascal("last_name"))

print()
def make_upper(in_str: str) -> str:
    return in_str.upper()


class Person(BaseModel):
    model_config = ConfigDict(alias_generator=make_upper)

    id_: int
    first_name: str | None = None
    last_name: str
    age: int | None = None

print(Person.model_fields)
print()
fabio = Person(ID_=1,  LAST_NAME="Classo", AGE=50)
print(fabio)
print(fabio.model_dump())
print(fabio.model_dump(by_alias=True))
print()

print("Overwriting configs ...")
class Person(BaseModel):
    model_config = ConfigDict(alias_generator=make_upper)

    id_: int = Field(alias="ID")
    first_name: str | None = None
    last_name: str
    age: int | None = None

p2 = Person(ID=2, LAST_NAME="Reis", AGE=50)
print(p2.model_dump(by_alias=True))
print(p2.model_dump_json(by_alias=True))

print()
print("Using pydantic functions ...")
class Person(BaseModel):
    model_config = ConfigDict(alias_generator=to_camel)

    id_: int = Field(alias="id")
    first_name: str | None = None
    last_name: str
    age: int | None = None

print(Person.model_fields)
print()
gigi = Person(id=3, firstName="Giovanna", lastName="Classo", age=12)
print(gigi)
print(gigi.model_dump())
print(gigi.model_dump(by_alias=True))
print(gigi.model_dump_json(by_alias=True))

print()
print("Using a custom function ...")
class Model(BaseModel):
    model_config = ConfigDict(alias_generator=to_camel)

    id_: int = Field(alias="id")
    list_: list[str] = Field(alias="list")
    filter_: dict = Field(alias="filter")
    number_elements: list[int]

print(Model.model_fields)
print()
def make_alias(field_name: str) -> str:
    alias = to_camel(field_name)
    return alias.removesuffix("_")

print(make_alias("log_"))
print(make_alias("number_elements_"))
print()

class ModelCustom(BaseModel):
    model_config = ConfigDict(alias_generator=make_alias)  # using the custom function

    id_: int
    list_: list[str] 
    filter_: dict 
    number_elements: list[int]

print(ModelCustom.model_fields)