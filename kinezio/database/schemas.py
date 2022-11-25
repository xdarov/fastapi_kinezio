from pydantic import BaseModel, validator, Field
from datetime import date

class BodyPartsSchem(BaseModel):
    parts_name: str
    parent_id: None | int


class CharacterPainSchem(BaseModel):
    vname: str


class ClientSchem(BaseModel):
    first_name: str
    second_name: str
    surname: str
    phone: str
    birthdate: date


class CuppingFactorsSchem(BaseModel):
    vname: str


class FrequencyOfPainSchem(BaseModel):
    vname: str


class ProvokingFactorsSchem(BaseModel):
    vname: str
