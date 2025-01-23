from pydantic import BaseModel, ConfigDict, Field, ValidationError

class Model(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    first_name: str = Field(validation_alias="FirstName")

m = Model(FirstName="Isaac")
print(m) # first_name='Isaac'
print(Model(first_name="Isaac")) #first_name='Isaac'
data = {"FirstName":"Isaac"}
m = Model.model_validate(data)
print(m.model_dump()) # same result, validation_alias only used for deserializing
print(m.model_dump(by_alias=True)) # first_name='Isaac'
print()

print("Using alias ...")
class Model(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    first_name: str = Field(validation_alias="FirstName", alias="firstName")

m = Model(FirstName="Isaac")
print(m.model_dump(by_alias=True))

print()
print("Using all options...")
class Model(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    first_name: str = Field(validation_alias="FirstName", 
                              alias="firstName",# We can choose between this options
                              serialization_alias="givenName")

m = Model(FirstName="Isaac")
data = {"FirstName":"Isaac"}
m = Model.model_validate(data)
print(m)
print(m.model_dump(by_alias=True))
print()

print()
print("Using alias generator")
from pydantic.alias_generators import to_camel
class Model(BaseModel):
    model_config = ConfigDict(populate_by_name=True, alias_generator=to_camel)

    first_name: str 
    last_name: str

data = {
    "first_name": "Isaac",
    "last_name": "Newton"
}

m = Model.model_validate(data)
print(m)
print(Model.model_fields)
print()

class Model(BaseModel):
    model_config = ConfigDict(populate_by_name=True, alias_generator=to_camel)

    first_name: str = Field(
        validation_alias="FirstName",
        serialization_alias="givenName" # Overwrites the alias
    )
    last_name: str

m = Model.model_validate(data)
print(m)
print(m.model_dump(by_alias=True))
print()

print("Using AliasChoices...")
from pydantic import AliasChoices
class Model(BaseModel):
    model_config = ConfigDict(populate_by_name=True, alias_generator=to_camel)

    first_name: str = Field(
        validation_alias=AliasChoices("FirstName", "GivenName"),
        serialization_alias="givenName" # Overwrites the alias
    )
    last_name: str

data = {
    "first_name": "Isaac",
    "last_name": "Newton"
}
m = Model.model_validate(data) #first_name
print(m)
print(m.model_dump(by_alias=True)) # givenName

data = {
    "GivenName": "Isaac",
    "last_name": "Newton"
}
m = Model.model_validate(data) #first_name
print(m)
print(m.model_dump(by_alias=True)) # givenName

print()
print("An example using database config settings...")
data = {
    "databases":{
        "redis":{
                "name":"Local Redis",
                "redis_conn":"redis://secret@localhost:9000/1"
            },
        "psql":{
            "name":"Local postgres",
            "pgsql_conn":"postgresql://user:secret@localhost"
        },
        "nosql":{
            "name":"Local MongoDB",
            "mongo_conn":"mongodb://USERNAME:PASSWORD@HOST/DATABASE"
        }
    }
}

class Database(BaseModel):
    name: str
    connection: str = Field(validation_alias=AliasChoices("redis_conn",  "pgsql_conn", "mongo_conn"))

databases = {}

for key, value in data["databases"].items():
    m = Database.model_validate(value)
    databases[key] = m

for k, v in databases.items():
    print(k, v)

print()
print("Nested model...")
class DatabasesNested(BaseModel):
    databases: dict[str, Database]

databasesNested = DatabasesNested.model_validate(data)
print(databasesNested)
print()
print(databasesNested.model_dump_json(indent=2))