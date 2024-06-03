class Player:
    def __init__(self):
        self.sens = 0.35
    def setSens(self, new_sens):
        self.sens = new_sens
    def getSens(self):
        return self.sens