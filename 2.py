def convert_to_quaternary(num):
    res = ''
    while num > 0:
        res += str(num % 4)
        num //= 4
    return res[::-1]


print(convert_to_quaternary(int(input())).count('3'))
