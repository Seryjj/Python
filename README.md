# Python



Долполнительные материалы с занятий

Ольга Авдонина: n = int(input())
for i in range (n-1):
print((-3) ** i, end = ',')
print((-3) ** (i+1))


Ольга Авдонина: slov = {}
n = int(input())
for i in range (1,n + 1):
slov[i] = 3 * i + 1
print(slov)


Ольга Авдонина: str1 = input()
str2 = input()
count1 = str1.count(str2)
print(count1)

Vladislav Isaev: a = input()
b = input()
count = 0
for i in range(len(a)):
if a[i:i+len(b)] == b:
count += 1
print(count)
print(a.count(b))


Vladislav Isaev: a = input()
b = input()
count = 0
for i in range(len(a)):
if a[i:i+len(b)] == b:
count += 1
print(count)
print(a.count(b))


Vladislav Isaev: with open('file.txt','r') as f:
a = f.read().split('\n')
print(a)