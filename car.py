class Car:
    wheels="4 wheels"
    def __init__(self,make,model,color):
        self.make=make
        self.model=model
        self.color=color
    def start_car(self):
        return f"vroom vroom"
    def car_capacity(self):
        return f'my {self.color} car can carry 5 passengers'
    def car_speed(self):
        return f'my {self.make}, with {self.wheels} has a speed of 246km/h'
    