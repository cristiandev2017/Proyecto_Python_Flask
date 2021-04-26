import sympy as sp
from math import *

'''
def f(x):
    func=cos(x)-x**3
    return func

def df(x):
    return -sin(x)-3*x**2
'''

def NewtonRaphson(x0,tol,n):
    x=sp.symbols('x')
    f=input('Digite la funcion (con variable x)')
    df = sp.diff(f)
    f=sp.lambdify(x,f)
    df=sp.lambdify(x,df)

    for k in range(n):
        x1=x0-f(x0)/df(x0)
        if(abs(x1-x0)<tol):
            print('x',k+1,'=',x1,end='')
            print('Es una buena aproximación')
            print('El valor de la funcion evaluado es =',f(x1))
            return
        x0=x1
        print('x',k+1,'=',x1)

NewtonRaphson(1, 0.01, 10)
