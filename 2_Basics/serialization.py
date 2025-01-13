from pydantic import BaseModel, ValidationError

class Person(BaseModel):
    first_name:str
    last_name:str
    age:int

fabio = Person(first_name="Fabio",last_name="Classo",age=49)
galois = Person(first_name="Evariste",last_name="Galois",age=20)
newton = Person(first_name="Isaac",last_name="Newton",age=84)


print(newton.__dict__)
print(type(newton.__dict__))
print("=" * 100)
# serializing ...
print(galois.model_dump())
print(type(galois.model_dump()))
print("=" * 100)
# serializing  as json
print(fabio.model_dump_json())
print(type(fabio.model_dump_json()))
print("=" * 100)
# identention
print(fabio.model_dump_json(indent=2))
print("=" * 100)
# Modifying data
print(galois.model_dump(exclude=['first_name', 'age']))
print("=" * 100)
print(newton.model_dump(include=['last_name']))
print("=" * 100)
