# Задайте последовательность чисел. 
# Напишите программу, которая выведет список 
# неповторяющихся элементов исходной последовательности.
list_1 = []
list_length = int(input('введите длину списка:'))
for i in range(list_length):
    temp = int(input('введите последовательность чисел: '))
    list_1.append(temp)
print(list_1)
list_2 = []

for i in list_1:
    if i in list_2:
        continue
    else:
        list_2.append(i)

print(list_2)            