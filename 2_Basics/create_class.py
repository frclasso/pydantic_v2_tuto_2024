# creating pydantic model

from pydantic import BaseModel

class Person(BaseModel):
    first_name:str
    last_name:str
    age:int


p = Person(first_name="Fabio",last_name="Classo",age=49)
       

print(p)
print()
print(repr(p))
print()
print(p.model_fields)

from pydantic import ValidationError

try:
    Person(last_name="Edggie")
except ValidationError as e:
    print(e)

print()
class Person2(BaseModel):
    first_name:str
    last_name:str
    age:int

    @property
    def displayName(self):
        return f"{self.first_name} {self.last_name}"


p2 = Person2(first_name="Fabio",last_name="Classo",age=49)
print(p2.displayName)
print(p2.age)
p2.age = 48
print(p2)

p2 = Person2(first_name="Fabio",last_name="Classo",age=49)
try:
    Person2(first_name="Fabio",last_name="Classo",age="Fourthy Nine")
except ValidationError as e :
    print(e)

print()
p.age = 20
print(p)
p.age = "Twenty"
print(p)