import math
x = int(input("Nhập x: "))
n = int(input("Nhập n: "))
def S(x, n):
    result = 0
    for k in range(n + 1):
        result += (x ** (2 * k + 1)) / math.factorial(2 * k + 1)
    return result

print(S(x, n))
