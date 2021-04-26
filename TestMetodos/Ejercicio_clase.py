from math import *

def f(x):
    return pow(x,3)-5*(x)+e**(x)

def biseccion(a,b,tol):
    m1=a
    m=b
    k=0
    if(f(a)*f(b)>0):
        print('La funcion no cambia de signo')
    
    while(abs(f(m))>tol):
        m1=m
        m=(a+b)/2
        if(f(a)*f(m)<0): #Cambia de signo en [a,m]
            b=m
        if(f(m)*f(b)<0): #Cambia de signo en [m,b]
            a=m
        print('El intervalo es [',a,',',b,']')
        k=k+1
    
    print('x',k,'=',m,'Es una buena aproximación')

biseccion(1,3, 10**(-2))