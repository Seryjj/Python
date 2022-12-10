# 4'. Задайте список из N элементов, заполненных числами из промежутка [-N, N]. 
# Найдите произведение элементов на указанных позициях. Позиции хранятся в файле file.txt в одной строке одно число.
# (для продвинутых - с файлом, вариант минимум - ввести позиции в консоли)
# -2 -1 0 1 2
# Позиции: 0,1 -> 2


# N=int(input('Введите число N '))
# a=[]
# for i in range(2*N+1):
#     a.append(-N+i)
# print(a)

# sum=0

# with open('file.txt','r') as f:
#     b = f.read().split('\n')
# print(b)

# x=int(b)

# for i in x:
#     sum=a[i]+sum
# print(sum)




# for line in a:





N = int(input('Введите число'))
numbers = []
for i in range(2*N+1):
     numbers.append(-N+i)
print(numbers)



f = open('file.txt', 'w')
while True:
    s = input('Укажите позицию для вычисления - ')
    if s == "":
        break
    f.write(s+"\n")
f.close()

result = 1
f = open('file.txt', 'r')
for line in f:
    if line == "":
        break
    result *= numbers[int(line)]
f.close()
print(result)