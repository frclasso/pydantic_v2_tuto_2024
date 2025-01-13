from pydantic import BaseModel, ValidationError

class Person(BaseModel):
    first_name:str
    last_name:str
    age:int

p = Person(first_name="Fabio",last_name="Classo",age=49)

data = {
    "first_name":"Isaac",
    "last_name":"Newton",
    "age": 84
}
print("=" * 100)
p2 = Person(**data)
print(p2)
print("=" * 100)
p3 = Person.model_validate(data)
print(p3)
print("=" * 100)
missing_data = {"last_name":"Newton"}
try:
    Person.model_validate(missing_data)
except ValidationError as e:
    print(e)
print("=" * 100)

# Manipulate a JSON string
data2 = '''{
            "first_name":"Isaac",
            "last_name":"Newton",
            "age": 84
        }'''

p4 = Person.model_validate_json(data2)
print(p4)
print("=" * 100)
missing_data2 = '''{"last_name":"Newton"}'''
try:
    Person.model_validate_json(missing_data2)
except ValidationError as e:
    print(e)
print("=" * 100)

print("=" * 100)
class Coodiantes(BaseModel):
    x:float
    y:float

p1 = Coodiantes(x=1.0, y=2.0)
print(type(p1.x))
print(type(p1.y))
print("Coercion ===================")
p2 = Coodiantes(x=1, y="2.1")
print(type(p2.x), p2.x)
print(type(p2.y), p2.y)

print("JSON validation ===================")
class Model(BaseModel):
    field:str

print(Model(field="Python"))
print()
try:
    Model(field=1000)
except ValidationError as e:
    print(e)
print()

class Contact(BaseModel):
    email:str

initial_json_data = """
    {
        "email":"frclasso@email.com"
        }
"""
print(Contact.model_validate_json(initial_json_data))
new_data_json = """
    {
        "email": {
            "work":"fabio.classo@nttdata.com",
            "personal":"frclasso@email.com"

        }
    }
"""
print("new_data_json validation ===================")
print()
try:
    Contact.model_validate_json(new_data_json)
except ValidationError as e:
    print(e)

print("New data as Dict")
new_data = {
        "email": {
            "work":"fabio.classo@nttdata.com",
            "personal":"frclasso@email.com"

        }
    }
print(Contact(email=str(new_data["email"])))