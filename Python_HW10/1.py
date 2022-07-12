class Matrix:
    def __init__(self, num_lst):
        self.rows = len(num_lst)
        self.columns = len(num_lst[0])
        self.elements = num_lst

    def __str__(self):
        out = ''
        for i in range(self.rows):
            out += '|'
            for j in range(self.columns):
                if j == self.columns - 1:
                    out += f'{self.elements[i][j]}|\n'
                else:
                    out += f'{self.elements[i][j]}\t'
        return out

    def __add__(self, sec_matrix):
        if self.rows == sec_matrix.rows and self.columns == sec_matrix.columns:
            res_lst = [[0] * self.columns for i in range(self.rows)]
            for i in range(self.rows):
                for j in range(self.columns):
                    res_lst[i][j] += self.elements[i][j] + sec_matrix.elements[i][j]
            res_matrix = Matrix(res_lst)
            return res_matrix
        else:
            return None


numbers1 = [[1, 2, 3, 4], [5, 6, 7, 8]]
numbers2 = [[10, 9, 8, 7], [6, 5, 4, 3]]
matrix1 = Matrix(numbers1)
matrix2 = Matrix(numbers2)
matrix3 = matrix1 + matrix2

print('Первая матрица:')
print(matrix1)
print('Вторая матрица:')
print(matrix2)
print('Результат их сложения:')
print(matrix3)
