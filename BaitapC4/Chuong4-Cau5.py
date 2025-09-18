def fibonancci(n):
    if n <= 2:
        return 1
    return fibonancci(n-1) + fibonancci(n-2)

def listfibo(n):
    for i in range(1, n + 1):
        print(fibonancci(i), end='\t ')
print(fibonancci(9))
listfibo(9)