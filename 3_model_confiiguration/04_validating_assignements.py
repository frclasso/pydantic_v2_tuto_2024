from pydantic import BaseModel, ConfigDict, ValidationError

class Model(BaseModel):
    """Without validation"""
    field: int

m  = Model(field=10)
m.field = "Python"
print(m)

print()
print("Validating assigments...")

class Model(BaseModel):
    """With validation assigments"""
    model_config = ConfigDict(validate_assignment=True) # default is False
    field: int

m  = Model(field=10)
try:
    m.field = "Python"
except ValidationError as e:
    print(e)