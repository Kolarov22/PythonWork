# Ex1
# def fibo():
#     limit = int(input("Input: \n"))
#     prev = 0
#     curr = 1
#     next = curr
#     for i in range(limit-1):
#         if(i == 0):
#             print(0)
#             print(1)
#         else:
#             print(next)
#             prev, curr = curr, next
#             next = prev+curr
# fibo()

# Ex2
# def gcd(a, b):
#     if a == 0:
#         return b
#
#     return gcd(b % a, a)
# print(gcd(36, 48))

# Ex3
# def lcm(a, b):
#     greater = max(a, b)
#     smallest = min(a, b)
#     for i in range(greater, a*b+1, greater):
#         if i % smallest == 0:
#             return i
#
# print(lcm(3,5))

# Ex4
# def oddEvenSort(list):
#     odd = []
#     even = []
#     for el in list:
#         if(el % 2 == 0):
#             even.append(el)
#         else:
#             odd.append(el)
#     return even, odd
# toBeSorted = [1, 4, 6, 2, 21, 13, 18, 22]
# print(oddEvenSort(toBeSorted))

# Ex5
# class Cube:
#     def __init__(self, edge):
#         self.edge = edge
#
#     def oneFaceArea(self):
#         return self.edge**2
#     def totalArea(self):
#         return 6*self.oneFaceArea()
#     def volume(self):
#         return self.edge**3
#
# Obj1 = Cube(3)
# print(Obj1.oneFaceArea(),
# Obj1.totalArea(),
# Obj1.volume())

#Ex6

# pow = lambda a,b : a**b
# print(pow(5,3))

