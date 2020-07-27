n = int(input())
print(n)
def fibo(n):
    a=0
    c=b=1
    for i in range(n-1):
        c=a+b
        a=b
        b=c
    return a , '' , b, '' , c
print(fibo(n))


def fibonacci(n):
    a, b = 0, 1
    for i in range(n):
        a, b = b, a+b
    return a


