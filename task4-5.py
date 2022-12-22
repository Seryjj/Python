# 5'. Даны два файла, в каждом из которых находится запись многочлена. Задача - сформировать файл, содержащий сумму многочленов.
# В file1.txt :
# 2*x**2 + 4*x + 5
# В file2.txt:
# 4*x**2 + 1*x + 4
# Результирующий файл:
# 6*x**2 + 5*x + 9


import sympy

x=sympy.Symbol('x')

with open('file1.txt', 'w', encoding='utf-8') as file:
    file.write('2*x**2 + 4*x + 5')
with open('file2.txt', 'w', encoding='utf-8') as file:
    file.write('4*x**2 + 1*x + 4')

with open('file1.txt','r') as file:
    l = file.read()


with open('file2.txt','r') as file:
    y = file.read()

print(l)
print(y)

m=sympy.simplify(l +'+' +y)

print(m)


with open('sum_poly.txt', 'w', encoding='utf-8') as file:
    file.write(m)