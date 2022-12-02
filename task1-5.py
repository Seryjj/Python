# 5'. Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.

# *Пример:*

# - A (3,6); B (2,1) -> 5,09
# - A (7,-5); B (1,-1) -> 7,21


import math



x_coordinate_A = float(input('Введите координату точки А по оси Х: '))
y_coordinate_A = float(input('Введите координату точки А по оси Y: '))
x_coordinate_B = float(input('Введите координату точки B по оси Х: '))
y_coordinate_B = float(input('Введите координату точки B по оси Y: '))

distance = math.sqrt((x_coordinate_B - x_coordinate_A)**2 + (y_coordinate_B - y_coordinate_A)**2)
print (distance)