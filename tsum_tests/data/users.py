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
class Existing_user:
    first_name: str
    last_name: str
    email: str
    password: str
    phone_number: str
    bday_data: str

@dataclasses.dataclass
class Nonexisting_user:
    first_name: str
    email: str
    password: str