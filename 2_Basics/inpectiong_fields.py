from pydantic import BaseModel, ValidationError

class Circle(BaseModel):
    center_x: int = 0
    center_y: int = 0 
    radius: int = 1
    name: str | None = None

for k, v in Circle.model_fields.items():
    print(k, ":", v)
print()
c1 = Circle(radius=2)
c2 = Circle(name="Unit circle")
print(f"c1: {c1}")
print(c1.model_dump())
print(type(c1.model_dump()))
print(c1.model_fields_set)
print(c1.model_fields.keys())
print("Getting the default fields...")
print(c1.model_fields.keys() - c1.model_fields_set)
print()
print("C2")
print(f"c2: {c2}")
print(c2.model_fields_set)


print()
print("Other things...")
class Model(BaseModel):
    field_1: int = 0 # required=False default=0
    field_2: int | None = None # required=False default=None
    field_3: str # required=True
    field_4: str | None = "Python"  # required=False default='Python'

for k, v in Model.model_fields.items():
    print(k, ":", v)
print()
m1 = Model(field_3='m1')
m2 = Model(field_1=1, field_2=None,field_3='m2', field_4="Python")
m3 = Model(field_1=10, field_2=20,field_3='m3', field_4="Pydantic")

print(m1.model_dump())
print(m1.model_fields_set) # {'field_3'} ==> required=True
print(m1.model_dump(include=m1.model_fields_set))
