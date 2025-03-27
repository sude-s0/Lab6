import math


def factorial(x):
    if x==0 or x==1:
        return 1
    else:
        return x * factorial(x-1)


formula = lambda x,n:((-1)**n)*(x**(2*n+1))/factorial(2*n+1)


def sine_x(x,n):
    rad_of_x= x*(math.pi/180)

    sum = 0
    for i in range(n):
        sum+=formula(rad_of_x,i)

    return sum


a = 0.0


def h_function(n):
    global a

    if n == 1 :
        a+=1
    else:
        h_function(n-1)
        a+=1/n
