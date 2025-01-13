from pydantic import BaseModel
from typing import Deque, List, Optional, Tuple
from datetime import date

class Automobile(BaseModel):
    manufacter: str 
    series_name: str
    type_: str
    is_eletric: bool = False
    manufactored_date: date
    base_msrp_usd: float
    vln: str
    number_of_doors: int = 4
    registration_country: str | None = None
    license_plate: str | None = None

for k,v in Automobile.model_fields.items():
    print(k, v)


auto = {
    "manufacter": "BMW", 
    "series_name": "M4",
    "type_": "Convertible",
    "is_eletric": False,
    "manufactored_date": "2023-01-01",
    "base_msrp_usd": 93_300,
    "vln": "1234567890",
    "number_of_doors": 2,
    "registration_country": "Brasil",
    "license_plate": "AAA-2024"
}

auto_json = '''{
    "manufacter": "BMW", 
    "series_name": "M4",
    "type_": "Convertible",
    "is_eletric": "False",
    "manufactored_date": "2023-01-01",
    "base_msrp_usd": "93_300",
    "vln": "1234567890",
    "number_of_doors": "2",
    "registration_country": "Brasil",
    "license_plate": "AAA-2024"
}
'''

auto_expected_serialization = {
    "manufacter": "BMW",
    "series_name": "M4",
    "type_": "Convertible",
    "is_eletric": False,
    "manufactored_date": date(2023,1,1),
    "base_msrp_usd": 93_300,
    "vln": "1234567890",
    "number_of_doors": 2,
    "registration_country": "Brasil",
    "license_plate": "AAA-2024"
}

auto_json_expected_serialization = {
    "manufacter": "BMW", 
    "series_name": "M4",
    "type_": "Convertible",
    "is_eletric": False,
    "manufactored_date": date(2023,1,1),
    "base_msrp_usd": 93_300,
    "vln": "1234567890",
    "number_of_doors": 2,
    "registration_country": "Brasil",
    "license_plate": "AAA-2024"
}

print()
car = Automobile.model_validate(auto)
print(car)
print()
try:
    assert car.model_dump() == auto_expected_serialization
    print("Equal")
except AssertionError as e:
    print(e)
print()
print("Validation JSON")
print(Automobile.model_validate_json(auto_json))
print()
try:
    assert car.model_dump() == auto_json_expected_serialization
    print("Equal")
except AssertionError as e:
    print(e)