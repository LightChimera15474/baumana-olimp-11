def join_array(array):
    res = ''
    for i in array:
        res += str(i)
    return int(res)


numArray = [int(i) for i in input()]
startNum = join_array(numArray)

index = numArray.index(min(numArray))
numArray[index] += 2

endNum = join_array(numArray)

result = endNum - startNum
print(result)
