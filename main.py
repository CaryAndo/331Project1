import random


def matrix_add(a, b):
    """ Add two matrices """
    m = [[0 for j in range(len(a[0]))] for i in range(len(a))]
    for row_index, i in enumerate(a):
        for col_index, j in enumerate(i):
            m[row_index][col_index] = a[row_index][col_index] + b[row_index][col_index]
    return m


def matrix_subtract(a, b):
    """ Subtract two matrices """
    m = [[0 for j in range(len(a[0]))] for i in range(len(a))]
    for row_index, i in enumerate(a):
        for col_index, j in enumerate(i):
            m[row_index][col_index] = a[row_index][col_index] - b[row_index][col_index]
    return m


def generate_random_matrix(n):
    """ Generate a random nXn matrix """
    return [[random.randint(1, 50) for i in range(n)] for j in range(n)]


def naive_multiply(a, b):
    """ Naive matrix multiplication, _should_ be O(n^3) """
    m = len(a)  # Number of rows in first matrix
    k = len(b)  # Number of rows in the second matrix
    res = []
    p = len(b[0])
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

    a11 = a[0:int(len(a) / 2)]
    for index, row in enumerate(a11):
        a11[index] = row[0:int(len(row) / 2)]

    a12 = a[0:int(len(a) / 2)]
    for index, row in enumerate(a12):
        a12[index] = row[int(len(a) / 2):len(a)]

    a21 = a[int(len(a) / 2):len(a)]
    for index, row in enumerate(a21):
        a21[index] = row[0:int(len(row) / 2)]

    a22 = a[int(len(a) / 2):len(a)]
    for index, row in enumerate(a22):
        a22[index] = row[int(len(a) / 2):len(a)]

    b11 = b[0:int(len(b) / 2)]
    for index, row in enumerate(b11):
        b11[index] = row[0:int(len(row) / 2)]

    b12 = b[0:int(len(b) / 2)]
    for index, row in enumerate(b12):
        b12[index] = row[int(len(b) / 2):len(b)]

    b21 = b[int(len(b) / 2):len(b)]
    for index, row in enumerate(b21):
        b21[index] = row[0:int(len(row) / 2)]

    b22 = b[int(len(b) / 2):len(b)]
    for index, row in enumerate(b22):
        b22[index] = row[int(len(b) / 2):len(b)]

    c11 = matrix_add(recursive_multiply(a11, b11), recursive_multiply(a12, b21))  # C11 = A11*B11 + A12*B21
    c12 = matrix_add(recursive_multiply(a11, b12), recursive_multiply(a12, b22))  # C12 = A11*B12 + A12*B22
    c21 = matrix_add(recursive_multiply(a21, b11), recursive_multiply(a22, b21))  # C21 = A21*B11 + A22*B21
    c22 = matrix_add(recursive_multiply(a21, b12), recursive_multiply(a22, b22))  # C22 = A21*B12 + A22*B22

    # Append c12 to c11
    for row_index, row in enumerate(c11):
        for col_index, col in enumerate(c12):
            row.append(c12[row_index][col_index])

    # Append c22 to c21
    for row_index, row in enumerate(c21):
        for col_index, col in enumerate(c12):
            row.append(c22[row_index][col_index])

    # Append c21 to c11
    for i in c21:
        c11.append(i)

    return c11


def strassen(a, b):
    if len(a) == 2:
        return naive_multiply(a, b)

    a11 = a[0:int(len(a) / 2)]
    for index, row in enumerate(a11):
        a11[index] = row[0:int(len(row) / 2)]

    a12 = a[0:int(len(a) / 2)]
    for index, row in enumerate(a12):
        a12[index] = row[int(len(a) / 2):len(a)]

    a21 = a[int(len(a) / 2):len(a)]
    for index, row in enumerate(a21):
        a21[index] = row[0:int(len(row) / 2)]

    a22 = a[int(len(a) / 2):len(a)]
    for index, row in enumerate(a22):
        a22[index] = row[int(len(a) / 2):len(a)]

    b11 = b[0:int(len(b) / 2)]
    for index, row in enumerate(b11):
        b11[index] = row[0:int(len(row) / 2)]

    b12 = b[0:int(len(b) / 2)]
    for index, row in enumerate(b12):
        b12[index] = row[int(len(b) / 2):len(b)]

    b21 = b[int(len(b) / 2):len(b)]
    for index, row in enumerate(b21):
        b21[index] = row[0:int(len(row) / 2)]

    b22 = b[int(len(b) / 2):len(b)]
    for index, row in enumerate(b22):
        b22[index] = row[int(len(b) / 2):len(b)]

    p = strassen(matrix_add(a11, a22), matrix_add(b11, b22))
    q = strassen(matrix_add(a21, a22), b11)
    r = strassen(a11, matrix_subtract(b12, b22))
    s = strassen(a22, matrix_subtract(b21, b11))
    t = strassen(matrix_add(a11, a12), b22)
    u = strassen(matrix_subtract(a21, a11), matrix_add(b11, b12))
    v = strassen(matrix_subtract(a12, a22), matrix_add(b21, b22))

    c11 = matrix_add(matrix_subtract(matrix_add(p, s), t), v)
    c12 = matrix_add(r, t)
    c21 = matrix_add(q, s)
    c22 = matrix_add(matrix_subtract(matrix_add(p, r), q), u)

    # Append c12 to c11
    for row_index, row in enumerate(c11):
        for col_index, col in enumerate(c12):
            row.append(c12[row_index][col_index])

    # Append c22 to c21
    for row_index, row in enumerate(c21):
        for col_index, col in enumerate(c12):
            row.append(c22[row_index][col_index])

    # Append c21 to c11
    for i in c21:
        c11.append(i)

    return c11


def print_matrix(matrix):
    """ Print a matrix.. """
    for i in matrix:
        print(i)
    print("")


if __name__ == '__main__':
    import time

    for z in range(1, 10):
        print(str(2**z) + 'X' + str(2**z) + ' elements:')
        ma = generate_random_matrix(2**z)
        mb = generate_random_matrix(2**z)
        c = []
        t1 = time.time()
        c = naive_multiply(ma, mb)
        t2 = time.time()
        print('Naive: ' + str((t2 - t1)*1000) + 'ms')

        t1 = time.time()
        c = recursive_multiply(ma, mb)
        t2 = time.time()
        print('Recursive: ' + str((t2 - t1)*1000) + 'ms')

        t1 = time.time()
        c = strassen(ma, mb)
        t2 = time.time()
        print('Strassen: ' + str((t2 - t1)*1000) + 'ms')
        print("")
