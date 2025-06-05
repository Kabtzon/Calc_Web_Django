from django.shortcuts import render
import sympy as sp
import numpy as np
import matplotlib.pyplot as plt
import os
from .metodos.biseccion import metodo_biseccion
from .metodos.newton import metodo_newton_raphson
from .metodos.newton_modificado import metodo_newton_modificado

def index(request):
    return render(request, 'raiz/index.html')

def resultado(request):
    if request.method == 'POST':
        metodo = request.POST['metodo']
        expresion = request.POST['funcion']
        f_expr = sp.sympify(expresion)
        iteraciones = []
        raiz = None
        error = None

        try:
            if metodo == 'biseccion':
                a = float(request.POST['a'])
                b = float(request.POST['b'])
                tol = float(request.POST['tolerancia'])
                max_iter = int(request.POST['iteraciones'])
                iteraciones, raiz = metodo_biseccion(f_expr, a, b, tol, max_iter)
            elif metodo == 'newton':
                x0 = float(request.POST['x0'])
                tol = float(request.POST['tolerancia'])
                max_iter = int(request.POST['iteraciones'])
                iteraciones, raiz = metodo_newton_raphson(f_expr, x0, tol, max_iter)
            elif metodo == 'newton_modificado':
                x0 = float(request.POST['x0'])
                tol = float(request.POST['tolerancia'])
                max_iter = int(request.POST['iteraciones'])
                iteraciones, raiz = metodo_newton_modificado(f_expr, x0, tol, max_iter)
        except Exception as e:
            return render(request, 'raiz/index.html', {'error': str(e)})

        # Generar gráfica
        # Generar gráfica personalizada
        x = sp.Symbol('x')
        f_lambd = sp.lambdify(x, f_expr, modules=['numpy'])
        x_vals = np.linspace(float(raiz) - 5, float(raiz) + 5, 400)
        y_vals = f_lambd(x_vals)

        # Crear figura con fondo gris claro
        fig, ax = plt.subplots(figsize=(6, 4))
        ax.set_facecolor('#d9d9d9')

        ax.plot(x_vals, y_vals, label=str(expresion), color='blue', linewidth=2)
        ax.axhline(0, color='black', linewidth=0.8, linestyle='--')
        ax.axvline(float(raiz), color='red', linestyle='--', label=f'Raíz ≈ {raiz:.5f}')

        ax.set_xlabel('x', color='black')
        ax.set_ylabel('f(x)', color='black')
        ax.spines['bottom'].set_color('black')
        ax.spines['left'].set_color('black')
        ax.tick_params(colors='black')

        ax.legend(facecolor='#d9d9d9', edgecolor='black', labelcolor='black')

        static_path = os.path.join('raiz', 'static', 'raiz', 'plot.png')
        plt.tight_layout()
        plt.savefig(static_path, dpi=100, facecolor='#d9d9d9')
        plt.close()


        return render(request, 'raiz/resultado.html', {
            'iteraciones': iteraciones,
            'raiz': raiz,
            'metodo': metodo,
            'funcion': expresion
        })

    return render(request, 'raiz/index.html')
