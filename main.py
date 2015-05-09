def matrix_add(a, b):
    """ Add two matrices """
    c = [[0 for j in range(len(a[0]))] for i in range(len(a))]
    for row_index, i in enumerate(a):
        for col_index, j in enumerate(i):
            c[row_index][col_index] = a[row_index][col_index] + b[row_index][col_index]
    return c


def naive_multiply(a, b):
    """ Naive matrix multiplication, _should_ be O(n^3) """
    m = len(a)  # Number of rows in first matrix
    n = len(a[0])  # Number of columns in the second matrix
    k = len(b)  # Number of rows in the second matrix
    res = []
    if len(b) != 1:
        p = len(b[0])
    else:
        p = 0
    if len(b) == 0:
        print('Second param is not big enough')
    elif n != k:
        print('Size mismatch!')
    else:
        n = k
        for q in range(m):
            res.append([0])
        for q in range(m):
            for w in range(p - 1):
                res[q].append(0)
        for i in range(m):
            for j in range(p):
                for r in range(n):
                    res[i][j] = a[i][r] * b[r][j] + res[i][j]
    return res


def recursive_multiply(a, b):
    """ This method only works with square matrices """
    if len(a) == 2:
        return naive_multiply(a, b)

    a11 = a[0:int(len(a)/2)]
    for index, row in enumerate(a11):
        a11[index] = row[0:int(len(row)/2)]

    a12 = a[0:int(len(a)/2)]
    for index, row in enumerate(a12):
        a12[index] = row[int(len(a)/2):len(a)]

    a21 = a[int(len(a)/2):len(a)]
    for index, row in enumerate(a21):
        a21[index] = row[0:int(len(row)/2)]

    a22 = a[int(len(a)/2):len(a)]
    for index, row in enumerate(a22):
        a22[index] = row[int(len(a)/2):len(a)]

    b11 = b[0:int(len(b)/2)]
    for index, row in enumerate(b11):
        b11[index] = row[0:int(len(row)/2)]

    b12 = b[0:int(len(b)/2)]
    for index, row in enumerate(b12):
        b12[index] = row[int(len(b)/2):len(b)]

    b21 = b[int(len(b)/2):len(b)]
    for index, row in enumerate(b21):
        b21[index] = row[0:int(len(row)/2)]

    b22 = b[int(len(b)/2):len(b)]
    for index, row in enumerate(b22):
        b22[index] = row[int(len(b)/2):len(b)]

    c11 = matrix_add(recursive_multiply(a11, b11), recursive_multiply(a12, b21))  # C11 = A11*B11 + A12*B21
    c12 = matrix_add(recursive_multiply(a11, b12), recursive_multiply(a12, b22))  # C12 = A11*B12 + A12*B22
    c21 = matrix_add(recursive_multiply(a21, b11), recursive_multiply(a22, b21))  # C21 = A21*B11 + A22*B21
    c22 = matrix_add(recursive_multiply(a21, b12), recursive_multiply(a22, b22))  # C22 = A21*B12 + A22*B22

    for row_index, row in enumerate(c11):
        for col_index, col in enumerate(c12):
            row.append(c12[row_index][col_index])

    for row_index, row in enumerate(c21):
        for col_index, col in enumerate(c12):
            row.append(c22[row_index][col_index])

    for i in c21:
        c11.append(i)

    return c11


def print_matrix(matrix):
    """ Print a matrix.. """
    for i in matrix:
        print(i)
    print("")


def pad_uneven_matrix(matrix):
    new_matrix = matrix

    if len(matrix) % 2 != 0:
        new_matrix.append([0 for i in range(len(new_matrix[0]))])  # Append a new row of 0's

    if len(matrix[0]) % 2 != 0:
        for row in new_matrix:
            row.append(0)  # Append a 0 to the end of each row (add a column)

    return matrix


if __name__ == '__main__':
    aE = [[1, 4, 5, 6],
         [1, 1, 1, 6],
         [1, 9, 8, 6],
         [1, 9, 8, 6]]

    bE = [[3, 4, 5, 3],
         [2, 3, 4, 2],
         [7, 3, 3, 2],
         [4, 1, 4, 1]]

    cE = [[1, 3],
         [4, 4]]

    dE = [[3,5],
         [1, 6]]

    c = naive_multiply(aE, bE)
    d = recursive_multiply(aE, bE)

    print_matrix(c)

    print_matrix(d)
