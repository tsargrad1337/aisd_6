'''
Вариант 20.  Дан одномерный массив. Сформировать все возможные варианты данного массива путем замены положительных элементов на четных местах на нули.
Условие: Существует разделение на четные и нечетные цифры. Массив должен состоять из 4 элементов, и в нем должно быть от 4 до 6 различх цифр.
Целевая функция: найти максимальную сумму всех элементов массива
'''

chet = ['2', '4', '6', '8', '0']
nechet = ['1', '3', '5', '7', '9']
value = {'1': 1, '2': 2,'3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '0': 0}

print('Выберете тип цифр')
while True:
    choice = input('Введите 1, если хотите выбрать четные цифры, 2 - нечетные ')
    if choice == '1' or choice == '2':
        break

if choice == '1':
    n = int(input('\nВведите количество используемых цифр(от 4 до 6)\n'))
   
    initial = []
    max_rating = 0
    def array(n, max_rating):
        for i in range(n):  #перебираем все возможные варианты
            for j in range(i + 1, n):
                for k in range(j + 1, n):
                    for b in range(k + 1, n):
                        combo = [chet[i], '0', chet[k], '0']
                        rate_sum = sum([value[number] for number in combo])
                        if rate_sum > max_rating: 
                            max_rating_combination = combo
                            max_rating = rate_sum                              
                        initial.append((combo, rate_sum))
        print(f'Всего может быть составлено {len(initial)} комбинаций из {n} цифр.\n\n'
          f'Список комбинаций цифр ({", ".join(chet[:n])}) c общей суммой:\n')
        for count, combo in enumerate(initial, start=1):
            print(f'{count}. {" - ".join((str(x) for x in combo))}')
        print('\nВариант комбинации с наивысшей суммой:')
        return max_rating_combination, max_rating
    print(array(n, max_rating))

if choice == '2':
    n = int(input('\nВведите количество используемых цифр\n'))
    
    initial = []
    max_rating = 0
    def array(n, max_rating):
        for i in range(n):  #перебираем все возможные варианты
            for j in range(i + 1, n):
                for k in range(j + 1, n):
                    for b in range(k + 1, n):
                        combo = [nechet[i], '0', nechet[k], '0']
                        rate_sum = sum([value[number] for number in combo])
                        if rate_sum > max_rating:
                            max_rating_combination = combo
                            max_rating = rate_sum                              
                        initial.append((combo, rate_sum))
        
        print(f'Всего может быть составлено {len(initial)} комбинаций из {n} цифр.\n\n'
          f'Список комбинаций квартета из инструментов ({", ".join(nechet[:n])}) c общей суммой:\n')
        for count, combo in enumerate(initial, start=1):
            print(f'{count}. {" - ".join((str(x) for x in combo))}')
        print('\nВариант квартета с наивысшей суммой:')
        return max_rating_combination, max_rating
    print(array(n, max_rating))
    print('\nВариант квартета с наивысшей суммой:')
    print(array(n, max_rating))
