import dataclasses


@dataclasses.dataclass
class User:
    first_name: str
    last_name: str
    email: str
    password: str
    gender: str
    bd_year: str
    bd_month: str
    bd_day: str


@dataclasses.dataclass
class ExistingUser:
    first_name: str
    last_name: str
    email: str
    password: str
    phone_number: str
    bday_data: str


@dataclasses.dataclass
class NonExistingUser:
    first_name: str
    email: str
    password: str
