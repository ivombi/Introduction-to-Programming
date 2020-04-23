import turtle
def koch(t,order,size):
    if order==0:
        t.forward(size)
    else:
        for angle in [60,-120,60,0]:
            koch(t,order-1,size/3)
            t.left(angle)

t = turtle.Turtle()
koch(t,4,1000)

def fac_iter(n):
    res = 1
    i = 1
    while i <=n:
        res*=i
    return res

def fac_rec(n):
    if n==0 or n==1:
        return 1
    else:
        return n*fac_rec(n-1)

#Exercises
#7.2
def print_first(string,i):
    while i !=len(string):
        print(string[i])
        i +1

#7.3
def weird_stuff(i):
    while i >=0:
        if (i==0):
            return
        else:
            print(""*i,"x")
            print(""*i,"x")
            i-=1

#7.5
def ackermann_function(m, n):
    if m == 0:
        return n + 1
    elif m > 0 and n == 0:
        return ackermann_function(m - 1, 1)
    elif n > 0 and m > 0:
        return ackermann_function(m - 1, ackermann_function(m, n - 1))

def convert(string_number):
    n = len(string_number)
    i = 0
    for letter in string_number:
        return 10^n +convert(string_number)
        n-=1

convert("12345")
