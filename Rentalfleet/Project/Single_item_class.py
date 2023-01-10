from datetime import datetime, timedelta
from dataclasses import dataclass, field
from typing import Type, List
from enum import Enum, auto
used_items = set()

class ItemType(Enum):
    INVERTER_RACK = auto()
    BATTERY_RACK = auto()
    TRAILER = auto()
    CABLE = auto()

@dataclass
class Contract:
    name: str
    items: List[Type[ItemType]] = field(default_factory=list)
    removed_items: List[Type[ItemType]] = field(default_factory=list)
    total_cost: float = 0.0
    start_date: datetime = field(default=None)
    
    def add_items(self, items: List[Type[ItemType]], start_date: datetime, end_date: datetime = None):
        added_items = []
        for item in items:
            if hasattr(item, "current_contract") and item.current_contract:
                print(f'{item.__class__.__name__} is already in contract {item.current_contract} and will not be added to this contract')
            else:
                item.current_contract = self.name
                self.items.append(item)
                #self.total_cost += item.rental_price
                added_items.append(item)
        if not self.start_date:
            self.start_date = start_date
        return added_items
        
    def remove_items(self, items: List[Type[ItemType]], end_dates: List[datetime] = None):
        removed_items = []
        for i, item in enumerate(items):
            if item.__class__ not in self.items:
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
                self.removed_items.append(item)
                removed_items.append(item)
                print(f'removing {item.__class__.__name__} from contract')
        return removed_items
    
    def get_items(self):
        def list_items():
            return self.items
        return list_items
    
    def generate_invoice(self, period: int):
        invoice_total = 0.0
        for item in self.items:
            rental_period = period
            if item.end_date:
                rental_period = (item.end_date - item.start_date).days //7

@dataclass
class RentalItem:
    name: str
    #rental_price: float
    build_date : str
    current_contract: Type[Contract] = None
    previous_contracts: List[Type[Contract]] = field(default_factory=list)
    
    def __hash__(self):
        return hash(self.build_date)

    def __hash__(self):
        return hash(self.name)

@dataclass
class InverterRack(RentalItem):
    power: int = 0

@dataclass
class BatteryRack(RentalItem):
    pass

@dataclass
class Trailer(RentalItem):
    laadgewicht : int = 0 
    assen : int = 0 
    leeg_gewicht : int = 0
    
@dataclass
class Cable(RentalItem):
    length : int = 0 
    amperage : int = 0
