from pydantic import BaseModel, ConfigDict, ValidationError

class Model(BaseModel):

    model_config = ConfigDict(str_strip_whitespace=True)
    field: str

m1 = Model(field="    python")
m2 = Model(field="python\t   \n")

print(m1)
print(m2)
print(f"Checking: {m1 == m2}")

print()
print("Using lower case coercing...")
class Model(BaseModel):

    model_config = ConfigDict(str_strip_whitespace=True, str_to_lower=True)
    field: str

m3 = Model(field="    PYTHON\t\n")
print(m3)

print()
print("Using upper case coercing...")
class Model(BaseModel):

    model_config = ConfigDict(str_strip_whitespace=True, str_to_upper=True)
    field: str

m4 = Model(field="    Python\t\n")
print(m4)