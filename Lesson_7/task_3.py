"""
Задание 3.

Реализовать программу работы с органическими клетками, состоящими из ячеек.

Необходимо создать класс Клетка (Cell).

В его конструкторе инициализировать параметр (quantity),
соответствующий количеству ячеек клетки (целое число).

В классе должны быть реализованы методы перегрузки арифметических операторов:
сложение (add()),
вычитание (sub()),
умножение (mul()),
деление (truediv()).

Данные методы должны применяться только к клеткам и выполнять увеличение,
уменьшение, умножение и целочисленное (с округлением до целого) деление клеток,
соответственно.

Сложение. Объединение двух клеток. При этом число ячеек общей клетки должно
равняться сумме ячеек исходных двух клеток.

Вычитание. Участвуют две клетки. Операцию необходимо выполнять только если
разность количества ячеек двух клеток больше нуля, иначе выводить
соответствующее сообщение.

Умножение. Создается общая клетка из двух. Число ячеек общей клетки определяется
как произведение количества ячеек этих двух клеток.

Деление. Создается общая клетка из двух.
Число ячеек общей клетки определяется как целочисленное деление количества ячеек
этих двух клеток.

** - По желанию: В классе необходимо реализовать метод make_order(), принимающий
экземпляр класса и количество ячеек в ряду. Данный метод позволяет организовать
ячейки по рядам. Метод должен возвращать строку вида *****\n*****\n*****...,
где количество ячеек между \n равно переданному аргументу. Если ячеек на
формирование ряда не хватает, то в последний ряд записываются все оставшиеся.

Например, количество ячеек клетки равняется 12, количество ячеек в ряду — 5.
Тогда метод make_order() вернет строку: *****\n*****\n**.
Или, количество ячеек клетки равняется 15, количество ячеек в ряду — 5.
Тогда метод make_order() вернет строку: *****\n*****\n*****.
Подсказка: подробный список операторов для перегрузки доступен по ссылке.

------------------------------------------------------------------------------
Пример клиентского кода:
print("Создаем объекты клеток")
cell1 = Cell(30)
cell2 = Cell(25)

cell3 = Cell(10)
cell4 = Cell(15)

    print()

    print("Складываем")
    print(cell1 + cell2)

    print()

    print("Вычитаем")
    print(cell2 - cell1)
    print(cell4 - cell3)

    print()

    print("Умножаем")
print(cell2 * cell1)

print()

print("Делим")
print(cell1 / cell2)

print()

print("Организация ячеек по рядам")
print(cell1.make_order(5))
print(cell2.make_order(10))

------------------------------------------------------------------------------
Результаты:
Создаем объекты клеток

Складываем
Сумма клеток = (55)

Вычитаем
Разность отрицательна, поэтому операция не выполняется
Разность клеток = (5)

Умножаем
Умножение клеток = (750)

Делим
Деление клеток = (1)

Организация ячеек по рядам
*****\n *****\n *****\n *****\n *****\n *****\n
**********\n **********\n *****
"""


class Cell:
    """ Cell Class Docstring """

    def __init__(self, quantity):
        self.quantity = int(quantity)

    def __str__(self):
        return f'({self.quantity})'

    def __add__(self, other):
        return f'Sum of cells = {str(Cell(self.quantity + other.quantity))}'

    def __sub__(self, other):
        if (self.quantity - other.quantity) > 0:
            return f'Residue of cells = {Cell(int(self.quantity - other.quantity))}'
        return 'Residue is negative so action does not execute'

    def __mul__(self, other):
        return f'Multiplication of cells = {Cell(int(self.quantity * other.quantity))}'

    def __truediv__(self, other):
        return f'Division of cell = {Cell(round(self.quantity // other.quantity))}'

    def make_order(self, cells_count):
        """ make_order docstring """
        row = ''
        for _ in range(int(self.quantity / cells_count)):
            row += f'{"*" * cells_count}\\n '
        row += f'{"*" * (self.quantity % cells_count)}'
        return row


print("Create cell's objects")
cell1 = Cell(32)
cell2 = Cell(14)

cell3 = Cell(12)
cell4 = Cell(22)

print()

print("Addition")
print(cell1 + cell2)

print()

print("Subtraction")
print(cell2 - cell1)
print(cell4 - cell3)

print()

print("Multiplication")
print(cell2 * cell1)

print()

print("Division")
print(cell1 / cell2)

print()

print("Organization of cells by rows")
print(cell1.make_order(4))
print(cell2.make_order(11))