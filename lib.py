from random import randint

class Dot:
    ## фактическая точка игрового поля 
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    # def __str__(self):
    #     return self.__x, self.__y

class Ship:
    def __init__(self, Dot, rang = 1, orient = False):
        self.dot = Dot          # координаты носа корабля
        self.rang = rang        # ранг корабля (кол-во палуб)
        if not orient:
            self.orient = False    # ориентация корабля на доске (h/w)
        else:
            self.orient = True


    def getShip(self):          # по параметрам корабля возвращает набор его точек горизонтально расположенных или вертикально
        if not self.orient: #self.orient == 'h':
            return [(i, self.dot.y) for i in range(self.dot.x, self.dot.x + self.rang)]
        else:
            return [(self.dot.x, i) for i in range(self.dot.y, self.dot.y + self.rang)]

class Board():
    def __init__(self, size = 6):
        self.size = size                                                                # размерность игрового поля
        self.deck = [[u'\u2022' for y in range(size)] for x in range(size)]             # точки на доске
        self.dots = set([(x, y) for y in range(self.size) for x in range(self.size)])   # точки плоскости доски для определения возможности парковки корабля
        if size == 6:
            self.ships = [3,2,2,1,1,1,1]
            attempt = 2000
        elif size == 10:
            self.ships = [4,3,3,2,2,2,1,1,1,1]
            attempt = 5000
        tAtt = 0
        for rang in self.ships:
            while True:
                park = self.addShip(Ship(Dot(randint(0, size), randint(0, size)), rang, randint(0,1)))
                tAtt += 1
                if park or tAtt > attempt:
                    break
            if tAtt > attempt:
                print('Exit loop. Ship parking ship is bad.')
                break

    @staticmethod
    def emptyDots(Dot):
        ## набор точек, окружающих переданную точку
        #  для вычитания из self.dots точек корабля и точек контура корабля
        x, y = Dot[0], Dot[1]
        return [
            (x-1, y-1), (x, y-1), (x+1, y-1),
            (x-1, y), (x, y), (x+1, y),
            (x-1, y+1), (x, y+1), (x+1, y+1)
        ]

    def __add(self, Dot, status):
        ## добавление точки корабля на доску 
        # и вычитание из списка self.dots точки и её контура
        if self.deck[Dot[1]][Dot[0]] == u'\u2022':
            self.deck[Dot[1]][Dot[0]] = status
            tDots = self.emptyDots(Dot)
            self.dots.difference_update(tDots)
            # print('self.dots='+str(len(self.dots)))

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

