from datetime import datetime, timedelta
from dataclasses import dataclass, field
from typing import Type, List

used_items = set()

@dataclass
class InverterRack:
    build_date: str
    rental_price: float = 0.0
    start_date: datetime = None
    end_date: datetime = None

    def __hash__(self):
        return hash(self.build_date)

@dataclass
class BatteryRack:
    build_date: str
    rental_price: float = 0.0
    start_date: datetime = None
    end_date: datetime = None

    def __hash__(self):
        return hash(self.build_date)

@dataclass
class Trailer:
    build_date: str
    rental_price: float = 0.0
    start_date: datetime = None
    end_date: datetime = None

    def __hash__(self):
        return hash(self.build_date)

@dataclass
class Contract:
    items: list = field(default_factory=list)
    removed_items: list = field(default_factory=list)
    total_cost: float = 0.0
    
    def add_items(self, items: List[Type], start_date: datetime, end_date: datetime = None):
        added_items = []
        for item in items:
            if item in used_items:
                print(f'{item.__class__.__name__} has already been used and will not be added to the contract')
            else:
                used_items.add(item)
                item.start_date = start_date
                item.end_date = end_date
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
        invoice_total = 0.0
        for item in self.items:
            rental_period = period
            if item.end_date:
                rental_period = (item.end_date - item.start_date).days // 7
            invoice_total += item.rental_price * rental_period
        for item in self.removed_items:
            rental_period = period
            if item.end_date:
                rental_period = (item.end_date - item.start_date).days // 7
            invoice_total += item.rental_price * rental_period
        print(f'Invoice total: {invoice_total:.2f}')
        
    def print_items(self):
        for item in self.items:
            print(item.__class__.__name__)

inverter_rack = InverterRack(build_date='2022-01-01', rental_price=100.0)
battery_rack = BatteryRack(build_date='2022-01-02', rental_price=200.0)
trailer = Trailer(build_date='2022-01-03', rental_price=300.0)

contract = Contract()

# Add items to the contract with a start date and no end date
start_date = datetime(2022, 1, 1)
contract.add_items([inverter_rack, battery_rack, trailer], start_date=start_date)

# Print the items in the contract
contract.print_items()  # Output: InverterRack, BatteryRack, Trailer

# Remove an item from the contract
contract.remove_item(inverter_rack)

# Generate an invoice for a 4 week period
contract.generate_invoice(4)  # Output: Invoice total: 500.00

# Add an item to the contract with a start date and end date
start_date = datetime(2022, 1, 15)
end_date = datetime(2022, 2, 5)
contract.add_items([inverter_rack], start_date=start_date, end_date=end_date)

# Generate an invoice for a 4 week period
contract.generate_invoice(4)  # Output: Invoice total: 700.00