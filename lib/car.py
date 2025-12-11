from datetime import datetime 
from tyre import *

class Car():
    def __init__(self):
        self.my_tyres = []
        # parameters: none
        # output: none
        # side-effect: creates an empty list

    def add_tyres(self, tyre):
        self.my_tyres.append(tyre)
        # parameters: tyre
        # output: none
        # side-effect: adds tyre to list 

'''
rachels_car = Car()
left_tyre = Tyre('left_front')
# print(left_tyre.tyre)
left_tyre.record_pressure(100) 
left_tyre.record_tread_depth(25) 
right_tyre = Tyre('right_front')
# print(left_tyre.tyres)
right_tyre.record_pressure(200) 
right_tyre.record_tread_depth(50) 
# print(left_tyre.tyres)
rachels_car.add_tyres(left_tyre)
rachels_car.add_tyres(right_tyre)
today = str(datetime.now().date())
for tyre in rachels_car.my_tyres:
    print(rachels_car.my_tyres[rachels_car.my_tyres.index(tyre)].tyre)
'''


