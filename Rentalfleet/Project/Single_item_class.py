from datetime import datetime, timedelta
from dataclasses import dataclass, field
from typing import List, TypeVar, Type

RentalItemType = TypeVar('RentalItemType', bound='RentalItem')

@dataclass
class Contract:
    name: str
    items: List[RentalItemType] = field(default_factory=list)
    removed_items: List[RentalItemType] = field(default_factory=list)
    total_cost: float = 0.0
    start_date: datetime = field(default=None)

    def add_items(self, items: List[RentalItemType], start_date: datetime, end_date: datetime = None):
        added_items = []
        for item in items:
            if hasattr(item, "current_contract") and item.current_contract:
                print(f'{item.name} is already in contract {item.current_contract} and will not be added to this contract')
            else:
                item.current_contract = self.name
                self.items.append(item)
                added_items.append(item)
        if not self.start_date:
            self.start_date = start_date
        return added_items

    def remove_item(self, item: RentalItemType, end_date: datetime = None):
        if item not in self.items:
            print(f'{item.name} is not in contract')
        else:
            if end_date:
                item.end_date = end_date
            else:
                item.end_date = datetime.now()
            item.current_contract = None
            self.items.remove(item)
            self.removed_items.append(item)
            print(f'removing {item.name} from contract')
        
    def remove_multiple_items(self, items: List[RentalItemType], end_dates: List[datetime] = None):
        removed_items = []
        for item in items:
            self.remove_item(item)
        return removed_items

    def get_items(self):
        def list_items():
            return self.items
        return list_items

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