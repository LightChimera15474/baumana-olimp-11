from random import  randint


def print_matrix(m):
    for line in m:
        print(' '.join(map(str, line)))


rows = int(input())
cols = int(input())
matrix = [[randint(0, 0) for i in range(rows)] for line in range(cols)]

cntInputs = 0
x, y = 0, 0
Index = 0

while cntInputs < rows * cols:
    print()
    print_matrix(matrix)
    while y > 0 and x < cols - 1:
        x += 1
        y -= 1
        matrix[y][x] = 1#randint(0, 1)
        cntInputs += 1
    if x < cols - 1:
        x += 1
        matrix[y][x] = 1#randint(0, 1)
        cntInputs += 1
    else:
        y += 1
        matrix[y][x] = 1#randint(0, 1)
        cntInputs += 1

    while y < rows - 1 and x > 0:
        x -= 1
        y += 1
        matrix[y][x] = 1#randint(0, 1)
        cntInputs += 1
    x += 1
    matrix[y][x] = 1#randint(0, 1)
    cntInputs += 1

print(matrix)
