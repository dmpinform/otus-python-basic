"""
Домашнее задание №1
Функции и структуры данных
"""


def power_numbers(*numbers):
    """
    функция, которая принимает N целых чисел,
    и возвращает список квадратов этих чисел
    """

    numbers = [*numbers]
    listn = list(num**2 for num in numbers if str(num).isdigit())
    if len(listn) != len(numbers):
        print(f'Error int value in list: {numbers}')
    return listn

# filter types
ODD = "odd"
EVEN = "even"
PRIME = "prime"


def filter_numbers(numbers, ft=ODD):
    """
    функция, которая на вход принимает список из целых чисел,
    и возвращает только чётные/нечётные/простые числа
    (выбор производится передачей дополнительного аргумента)
    """
    listn = list(num for num in numbers if str(num).isdigit())
    if len(listn) != len(numbers):
        print(f'Error int value in list: {numbers}')
        return numbers

    list_result = []
    if ft == ODD:
        list_result = list(n for n in numbers if n % 2 > 0)
    if ft == EVEN:
        list_result = list(n for n in numbers if n % 2 == 0)
    if ft == PRIME:
        for n in numbers:
            isprime = True
            if n > 1:
                for x in range(2, n):
                    if n % x == 0:
                        isprime = False
                        break
                if isprime:
                    list_result.append(n)

    return list_result
