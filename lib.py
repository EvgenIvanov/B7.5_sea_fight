class Dot:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __str__(self):
        return self.__x, self.__y
        # return '{} {}'.format(self.x, self.y)

class Ship:
    def __init__(self, Dot, rang = 1, orient = 'h'):
        self.dot = Dot      # координаты носа корабля
        self.rang = rang
        self.orient = orient

    def getShip(self):
        # tDots = []
        if self.orient == 'h':
            return [(i, self.dot.y) for i in range(self.dot.x, self.dot.x + self.rang)]
            # for i in range(self.dot.x + self.rang):
            #     tDots.append((i, self.dot.y))
        else:
            return [(self.dot.x, i) for i in range(self.dot.y, self.dot.y + self.rang)]
        #     for i in range(self.dot.y + self.rang):
        #         tDots.append((self.dot.x, i))
        # return tDots

class Board():
    dots = set()
    def __init__(self, size):
        self.size = size
        self.deck = [[u'\u2022' for y in range(size)] for x in range(size)]
        # self.dots [(x,x) for x in range(size)]
        for x in range(6):
            for y in range(6):
                self.dots.add((x, y))

    @staticmethod
    def emptyDot(Dot):
        x, y = Dot[0], Dot[1]
        return [
            (x-1, y-1), (x, y-1), (x+1, y-1),
            (x-1, y), (x, y), (x+1, y),
            (x-1, y+1), (x, y+1), (x+1, y+1)
        ]
        # return tDots

    def __add(self, Dot, status):
        # if self.deck[Dot[1]][Dot[0]] == u'\u2022':
            # self.deck[Dot[1]][Dot[0]] = status
        if self.deck[Dot[1]][Dot[0]] == u'\u2022':
            self.deck[Dot[1]][Dot[0]] = status
            tDots = self.emptyDot(Dot)
            self.dots.difference_update(tDots)
            print('self.dots='+str(len(self.dots)))

    def addShip(self, Ship):
        ret = False
        sh = set(Ship.getShip())
        if sh.issubset(self.dots):
            for i in sh:
                self.__add(i,u'\u2589')
            ret = True
            self.dots.difference_update(sh) # удаление точек корабля из массива dots
        return ret
    
    def show(self, hide = 0):
        str_ = [str(i+1)+' ' for i in range(self.size)]
        print(f"   {''.join(str_)} " + 'X'+'×' + u'\u2573' + '¤'+u'\u2022\u25E6\u00B0\u03BF')
        for i,row in enumerate(self.deck):
            print(f' {chr(65+i)} ' + ' '.join(row)) #' ' + row + '\n')
        print()
        # bordersize = 6
        
        # '¤'
        # u'\u2573'
        # for x in range(bordersize):
        #     row = [u'\u2573' for y in range(bordersize)]
        #     # for y in range(bordersize):
        #     #     row.append(u'\u2573') #05') #91') #y+1)
        #     b.append(row)
        # print(self.deck)
        
        # отобразить символ по коду chr()
        # отобазить код по символу ord()

