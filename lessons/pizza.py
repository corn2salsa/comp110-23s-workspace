"""Define pizza class"""

class Pizza:

    # attributes
    size: str # small or large
    toppings: int
    gluten_free: bool


    def __init__(self, size_input: str, top_input: int, gf_input: bool):
        self.size = size_input
        self.gluten_free = gf_input
        self.toppings = top_input
        #returns self

    def price(self) -> float:
        """Pizza price"""
        cost: float = 0.0
        if self.size == "large":
            cost = 6.0
        else: 
            cost = 5.0
        cost += .75 * self.toppings
        if self.gluten_free:
            cost += 1.0
        return cost
    
    def add_toppings(self, num_toppings: int):
        """Add toppings"""
        self.toppings += num_toppings
        
