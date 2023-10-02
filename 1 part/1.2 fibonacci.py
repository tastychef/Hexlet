def fib(n):
    return (fib(n-1)+fib(n-2) if n>=2 else 1 if n==1 else 0)
