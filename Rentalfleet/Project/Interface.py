from dataclasses import dataclass
@dataclass
class Food:
    name: str
    carbs_percent: int
    fiber_percent: int
    
    @property
    def net_carbs(self):
        return self.carbs_percent + self.fiber_percent
    
Food('apple', 40, 5).net_carbs
dir()
print(Food)
