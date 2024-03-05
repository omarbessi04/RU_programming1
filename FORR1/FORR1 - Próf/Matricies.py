# With two given matricies, A and B, create matrix C, which is the addition of matricies A and B

def create_matrices():
    """Create matricies A and B, and return them as (matrix_A, matrix_B)"""
    matrix_A = []
    matrix_B = []

    for i in range(2):
        for j in range(NUMBER_OF_ROWS):
            # For every row, create an empty row
            row = []
            for y in range(NUMBER_OF_COLUMNS):
                # For every column in said row, insert an integer input
                row.append(int(input()))
                
            # Append the newly created row to either matrix A or B
            if i == 0:
                matrix_A.append(row)
            else:
                matrix_B.append(row)

    return matrix_A, matrix_B

def create_matrix_C():
    """Create matrix C, the addition of matricies A and B"""
    matrix_C = []

    for i in range(NUMBER_OF_ROWS):
        # For every row, create an empty row
        row = []
        for j in range(NUMBER_OF_COLUMNS):
            # For every number in A, add the number in B with the matching position, and insert it into the row
            position_addition = matrix_A[i][j] + matrix_B[i][j]
            row.append(position_addition)
        # Append the row to matrix C
        matrix_C.append(row)

    return matrix_C


NUMBER_OF_ROWS = 2
NUMBER_OF_COLUMNS = 3

matrix_A, matrix_B = create_matrices()

matrix_C = create_matrix_C()

print(matrix_A)
print(matrix_B)
print(matrix_C)