# Ограничение: максимальная сумма элементов массива не должна превышать некоторое число.
# Целевая функция: вывести массив с максимальной  суммой элементов , не превышая данное ограничение.

import itertools
import copy
from random import randint
n = 10
array = [0]*n
for i in range(n):
    array[i] = randint(-10, 10)
def array_variants(array, max_sum):
    if max_sum < sum(x for x in array if x < 0):
        raise ValueError("Максимальная сумма не может быть меньше суммы положительных элементов")

    variants = []
    indices = [i for i in range(1, len(array), 2) if array[i] > 0]

    for i in range(len(indices) + 1):
        for combination in itertools.combinations(indices, i):
            variant = copy.deepcopy(array)
            for index in combination:
                variant[index] = 0
            print(f"Полученный вариант: {variant}, сумма элементов: {sum(variant)}")  # выводим каждый вариант перед проверкой
            # Проверка на соответствие максимальной сумме
            if sum(variant) <= max_sum:
                variants.append(variant)

    # Находим вариант с максимальной суммой элементов
    best_variant = max(variants[::-1], key = sum)
    return best_variant

max_sum = 10

# Получаем лучший вариант, удовлетворяющий ограничению
best_variant = array_variants(array, max_sum)

# Выводим лучший вариант
print(best_variant)
