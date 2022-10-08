# Задайте натуральное число N. Напишите программу, 
# которая составит список простых множителей числа N.
n = int(input('введите число: '))
# list_n = list(filter(lambda i: not n%i, (i for i in range(2, n))))
list_n = []
for i in range(2, n-1):
    if not n%i:
        list_n.append(i)
        while not n%i:
           n = n/i
print(list_n)        
