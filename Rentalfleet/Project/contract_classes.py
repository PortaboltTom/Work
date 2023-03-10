from datetime import datetime, timedelta
from dataclasses import dataclass, field
from typing import Type, List
from enum import Enum, auto
used_items = set()

@dataclass
class Contract:
    name: str
    items: List[Type] = field(default_factory=list)
    removed_items: List[Type] = field(default_factory=list)
    total_cost: float = 0.0
    start_date: datetime = field(default=None)
    
    def add_items(self, items: List[Type], start_date: datetime, end_date: datetime = None):
        added_items = []
        for item in items:
            if hasattr(item, "current_contract") and item.current_contract:
                print(f'{item.__class__.__name__} is already in contract {item.current_contract} and will not be added to this contract')
            else:
                item.current_contract = self.name
                self.items.append(item)
                self.total_cost += item.rental_price
                added_items.append(item)
                # Update start date if not already set
        if not self.start_date:
            self.start_date = start_date
        return added_items
        
    def remove_items(self, items: List[Type], end_dates: List[datetime] = None):
        removed_items = []
        for i, item in enumerate(items):
            if item not in self.items:
                print(f'{item.__class__.__name__} is not in contract')
            else:
                if end_dates and end_dates[i]:
                    item.end_date = end_dates[i]
                else:
                    item.end_date = datetime.now()
                duration = item.end_date - self.start_date
                item.previous_contracts.append((item.current_contract, duration))
                item.current_contract = None
                self.items.remove(item)
                self.total_cost -= item.rental_price
                self.removed_items.append(item)
                removed_items.append(item)
                print(f'removing {item.__class__.__name__} from contract')
        return removed_items
    
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

@dataclass
class InverterRack:
    build_date: str
    rental_price: float = 0.0
    power: int=0
    current_contract: Type[Contract] = None
    previous_contracts: List[Type[Contract]] = field(default_factory=list)

    def __hash__(self):
        return hash(self.build_date)

@dataclass
class BatteryRack:
    build_date: str
    rental_price: float = 0.0
    current_contract: Type[Contract] = None
    previous_contracts: List[Type[Contract]] = field(default_factory=list)

    def __hash__(self):
        return hash(self.build_date)

@dataclass
class Trailer:
    build_date: str
    rental_price: float = 0.0

    current_contract: Type[Contract] = None
    previous_contracts: List[Type[Contract]] = field(default_factory=list)

    def __hash__(self):
        return hash(self.build_date)


