# Вычислить число c заданной точностью d
# Пример:
# - при $d = 0.001, π = 3.141.$    $10^{-1} ≤ d ≤10^{-10}$
import math
from decimal import Decimal
n = Decimal(input('задайте точность округления числа пи (например 0.001): '))
num = Decimal(math.pi)
print (num.quantize(Decimal(n)))