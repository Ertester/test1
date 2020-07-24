n = int(input())
a=0
c=b=1
for i in range(int(n-1)):
    c=a+b
    a=b
    b=c
print(a , '' , b, '' , c)