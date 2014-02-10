from time import clock
class WallClock():
    def __init__(self):
        self.created=clock()
    def show(self):
        return round(clock()-self.created,3)