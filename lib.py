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
        self.ships = []
        self.deck = []
        self.size = size                                                                # размерность игрового поля
        self.dots = []
        if size == 6:
            self.shipsRang = [3,2,2,1,1,1,1]
            attempt = 2000
        elif size == 10:
            self.shipsRang = [4,3,3,2,2,2,1,1,1,1]
            attempt = 5000
        while len(self.ships) != len(self.shipsRang):
            self.ships.clear()
            self.dots.clear()
            self.deck.clear()
            self.dots = set([(x, y) for y in range(self.size) for x in range(self.size)])   # точки плоскости доски для определения возможности парковки корабля
            self.deck = [[u'\u2022' for y in range(size)] for x in range(size)]             # точки на доске
            for rang in self.shipsRang:
                tAtt = 0
                while True:
                    ship = Ship(Dot(randint(0, size), randint(0, size)), rang, randint(0,1))
                    park = self.addShip(ship)
                    tAtt += 1
                    if park or tAtt > attempt:
                        if park:
                            self.ships.append(ship)
                        break
                if tAtt > attempt:
                    print('Exit loop. Ship parking is bad.')
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
    
    @staticmethod
    def show(own, ali):
        print('\n   Your board             Opponent board')
        print('   ----------             --------------')
        str_ = [str(i+1)+' ' for i in range(own.size)]
        print(f"   {''.join(str_)}             {''.join(str_)}") #" + 'X'+'×' + u'\u2573' + '¤'+u'\u2022\u25E6\u00B0\u03BF')
        for i,row in enumerate(own.deck):
            aliRow = ali.deck[i]
            print(f' {chr(65+i)} ' + ' '.join(row) + f'            {chr(65+i)} ' + ' '.join(aliRow)) #.replace(u'\u2589',u'\u2022')) #' ' + row + '\n')
            # print(row)
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

