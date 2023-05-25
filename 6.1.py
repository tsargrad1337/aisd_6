# Дан одномерный массив.
# Сформировать все возможные варианты данного массива
# путем замены положительных элементов на четных местах на нули.
import itertools
from random import randint
n = 10
array = [0]*n
for i in range(n):
    array[i] = randint(-100, 100)

# Функция-генератор, которая возвращает все возможные варианты массива, заменяя положительные числа на четных позициях на нули
def array_variants(arr):
    indices = [i for i in range(1, len(arr), 2) if arr[i] > 0]

    for i in range(len(indices) + 1):
        for combination in itertools.combinations(indices, i):
            for index in combination:
                x = arr[index]
                arr[index] = 0
                
            yield arr[:]  # yield генерирует каждый вариант по очереди
            for index in combination:
                arr[index] = x  # возвращаем массив к исходному состоянию

# Получаем все возможные варианты
variants = array_variants(array)

# Выводим варианты
for variant in variants:
    print(variant)
