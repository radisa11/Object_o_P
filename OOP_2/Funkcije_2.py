def f(a=5,b=0,c=9):
    print(a,b,c)

f(1,2,3) 
f(1,2)   
f(1)   
f()   


def g(*args):
    print(args)

g(1,2,3,4,5)
g(1,2,3,4,5,6,7,8,9,0)


def h(a,b,*c,**k):
    print(a,b,c,k["s"],k["s2"])
    print(a,b,c,k)

h(3,4,7,9,2,s="Dobar dan",s2="Dobro Vece")
def Min(a: int,b: int) -> int:
    return a if a<b else b

c = Min(7,9)
print(c)
print(Min(7,9))

def kako_hocemo(*a: int) -> int:
    m=a[0]
    for i in range(1,len(a)):
        if a[i]>m:
            m = a[i]
    return m
    


maxi = kako_hocemo(1,2,3,4,0,9,21)
print(maxi)

def suma(*a: int) -> int:
    s: int = 0
    for i in a:
        s += i 
    return s

su = suma(1,2,3,4,0,9,21)
print(su)

def suma_n(n: int) -> int:
    s: int = 0
    for i in range(1,n+1):
        s += i
        return s
    
print(suma_n(5)) 


def f(n):
    if n==0:
        return
    print(n,end=" ")
    f(n-1)  
    print(n,end=" ") 

f(10)

a = [1,2,3,4,5]
def parcici(a):
    if len(a)==0:
        return
    print(a)
    parcici(a[1:])

parcici(a)

a = [1,2,3,4,5]
def iterativni_parcici(a):
    for i in range(len(a)):
        print(a[i:])

iterativni_parcici(a)

def rek_suma(n):
    print(f"poziva se rek_suma ({n})")
    if n==0:
        return 0
    return n + rek_suma(n-1)
print(rek_suma(5))

def sum_number(a,b):
    return a + b
print(sum_number(1,3))

sum_number_l = lambda a,b: a + b
print(sum_number_l(1,3))

def myFunction(f):
    f("Hallo World!")

myFunction(print)

def myFunction_2(f):
    return f("Hallo World!")

print(myFunction_2(len))



