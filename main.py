from lib import *

# print(Dot(1, 1))
# d = Dot(1, 1)
# print(d)
 
sh = Ship(Dot(0,0),3,'w')
b = Board(6)
b.show()
# print(b.pointStatus.star)
# b.deck[5][5] = 'X'
# b.add(Dot(5, 5),'X')
# b.add(Dot(4, 4),'X')
print(b.addShip(sh))
b.show()
sh = Ship(Dot(0,3))
print(b.addShip(sh))
b.show()
# print(sh.getShip())
# shP = set(sh.getShip()) #(1,'a'))
# print(shP)
# t1 = [(1,1),(2,1),(3,1),
#       (1,2),(2,2),(3,2)]
# # print(sh.getShip().insubset(t1))
# set_ = set(t1)
# set_1 = tuple(Dot(1,1))
# if shP.issubset(set_): #set_.intersection(sh.getShip()):
#     print('YY')
# else:
#     print('NN')
# print(str(Dot(1,1)) in t1)
# ii, rang = 2,3
# for i in range(ii,ii+rang):
#     print(i)

# # s1 = [(2,i) for i in range(ii,ii+rang)]
# d = []
# for x in range(6):
#     for y in range(6):
#         d.append(Dot(x, y))
# s = 1

# print(b[3][1])
# print(s1)
# bordersize = 6
# b = []
# for x in range(bordersize):
#     row = []
#     for y in range(bordersize):
#         row.append(u'\u2505') #91') #y+1)
#     b.append(row)

# print(b)