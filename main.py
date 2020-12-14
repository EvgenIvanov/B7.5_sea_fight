from lib import *

g = Game(6)
g.start()

# a ='f'
# print(type(a))
# xx = int(input())a1
# 1 1/A1/1A
# regexp ([1-9]|[1][0])[A-Fa-f]|

# while True:
#     try:
#         str_ = input('=>')
#         if not fullmatch(r'([1-9]|[1][0])[A-Fa-f]|[A-Fa-f]([1][0]|[1-9])', str_):
#             raise ValueError
#         str_ = str_.upper()
#         if ord(str_[0]) > 64:
#             y = ord(str_[0]) - 65
#             x = int(str_[1:]) - 1
#         else:
#             y = ord(str_[-1]) - 65
#             x = int(str_[0:-1]) - 1
#     except ValueError:
#         print(f'value must be: [1..{size}][A..{(chr(65 + size - 1))}a..{(chr(97 + size - 1))}]\nor [A..{(chr(65 + size - 1))}a..{(chr(97 + size - 1))}][1..{size}]')
#     else:
#         break
# print(str_)
# print('x='+str(x),'y='+str(y))
# while True:
#     try:

#         x, y = map(int, input('=>').split())
#         # x = int(x)
#         if x < 0 or x > size-1 or y < 0 or y > size-1:
#             raise ValueError
#     except ValueError:
#         if isinstance(x, str):
#             x = x.lower()
#             try:
#                 if len(x) != 1 or not (0 <= (ord(x) - 97) <= size - 1):
#                     raise ValueError
#                 x = ord(x) - 97
#             except ValueError:
#                 print(f'x and y must be: [0..{size-1}], int() or [A..{(chr(65 + size - 1))}a..{(chr(97 + size - 1))}]')
#             else:
#                 # print('ord=' + str(ord(x)))
#                 break
#         else:
#             print(f'x and y must be: [0..{size-1}], int() or [A..{(chr(65 + size - 1))}a..{(chr(97 + size - 1))}]')
#     else:
#         # print('x=' + str(x))
#         break
# print('x='+str(x))
# g = Game(6)
# g.start()6
# print(Dot(1, 1))
# d = Dot(1, 1)
# print(d)
 
# a = Board()5 
# b = Board()
# b.show(a,b)

# sh = Ship(Dot(0,0),3,'w')
# print

# b.addShip(Ship(Dot(0,0),3,'w'))
# b.show()
# sh = Ship(Dot(2,4))
# # print(b.addShip(sh))
# b.addShip(sh)
# b.show()
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