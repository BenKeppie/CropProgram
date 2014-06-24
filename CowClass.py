from AnimalClass import *

class Cow(Animal):
    """A representation of a sheep"""
    def __init__(self):
        super().__init__(1,5,5)
        self._type="Cow"

    def grow(self,food,water):
        if water>=self._water_need and food>= self._food_need:
            if self._status=="Baby" and water>self._water_need:
                self._growth += self._growth_rate*1.5
            elif self._status=="Young" and water > self._water_need:
                self._growth += self._growth_rate*1.25
            else:
                self._growth += self._growth_rate
        self._days_growing +=1
        self._update_status()
                


if __name__=="__main__":
    cow=Cow()
    

