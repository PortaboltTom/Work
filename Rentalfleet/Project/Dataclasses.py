from dataclasses import dataclass, field
from typing import Type

used_items = set()

@dataclass
class InverterRack:
    build_date: str
    rental_price: float = 0.0
    power: int = None

    def __post_init__(self):
        if self.power is None:
            raise ValueError("Power must be set.")
@dataclass
class BatteryRack:
    build_date: str
    rental_price: float = 0.0

    def __hash__(self):
        return hash(self.build_date)

@dataclass
class Trailer:
    build_date: str
    rental_price: float = 0.0

    def __hash__(self):
        return hash(self.build_date)

@dataclass
class Contract:
    items: list = field(default_factory=list)
    removed_items: list = field(default_factory=list)
    total_cost: float = 0.0
    
    def add_item(self, items: list):
        added_items = []
        for item in items:
            if item in used_items:
                print(f'{item.__class__.__name__} has already been used and will not be added to the contract')
            else:
                used_items.add(item)
                self.items.append(item)
                self.total_cost += item.rental_price
                added_items.append(item)
        return added_items
        
    def remove_item(self, item: Type):
        if item not in self.items:
            raise ValueError('item is not in contract')
        used_items.remove(item)
        self.items.remove(item)
        self.total_cost -= item.rental_price
        self.removed_items.append(item)
        print(f'removing {item.__class__.__name__} from contract')
        
    def generate_invoice(self, period: int):
        invoice_total = self.total_cost * period
        for item in self.removed_items:
            invoice_total += item.rental_price * period
        print(f'Invoice total: {invoice_total:.2f}')
    
    def print_items(self):
        for item in self.items:
            print(item.__class__.__name__)

inverter_rack = InverterRack(build_date='2022-01-01', rental_price=100.0)
battery_rack = BatteryRack(build_date='2022-01-02', rental_price=200.0)
trailer = Trailer(build_date='2022-01-03', rental_price=300.0)

contract = Contract()
contract.add_item([inverter_rack, battery_rack, trailer, trailer])
contract.remove_item(trailer)
contract.print_items()

'''
contract.add_item(battery_rack)
contract.add_item(trailer)

contract.generate_invoice(4)  # Output: Invoice total: 1200.00


inverter_rack = InverterRack(build_date='2022-01-01', rental_price = 60)
battery_rack = BatteryRack(build_date='2022-01-02', rental_price = 20)
trailer = Trailer(build_date='2022-01-03', rental_price = 40)
contract = Contract()


contract.add_item(inverter_rack)
contract.add_item(battery_rack)
contract.add_item(trailer)
contract.remove_item(inverter_rack)

print(contract.items)  # Output: [InverterRack(build_date='2022-01-01'), BatteryRack(build_date='2022-01-02'), Trailer(build_date='2022-01-03')]

try:
    contract.add_item(inverter_rack)
except ValueError as e:
    print(e)  # Output: item has already been used
'''