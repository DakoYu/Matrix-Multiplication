def is_valid(a):
    prev = len(a[0])
    for i in range(1, len(a)):
        if prev != len(a[i]):
            return False
    return True

def matrix_multiply(a,b):
    res1 = is_valid(a)
    res2 = is_valid(b)
    if res1 != res2:
        return []
    matrix = create_matrix(len(a), len(b[0]))
    print(matrix)
    for i in range(len(a)):
        for j in range(len(b[0])):
            for k in range(len(b)):
                matrix[i][j] += a[i][k] * b[k][j]
    return matrix

def create_matrix(m, n):
    matrix = []
    for i in range(m):
        my_row = []
        for j in range(n):
            my_row.append(0)
        matrix.append(my_row)
    return matrix


a = [[1,2,3],[4,5,6]]
b = [[1,2],[3,4], [5,6]]
print(matrix_multiply(a,b))
