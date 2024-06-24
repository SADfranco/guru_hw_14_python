import dataclasses


@dataclasses.dataclass
class Region:
    region_url: str
    region_name: str


@dataclasses.dataclass
class RegionsAll:
    region_size: int
    region_all_names: list
