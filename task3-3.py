# 3'. Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.

# *Пример:*

# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19 (максимальное значение у числа 1.2 , минимальное у 10.01)


def func1(num: float) ->float:
    list_num=str(num).split('.')
    return float('0'+list_num[1])

def func2(num_list: list[float]) -> float:
    new_list=[func1(i) for i in num_list if int(i) != float(i)]
    print(new_list)
    return max(new_list) - min(new_list)

example = [1.1, 1.2, 3.1, 5, 10.01]

print(func2(example))