from pydantic import BaseModel, ConfigDict, ValidationError

class Model(BaseModel):

    field : str

try:
    Model(field=10)
except ValidationError as e:
    print(e)

print()
print("Coercing to string...")
class Model(BaseModel):
    model_config = ConfigDict(coerce_numbers_to_str=True) # works with float, int and decimal
    field : str

print(Model(field=1.5))
print(Model(field='1.5'))

from decimal import Decimal

d = Decimal("10.5")
print(Model(field=d))

print()
print("Using strict mode ...")
class Model(BaseModel):
    model_config = ConfigDict(coerce_numbers_to_str=True, strict=True)  # strict mode doesn't work
    field : str
try:
    Model(field=100)
except ValidationError as e:
    print(e)