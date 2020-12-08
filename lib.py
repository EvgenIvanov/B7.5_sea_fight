class Dot:
    # x = ''
    # y = ''
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __str__(self):
        # return (self.x, self.y)
        return '{} {}'.format(self.x, self.y)

class Ship:
    def __init__(self, Dot, rang = 1, orient = 'h'):
        self.dot = Dot
        self.rang = rang
        self.orient = orient

class Board:
    pass
