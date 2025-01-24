from datetime import date
from enum import Enum
from pydantic import BaseModel,ConfigDict

class AutomobileType(Enum):
    sedan = "Sedan"
    coupe = "Coupe"
    convertible = "Convertible"
    suv = "SUV"
    truck = "Truck"

# template
# class Automobile(BaseModel):
#     model_config = ConfigDict(
#         extra="forbid",
#         str_strip_whitespace=True,
#         validate_default=True,
#         validate_assignment=True
#     )
#     manufacture: str
#     series_name: str
#     type_: AutomobileType
#     is_eletric: bool = False
#     manufacture_date: date
#     base_msrp_usd: float
#     vin: str
#     number_of_doors: int = 4
#     registration_country: str | None = None
#     license_plate: str | None = None

    # Rules to be implemented
    """
        Modify the Automobile model to implement the following:
        1- auto generate camel case aliases
        2- the field type_ in the model is provided type in source data, and 
        should also serialized to type.
        3- the data we received contains the following fields names that need to map
        to our model field names - butwe still want our camelized filed names
        to be used for serialization.
        4- Account for that (without renaming the field names):
            - number_of_doors is provided doors
            - manufacture_date is providaded completionDate
        5- The field base_msrp_usd is provided as msrpUSD, and we want the serialization
        name to be baseMSRPUSD.
        6- we want the JSON serialized output of manufacture_date to be this pattern:
        YYYY/MM/DD, but serializing to Python dict should remain as a date object.
    """

# The following source data:
data_json ='''
    {
        "manufacturer": "BMW",
        "seriesName": "M4",
        "type": "Convertible",
        "isEletric": false,
        "completionDate":"2023-01-01",
        "msprUSD": 93000,
        "vin": "1234567890",
        "doors": 2,
        "registrationCountry": "USA",
        "licensePlate": "AAA-BBB"
    }
'''



# RESOLUTION =======================================
from pydantic import Field, field_serializer
from pydantic.alias_generators import to_camel

class Automobile(BaseModel):
    # alias_generators=to_camel - answer 1
    model_config = ConfigDict(
        extra="forbid",
        str_strip_whitespace=True,
        validate_default=True,
        validate_assignment=True,
        alias_generators=to_camel, 
    )

    manufacturer: str
    series_name: str 
    type_: AutomobileType = Field(alias="type") #answer 2
    is_eletric: bool = False
    manufactured_date: date = Field(validation_alias="completionDate") #answer 4
    base_msrp_usd: float = Field(
        validation_alias="msprUSD",
        serialization_alias="baseMSPRUSD"
    ) #answer 5
    vin: str
    number_of_doors: int = Field(default=4,validation_alias="doors") #answer 3
    registration_country: str | None = None
    license_plate: str | None = None

    #answer 6
    @field_serializer("manufactured_date", when_used="json-unless-none")
    def serialize_date(self, value: date) -> str:
        return value.strftime("%Y/%m/%d")
    
car = Automobile.model_validate_json(data_json)
print(car)