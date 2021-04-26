import io
import random
import numpy as np
import json
import sympy as sp
from math import *
from flask import Flask,render_template,Response,request,jsonify
"""
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure
"""

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/m-biseccion/',methods=['GET', 'POST'])
def mbiseccion():
    return render_template('m-biseccion.html')


@app.route('/m-newtoon/')
def mnewtoon():
    return render_template('m-newtoon.html')

"""   
@app.route('/plot.png')
def plot_png():
    fig = create_figure()
    output = io.BytesIO()
    FigureCanvas(fig).print_png(output)
    return Response(output.getvalue(), mimetype='image/png')

def create_figure():
    fig = Figure()
    axis = fig.add_subplot(1, 1, 1)
    xs = range(100)
    ys = [random.randint(1, 50) for x in xs]
    axis.plot(xs, ys)
    return fig
"""

@app.route('/majaxbiseccion/',methods=['GET', 'POST'])
def majaxbiseccion():
    def f(x):
        return pow(x,3)-5*(x)+e**(x)
    
    def biseccion(a,b,tol):
        m1=a
        m=b
        k=0
        if(f(a)*f(b)>0):
            print('La funcion no cambia de signo')
        lista = []
        while(abs(f(m))>tol):
            m1=m
            m=(a+b)/2
            if(f(a)*f(m)<0): #Cambia de signo en [a,m]
                b=m
            if(f(m)*f(b)<0): #Cambia de signo en [m,b]
                a=m
            nuevodato = 'El intervalo es [',a,',',b,']'
            lista.append(nuevodato)
            k=k+1
            aproximacion = 'x',k,'=',m,'Es una buena aproximación'
        return (lista,aproximacion)
    resultado = []
    int1=None
    int2=None
    tole=None
    ecuac=None
    if request.method == "POST":
        int1 = int(request.form['int1'])
        int2 = int(request.form['int2'])
        tole = float(request.form['tole'])
        #ecuac = request.form['ecuac']
        resultado = biseccion(int1,int2, tole)  
    return jsonify(resultado=resultado)

@app.route('/majaxnewtoon/',methods=['GET', 'POST'])
def majaxnewtoon():
    def NewtonRaphson(x0,tol,n,ecuac):
        x=sp.symbols('x')
        f=ecuac
        df = sp.diff(f)
        f=sp.lambdify(x,f)
        df=sp.lambdify(x,df)

        lista = []
        for k in range(n):
            x1=x0-f(x0)/df(x0)
            if(abs(x1-x0)<tol):
                print('x',k+1,'=',x1,end='')
                print('Es una buena aproximación')
                nuevodato='x',k+1,'=',x1 , "Es una buena aproximación"
                lista.append(nuevodato)
                aproximacion ='El valor de la funcion evaluado es =',f(x1)
                return (lista,aproximacion)
            x0=x1
            print('x',k+1,'=',x1)
            nuevodato='x',k+1,'=',x1
            lista.append(nuevodato)
        

    resultado = []
    x0=None
    tol=None
    cant=None
    if request.method == "POST":
        x0 = int(request.form['x0'])
        tol = float(request.form['tol'])
        cant = int(request.form['cant'])
        ecuac = request.form['ecuac']
        resultado = NewtonRaphson(x0,tol,cant,ecuac)  
    return jsonify(resultado=resultado)

if __name__ == '__main__':
    app.run(debug=True)