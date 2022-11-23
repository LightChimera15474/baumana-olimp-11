n = int(input())
rows = cols = n

matrix = [[int(i) for i in input().split()] for line in range(cols)]
resArray = []
leftArray = []
rightArray = []

cnt = int((rows * cols - rows) / 2)

x = rows
y = 0
# right up
for i in range(cnt):
    while True:
        if x - 1 != y and x - 1 >= 0:
            x -= 1
            rightArray.append(matrix[y][x])
        else:
            x = rows
            y += 1
            break

x = 0
y = cols
# left down
for i in range(cnt):
    while True:
        if y - 1 != x and y - 1 >= 0:
            y -= 1
            leftArray.append(matrix[y][x])
        else:
            x += 1
            y = cols
            break

for i in range(len(rightArray)):
    resArray.append(rightArray[i])
    resArray.append(leftArray[i])

x = y = 0
while x < rows and y < cols:
    resArray.append(matrix[y][x])
    x += 1
    y += 1

print(' '.join(map(str, resArray)))
