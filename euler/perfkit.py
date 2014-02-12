from time import clock
class WallClock():
    def __init__(self, time_func=clock):
        self.time_func=time_func
        self.created=self.time_func()
    def __call__(self):
        return round(float(self.time_func()-self.created),6)