# 2. Напишите программу для проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.
from operator import not_

num_x = int(input('Введите значение X: '))
num_y = int(input('Введите значение Y: '))
num_z = int(input('Введите значение Z: '))
print(not_(num_x or num_y or num_z) == (not_(num_x) and not_(num_y) and not_(num_z)))
