from pydantic import BaseModel, ValidationError, ConfigDict
from datetime import date
import json

class Automobile(BaseModel):
    """Original"""
    manufacter:str
    series_name:str
    type_:str
    is_eletronic:bool
    manufacter_date:date
    base_msrp_usd:float
    vin:str
    number_of_doors:int = 4
    registration_country: str | None = None
    license_plate: str | None = None



"""
    Modify your Automobile model to implement the following:
        set model to forbid extra fields
        set the model to strip whitespaces from all string fields
        set the model to validate defaults and assignments
        use the enum provided bellow for the type_ field
"""

from enum import Enum

class AutomobileType(Enum):
    sedan = 'Sedan'
    coupe = 'Coupe'
    convertible = "Convertible"
    suv = "SUV"
    truck = "Truck"

data_json = '''
{
    "manufacter":" BMW ",
    "series_name":" M4 ",
    "type_": "Convertible",
    "manufacter_date":"2023-01-01",
    "base_msrp_usd":933300,
    "vin":"1234567890"
}
'''
class Automobile(BaseModel):
    """Refactored"""
    model_config = ConfigDict(
                                extra="forbid", 
                                str_strip_whitespace=True,
                                validate_default=True, 
                                validate_assignment=True
                                )
    
    manufacter:str
    series_name:str
    type_: AutomobileType
    is_eletronic:bool = False
    manufacter_date:date
    base_msrp_usd:float
    vin:str
    number_of_doors:int = 4
    registration_country: str | None = None
    license_plate: str | None = None

car = Automobile.model_validate_json(data_json)
# for i in car:
#     print(i)


##output
data_json_expected_serialization = '''
{
    "manufacter":"BMW",
    "series_name":"M4",
    "type_": <AutomobileType.convertible: 'Convertible'>,
    "is_eletronic": "False",
    "manufacter_date": "date(2023,01,01)",
    "base_msrp_usd": 933300.0,
    "vin":"1234567890",
    "number_of_doors":4,
    "registration_country": null,
    "license_plate": null
}
'''
other = '{"manufacter":"BMW","series_name":"M4","type_": "AutomobileType.convertible","is_eletronic": "False","manufacter_date": "2023,01,01","base_msrp_usd":933300.0,"vin":"1234567890","number_of_doors":4,"registration_country": null,"license_plate": null}'
# Make comparison
print(car.model_dump())
print()
print(data_json_expected_serialization)
# assert car.model_dump_json() == data_json_expected_serialization
# print()
# print(type(data_json_expected_serialization))
# print(data_json_expected_serialization)

# for k, v in json.loads(data_json_expected_serialization).items():
#     print(k, v)


# print()
