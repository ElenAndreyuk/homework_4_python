# Задана натуральная степень k. Сформировать случайным 
# образом список коэффициентов (значения от 0 до 100) 
# многочлена и записать в файл многочлен степени k.
# Пример:
# - k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0
from random import random
k = int(input('введите k: '))
a = ''
while k > 0:
    temp = round(random()*100)
    a = a + str(temp)+'*x^'+ str(k) + '+ '
    k -=1
temp = round(random()*100)
a= a + str(temp)+' = 0'
print(a)    
data = open('file.txt', 'w')
data.write(a)
data.close()