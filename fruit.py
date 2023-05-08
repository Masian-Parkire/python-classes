class Fruit:
    nutrients="Vitamin-c"
    def __init__(self,name,color,taste):
        self.name=name
        self.color=color
        self.taste=taste
    def fruit_price(self):
        return f"{self.name} are expensive because it has alot of {self.nutrients}"
    def describe_fruit(self):
        return f"a {self.name} is {self.taste} and it has {self.nutrients}"
    def fruit_expiry_date(self):
        return f"{self.name} has a {self.taste} because it has expired."
        