"""
Задание 4.

Пользователь вводит целое положительное число.
Найдите самую большую цифру в числе.
Для решения используйте цикл while и только арифметические операции.
"""
num = int(input("Enter an integer: "))
max = num % 10
num = num // 10
while num > 0:
    if num % 10 > max:
        max = num % 10
    num = num // 10
print(f"The largest digit is {max}")
