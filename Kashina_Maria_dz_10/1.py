class Matrix:
    def __init__(self, rows_in_matrix):
        self.rows_in_matrix = rows_in_matrix

    def __str__(self):
        return str('\n'.join(['\t'.join([str(el) for el in row]) for row in self.rows_in_matrix]))

    def __add__(self, other):
        new_matrix = []
        for i in range(len(self.rows_in_matrix)):
            new_rows = []
            for j in range(len(other.rows_in_matrix[i])):
                new_rows.append(self.rows_in_matrix[i][j] + other.rows_in_matrix[i][j])
            new_matrix.append(new_rows)
        return str('\n'.join(['\t'.join([str(el) for el in row]) for row in new_matrix]))


matrix1 = Matrix([[-1, 0, 1], [-1, 0, 1], [0, 1, -1], [1, 1, -1]])
matrix2 = Matrix([[-2, 0, 2], [-2, 0, 2], [0, 2, -2], [2, 2, -7]])
print(matrix1 + matrix2)
print(matrix1)
print(matrix2)
