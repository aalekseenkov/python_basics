"""
Задание 5.

Реализовать формирование списка, используя функцию range()
и возможности генераторного выражения.

В список должны войти четные числа от 100 до 1000 (включая границы).
Необходимо получить результат вычисления произведения всех элементов списка.

Подсказка: использовать лямбда-функцию и функцию reduce().
"""
from functools import reduce

primary_list = (x for x in range(100, 1001, 2))

result = reduce(lambda item1, item2: item1 * item2, primary_list)

print(f"Result is {result}")
