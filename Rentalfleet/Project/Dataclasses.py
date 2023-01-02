from dataclasses import dataclass, field
from typing import Type

used_items = set()

@dataclass
class InverterRack:
    build_date: str

    def __hash__(self):
        return hash(self.build_date)

@dataclass
class BatteryRack:
    build_date: str

    def __hash__(self):
        return hash(self.build_date)

@dataclass
class Trailer:
    build_date: str

    def __hash__(self):
        return hash(self.build_date)

@dataclass
class Contract:
    items: list = field(default_factory=list)
    
    def add_item(self, item: Type):
        if item in used_items:
            raise ValueError('item has already been used')
        used_items.add(item)
        self.items.append(item)

inverter_rack = InverterRack(build_date='2022-01-01')
battery_rack = BatteryRack(build_date='2022-01-02')
trailer = Trailer(build_date='2022-01-03')
contract = Contract()


contract.add_item(inverter_rack)
contract.add_item(battery_rack)
contract.add_item(trailer)

print(contract.items)  # Output: [InverterRack(build_date='2022-01-01'), BatteryRack(build_date='2022-01-02'), Trailer(build_date='2022-01-03')]

try:
    contract.add_item(inverter_rack)
except ValueError as e:
    print(e)  # Output: item has already been used
