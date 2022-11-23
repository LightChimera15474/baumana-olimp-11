from functools import lru_cache


def sort_and_count(string, alp):
    array = list(string)
    cnt = 0
    for i in range(len(array)):
        for j in range(len(array) - 1):
            if alp[array[j]] > alp[array[j + 1]]:
                array[j], array[j + 1] = array[j + 1], array[j]
                cnt += 1
    return cnt


@lru_cache()
def input_alphabet(n):
    res = {}
    for i in range(n):
        inputValue = input().split()
        tmpDict = {inputValue[0]: int(inputValue[1])}
        res.update(tmpDict)
    return res


N = int(input())
alphabet = input_alphabet(N)
sortedStr = str(input())
print(sort_and_count(sortedStr, alphabet))
