def fib0(n):
    a,b=0,1
    while(a<n):
        print(a,end=' ')
        a,b = b,a+b
        print()

def fib1(n):
    res = []
    a,b = 0,1
    while(a<n):
        res.append(a)
        a,b = b,a+b
    return res
fib1(5)
