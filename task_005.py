# Даны два файла, в каждом из которых находится 
# запись многочлена. Задача - сформировать файл, 
# содержащий сумму многочленов.

path_1 = 'polynomial_1.txt'
data = open(path_1, 'r')
for line in data:
    polynomial_1=  line   # извлекаем первый из файла
path_2 = 'polynomial_2.txt'
data = open(path_2, 'r')
for line in data:
    polynomial_2= line   # извлекаем второй 
print(polynomial_1)       
print(polynomial_2) 

poly_sum = polynomial_1 
list_1 = [i for i in polynomial_1 if i.isdigit()]
list_2 = [i for i in polynomial_2 if i.isdigit()]
list_1.pop(1)
list_2.pop(1)
list_3 = []
for i in range(len(list_1)):
    list_3.append (int( list_1[i]) + int(list_2[i]))
print(f'{list_3[0]}*x^2 + {list_3[1]}*x + {list_3[2]} = {list_3[3]}')
