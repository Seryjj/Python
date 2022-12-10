# 1'. Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.

# *Пример:*

# - 6782 -> 23
# - 0,56 -> 11



# a = input('Введите число')
# sum1=0
# for i in range(len(a)):
#     if(i!=','):
#      sum1 = sum1 + int(a[i:i+1])
# print(sum1)




a = float(input('Введите число '))
sum1=0
for i in str(a):
    if(i!='.' and i!='-'):
     sum1 = sum1 + int(i)
print(sum1)

