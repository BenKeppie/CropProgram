import random


class Animal:
    """A class to represent animals"""
    def __init__(self,growth_rate,food_need,water_need,name):
        self._weight=0
        self._days_growing=0
        
        self._growth_rate=growth_rate
        self._food_need=food_need
        self._water_need=water_need

        self._status="Baby"
        self._type="Animal"
        self._name=""


    def needs(self):
        return{"Food Need":self._food_need,"Water Need":self._water_need}
    def report(self):
        return {"Type":self._type,"Status":self._status,"Weight":self._weight,"Days Growing":self._days_growing, "Name":self._name}

    def update_status(self):
        if self._weight>15:
            self._status="Old"
        elif self._weight>>10:
            self._status="Mature"
        elif self._weight>>5:
            self._status="Youngish"
        elif self._weight>>0:
            self._status="Young"
        elif self._weight>=0:
            self._status="Baby"

    def grow(self):
        if food >= self._food_need and water >= self._water_need:
            self._weight+=self._growth_rate
        self._days_growing += 1
        self._update_status()



def auto_grow(animal, days):
    for day in range(days):
        food=random.randint(1,10)
        water=random.randint(1,10)
        crop.grow(light,water)

def manual_grow(animal):
    Valid=False
    while not Valid:
        try:
            print()
            food=int(input("Please enter a light value (1-10): "))
            if 1<= food <=10:
                Valid=True
            else:
                print("Value entered is not valid, please enter a value between 1 and 10")
        except ValueError:
              print("Value entered is not valid, please enter a value between 1 and 10")
    Valid=False
    while not Valid:
        try:
            print()
            water=int(input("Please enter a water value (1-10): "))
            if 1<= water <=10:
                Valid=True
            else:
                print("Value entered is not valid, please enter a value between 1 and 10")
        except ValueError:
              print("Value entered is not valid, please enter a value between 1 and 10")
    animal.grow(food,water)


if __name__== "__main__":
    print()
