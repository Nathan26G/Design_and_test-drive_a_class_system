from datetime import datetime 

class Tyre():

    def __init__(self, position):
        self.tyre = {'position': position, 'pressure': 0, 
            'tread_depth': 0, 'date':str(datetime.now().date())}
        # parameters: none
        # output: none
        # side-effect: creates an empty dictionary
        pass
    
    def record_pressure(self, pressure):
        self.tyre['pressure'] = pressure

        # parameters: the pressure, an an intiger
        # output: none
        # side-effect: adds tyre pressure to the tyre dict
        pass
    
    def record_tread_depth(self, tread_depth):
        self.tyre['tread_depth'] = tread_depth
        # parameters: the tread depth, an an intiger
        # output: none
        # side-effect: adds tyre tread depth to the tyre dict
        pass


left_tyre = Tyre('left_front')
print(left_tyre.tyre)
left_tyre.record_pressure(100) 
left_tyre.record_tread_depth(25) 
print(left_tyre.tyre)