from random import randint

class Dot:
    ## фактическая точка игрового поля 
    x = None
    y = None
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __str__(self):
        return self.x, self.y


class Ship:
    def __init__(self, dot, rang = 1, orient = False):
        self.dot = dot          # координаты носа корабля
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
                            self.ships.append(ship.getShip())
                        break
                if tAtt > attempt:
                    print('Exit loop. Ship parking is bad.')
                    break

    @staticmethod
    def emptyDots(dot):
        ## набор точек, окружающих переданную точку
        #  для вычитания из self.dots точек корабля и точек контура корабля
        x, y = dot.x, dot.y
        return [
            (x-1, y-1), (x, y-1), (x+1, y-1),
            (x-1, y), (x, y), (x+1, y),
            (x-1, y+1), (x, y+1), (x+1, y+1)
        ]

    def add(self, dot, status):
        ## добавление точки корабля на доску 
        # и вычитание из списка self.dots точки и её контура        
        if self.deck[dot.y][dot.x] == u'\u2022':
            self.deck[dot.y][dot.x] = status        
            tDots = self.emptyDots(dot)
            self.dots.difference_update(tDots)
        elif self.deck[dot.y][dot.x] == u'\u2589':
            self.deck[dot.y][dot.x] = status

            # print('self.dots='+str(len(self.dots)))

    def addShip(self, Ship):
        ret = False
        sh = set(Ship.getShip())
        if sh.issubset(self.dots):
            for i in sh:
                self.add(Dot(*i), u'\u2589')
            ret = True
            self.dots.difference_update(sh) # удаление точек корабля из массива dots
        return ret
    
    @staticmethod
    def show(own, ali):
        print('\n Opponent board          Your board  ')
        print('   ----------             --------------')
        str_ = [str(i+1)+' ' for i in range(own.size)]
        print(f"   {''.join(str_)}             {''.join(str_)}" + 'X'+'×' + u'\u2573' + '¤'+u'\u2022\u25E6\u00B0\u03BF')
        for i,row in enumerate(own.deck):
            aliRow = ali.deck[i]
            print(f' {chr(65+i)} ' + ' '.join(row).replace(u'\u2589',u'\u2022') + f'            {chr(65+i)} ' + ' '.join(aliRow)) #.replace(u'\u2589',u'\u2022')) #' ' + row + '\n')
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


class Player():
    def __init__(self, size):
        self.size = size
        self.board = Board(size)

    def shot(self):
        return map(int, input('Введите кординаты выстрела: ').split(' '))

    def shoot(self):
        # делаю выстрел
        # проверяю board.deck
        # если u'\u2022' - сказать "мимо", вернуть переход_хода
        # если '¤' или 'X' - сказать "уже стрелял", вернуть переход_хода 
        # если u'\u2589', то нужно проверить в board.ships:
        # вычесть из точек корабля, проверить оставшееся кол-во точек этого корабля
        # если точек не осталось, удалить объект корабля, сказать "убит", проверить на конец игры вернуть переход_хода
        # если точки еще остались, то сказать "ранен" вернуть переход_хода
        # shot_ = self.shot()
        dot = Dot(*self.shot())
        point = self.board.deck[dot.y][dot.x]
        if point == '•': #u'\2020':
            self.board.add(Dot(dot.x, dot.y), '¤')
            print(f'Dot{dot.x, dot.y} shot past')
            return False
        elif point == '¤' or point == 'X':
            print(f'Dot{dot.x, dot.y} alrady shot')
            return False
        elif point == '▉': #u'\2589':
            for ship in self.board.ships:
                if (dot.x, dot.y) in ship:
                    self.board.add(Dot(dot.x, dot.y), 'X')
                    ship.remove((dot.x, dot.y))
                    if not len(ship):
                        self.board.ships.remove(ship)
                        print(f'Dot{dot.x, dot.y} ship killed')
                    else:
                        print(f'Dot{dot.x, dot.y} ship wounded')
                    break
            return True

class AI(Player):
    def shot(self):
        return randint(0, self.size - 1), randint(0, self.size - 1)

class Game():
    def __init__(self, size = 6):
        self.size = size

    def start(self):
        print('  welcome to  ')
        print('  sea battle  ')
        print('     game     ')
        print('\nparking ship')
        us = Player(self.size)
        ai = AI(self.size)
        us.board.show(us.board, ai.board)
        step = 0
        while True:
            # print('gameOver')            
            while True:
                # print('move')
                if not step % 2:
                    move = us.shoot()
                    us.board.show(us.board, ai.board)
                if step % 2 == 1:
                    move = ai.shoot()
                if not move:    # если выстрел возвращает False
                    break       # то переход хода
                                # ранение и потопление корабля разрешают повторный ход
                elif not len(us.board.ships) or not len(ai.board.ships):
                    break
            if not len(us.board.ships) or not len(ai.board.ships):
                if not step % 2:
                    print('Congratulations, player 1 won')
                else:
                    print('Congratulations, player 2 won')
                print('Game over')
                break
            step +=1
            if not step % 2:
                us.board.show(us.board, ai.board)
        # us.board.show(us.board, ai.board)
        # us.board.show(ai.board, us.board)
        # print(ai.shoot())
        # us.board.show(ai.board, us.board)
        # print(ai.shoot())
        # us.board.show(ai.board, us.board)
        # us.board.show(us.board, ai.board)
        print('end')
        # ai = AI(size)
    