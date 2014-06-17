from CropClass import *

class Potato(Crop):
    """A representation of a potato crop"""
    def __init__(self):
        super().__init__(1,3,6)
        self._type="Potato"


    def grow(self,light,water):
        if water>=self._water_need and light>= self._light_need:
            if self._status=="Seedling" and water>self._water_need:
                self._growth += self._growth_rate*1.5
            elif self._status=="Young" and water > self._water_need:
                self._growth += self._growth_rate*1.25
            else:
                self._growth += self._growth_rate
        self._days_growing +=1
        self._update_status()
                


if __name__=="__main__":
    potato_crop=Potato()
    

