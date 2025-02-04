from uuid import uuid4

print("Python UUID4")
print(uuid4())
print()

print("Pydantic UUID4")
from pydantic import UUID4, BaseModel, ValidationError, Field

class Person(BaseModel):
    id: UUID4

p = Person(id=uuid4())
print(p)

p2 = Person(id='2f55c357-b474-4f20-ad20-9367e53bfc7d')
print(p2)
print(p2.model_dump())
print(p2.model_dump_json())
print()

print("Using a default value")
class Person(BaseModel):
    id: UUID4 = uuid4()

p3 = Person()
print(p3)
p4 = Person()
print(p4)
print()


class Person(BaseModel):
    id_: UUID4 = Field(alias="id", default=uuid4())

p5 = Person()
print(p5)
p6 = Person()
print(p6)
print("Still have the same uuid for tow persons")
print()

print("Fixing, using default_factory function")
class Person(BaseModel):
    id_: UUID4 = Field(alias="id", default_factory=uuid4)

p7 = Person()
print(p7)
p8 = Person()
print(p8)