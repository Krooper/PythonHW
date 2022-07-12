class Cell:
    def __init__(self, cellule):
        self.cellule = cellule

    def __add__(self, cell):
        return Cell(self.cellule + cell.cellule)

    def __sub__(self, cell):
        return Cell(self.cellule - cell.cellule)

    def __mul__(self, cell):
        return Cell(self.cellule * cell.cellule)

    def __floordiv__(self, cell):
        return Cell(self.cellule // cell.cellule)

    def __truediv__(self, cell):
        return Cell(self.cellule / cell.cellule)

    def __str__(self):
        return f'{self.cellule}'

    def make_order(self, number):
        cellule_num = self.cellule
        order = ''
        while cellule_num > 0:
            i = 0
            while i < number:
                if i == number - 1:
                    if cellule_num != 0:
                        order += '*\n'
                        cellule_num -= 1
                        i += 1
                    else: break
                else:
                    if cellule_num != 0:
                        order += '*'
                        cellule_num -= 1
                        i += 1
                    else: break
        return order


cell1 = Cell(16)
cell2 = Cell(3)

add_cell = cell1+cell2
sub_cell = cell1-cell2
mul_cell = cell1*cell2
floordiv_cell = cell1//cell2
truediv_cell = cell1/cell2

print(cell1)
print(cell2)
print(add_cell)
print(sub_cell)
print(mul_cell)
print(floordiv_cell)
print(truediv_cell)
print(cell1.make_order(4))

