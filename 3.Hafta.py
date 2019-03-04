#recursive fonksiyonlar

print("-------------------")

def power(m,n):
    s=m
    for i in range(1,n):
        s=s*m

    return s

def power_recursive_me(m,n):
    if(n==0):
        return 1
    elif(n==1):
        return m
    else:
        return m*power_recursive_(m,n-1)
    
def power_recursive(m,n):
    if(n==0):
        return 1
    elif(n==1):
        return m
    elif(n%2==0):
        return power_recursive(m*m,n//2)
    elif(n%2!=0):
        return power_recursive(m*m,n//2)*m
    
def factorial(n):
    s=1
    for i in range(1,n+1):
        s=s*i

    return s

def factorial_recursive(n):
    if(n==1):
        return n
    else:
        return n*factorial_recursive(n-1)


def fib(n):
    a,b=0,1
    for i in range(n-1):
        a,b=b,a+b
    return a

def fib_recursive(n):
    if(n==1):
        return 0
    elif(n<=3):
        return 1
    else:
        return fib_recursive(n-2)+fib_recursive(n-1)


print("5 üzeri 3:",power(5,3))
print("-------------------")
print("5 üzeri 3(recursive):",power_recursive(5,3))
print("--------------------")
print("5 faktoriel:",factorial(5))
print("-------------------")
print("5 faktoriel(recursive):",factorial_recursive(5))
print("-------------------")
print("8.fib:",fib(8))
print("-------------------")
print("8.fib(recursive):",fib_recursive(8))
