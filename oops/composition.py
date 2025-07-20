#composition = The composed object directly owns its components, which cannot exist independently "owns-a" relationship

class Engine:
    def __init__(self,horse_power):
        self.horse_power=horse_power

class Wheel:
    def __init__(self,size):
        self.size=size

#engine and wheel is composition here since car owns it
class Car:
    def __init__(self,maker,model,horse_power,wheel_size):
        self.maker=maker
        self.model=model
        self.engine=Engine(horse_power) #Composition
        self.wheel=[Wheel(wheel_size) for _ in range(4)] #Composition
        
    def display_car_details(self):
        print(f"maker :{self.maker}, model: {self.model}, engine:{self.engine.horse_power} (hp), wheel:{self.wheel[0].size}")
        
car1=Car("Tata","Altroz",500,18)
car2=Car("Mahindra","Thar",670,19)
car1.display_car_details()
car2.display_car_details()

