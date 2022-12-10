# 5'. Реализуйте алгоритм перемешивания списка.
from random import randint
mass = [1,3,5,6,8,0]
print(mass)

for i in range (len(mass)-1):
    n=randint(0, len(mass)-1)
    mass[i], mass[n] = mass[n], mass[i]
print(mass)