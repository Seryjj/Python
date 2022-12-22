# 4'. Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена 
# и записать в файл многочлен степени k.(записать в строку)

# Пример:

# k=2 => 2*x^2 + 4*x + 5 или x^2 + 5 или 10*x**2
# k=3 => 2*x^3 + 4*x^2 + 4*x + 5



import random


a=[]

def write_file(st):
    with open('file33.txt', 'w') as data:
        data.write(''.join(st))

def rnd():
    return random.randint(0,101)


def create_mn(k):
    lst = [rnd() for i in range(k+1)]
    return lst
    



def create_str(num_list: list[int]):
    for i in range(0,len(num_list)):
        a.append(f'{num_list[i]}*x**{i}')
        a.append(' + ')
    
    return a


k = int(input("Введите натуральную степень k = "))
koef = create_mn(k)
create_str(koef)
a.pop(-1)
write_file(a)



