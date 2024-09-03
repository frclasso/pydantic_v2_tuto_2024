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