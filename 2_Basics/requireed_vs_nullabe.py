from pydantic import BaseModel, ValidationError

print("case 1 = Required and Not Nullable )" +"=" * 30)
class Mode(BaseModel):
    field: int

try:
    Mode(field=None)
except ValidationError as e:
    print(e)

print()
print("case 2 Required and Nullable )" + "=" * 30)
class Mode2(BaseModel):
    field: int | None

try:
    Mode2()
except ValidationError as e:
    print(e)

print()
print("case 3 Option  and Not Nullable )" + "=" * 30)
class Mode3(BaseModel):
    field: int = 0 # default value

try:
    # Mode3(field=None) # Error
    Mode3()
except ValidationError as e:
    print(e)

print()
print("case 4 Option  and Nullable )" + "=" * 30)
class Mode4(BaseModel):
    field: int | None = None

try:
    # Mode4()
    # Mode4(field=None)
    # Mode4(field=1)
    Mode4(field="Python")
except ValidationError as e:
    print(e)