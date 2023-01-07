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
        return added_items
        
    def remove_item(self, item: Type):
        if item not in self.items:
            raise ValueError('item is not in contract')
        item.current_contract = None
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

@dataclass
class InverterRack:
    build_date: str
    rental_price: float = 0.0
    power: int = 0
    current_contract: Type[Contract] = None

    def __hash__(self):
        return hash(self.build_date)

@dataclass
class BatteryRack:
    build_date: str
    rental_price: float = 0.0
    current_contract: Type[Contract] = None
    
    def __hash__(self):
        return hash(self.build_date)

@dataclass
class Trailer:
    build_date: str
    rental_price: float = 0.0
    current_contract: Type[Contract] = None

    def __hash__(self):
        return hash(self.build_date)


