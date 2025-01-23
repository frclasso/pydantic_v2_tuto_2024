from pydantic import BaseModel, field_serializer
from datetime import datetime

# About
"""
    when_used: by default the custom serializer is always used, but we have some options available:
        always: the default , serializer is executed when serializing either to dict or to json
        unless-none: serializer  is not used if the value is None
        json: serializer  is only used when serializing JSON
        json-unless-none: serializer used when serializing  to JSON,  unless  the value is None
"""

class Model(BaseModel):

    dt: datetime | None = None

    @field_serializer("dt", when_used="always")
    def serializer_name(self, value):
        print(f"type={type(value)}")
        return value
    
m = Model(dt="2020-01-01T12:00:00")
print(m)
print(m.model_dump())
print(m.model_dump_json())
m1 = Model(dt = None)
print(m1)
print(m1.model_dump())
print(m1.model_dump_json())

print()
print("Changing to when_used=unless-none ....")
class Model(BaseModel):

    dt: datetime | None = None

    @field_serializer("dt", when_used="unless-none")
    def serializer_name(self, value):
        print(f"type={type(value)}")
        return value
    
m3 = Model(dt="2020-01-01T12:00:00")
print(m3)
print(m3.model_dump())
print(m3.model_dump_json())
print()

print("Formating the timestamp field ...")
dt  = datetime(2020, 1, 1, 12, 0,0)
print(dt)
print(dt.isoformat())
print(f"string format: {dt.strftime("%Y/%-m/%-d %I:%M %p")}")
print()

print("Using json-unless-none ...")
class Model(BaseModel):

    dt: datetime | None = None

    @field_serializer("dt", when_used="json-unless-none")
    def serializer_name(self, value):
        print(f"type={type(value)}")
        return value.strftime("%Y/%-m/%-d %I:%M %p") #formating string method
    
m4 = Model(dt="2020-01-01T12:00:00")
print(m4)
print(m4.model_dump())
print()
print(m4.model_dump_json())

print()
m5 = Model(dt=None)
print(m5)
print(m5.model_dump())
print(m5.model_dump_json())
print()

print("Adding serialize info ...")
from pydantic import FieldSerializationInfo
class Model(BaseModel):

    dt: datetime | None = None

    @field_serializer("dt", when_used="unless-none")
    def serializer_name(self, value, info: FieldSerializationInfo):
        print(f"type={type(value)}")
        return value
    
m6 = Model(dt=datetime(2020,1,1))
print(m6)
print()
print(m6.model_dump())
print()
print(m6.model_dump_json())

print()
print("Check witch method are in use: dict or json...")
from pydantic import FieldSerializationInfo
class Model(BaseModel):

    dt: datetime | None = None

    @field_serializer("dt", when_used="unless-none")
    def serializer_name(self, value, info: FieldSerializationInfo):
        print(f"type={type(value)}")
        print(f"is json={info.mode_is_json()}")
        return value
    
m7 = Model(dt=datetime(2020,1,1))
print(m7.model_dump())
print()
print(m7.model_dump_json())

print()
print("Formating timezone ...")
import pytz

dt =datetime.now(pytz.utc)
print(dt)
print(dt.isoformat())
print()

def make_utc(dt: datetime) -> datetime:
    if dt.tzinfo is None:
        dt = pytz.utc.localize(dt)
    else:
        dt = dt.astimezone(pytz.utc)
    return dt

dt1 = make_utc(datetime.now())
print(dt1)
print()

dt2 = make_utc(datetime.now(pytz.utc))
print(dt2)
print()
print(dt1.strftime("%Y-%m-%dT%H:%M:%SZ"))

def dt_utc_json_serializer(dt:datetime) -> str:
    dt = make_utc(dt)
    return dt.strftime("%Y-%m-%dT%H:%M:%SZ")

print()
print("Put all together ....")
class Model(BaseModel):

    dt: datetime | None = None

    @field_serializer("dt", when_used="unless-none")
    def serializer_name(self, dt, info: FieldSerializationInfo):
        if info.mode_is_json():
            return dt_utc_json_serializer(dt)
        return make_utc(dt)
    
m8 = Model(dt=datetime(2020, 1, 1))
print(m8)
print(m8.model_dump())
print(m8.model_dump_json())

print()
print("Location as a parameter ...")
eastern = pytz.timezone("US/Eastern")
dt = eastern.localize(datetime(2025, 1, 23))
print(dt)
m9 = Model(dt=dt)
print(m9)
print(m9.model_dump()) # return UTC not US/Eastern
print(m9.model_dump_json()) # return UTC not US/Eastern