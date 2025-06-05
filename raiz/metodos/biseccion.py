import sympy as sp

def metodo_biseccion(f_expr, a, b, tol, max_iter):
    x = sp.Symbol('x')
    f = sp.lambdify(x, f_expr, 'numpy')
    iteraciones = []
    
    if f(a) * f(b) >= 0:
        raise ValueError("f(a) y f(b) deben tener signos opuestos")

    for i in range(1, max_iter + 1):
        c = (a + b) / 2
        fc = f(c)
        error = abs(b - a) / 2

        iteraciones.append({'iter': i, 'a': a, 'b': b, 'c': c, 'f(c)': fc, 'error': error})

        if abs(fc) < tol or error < tol:
            break

        if f(a) * fc < 0:
            b = c
        else:
            a = c

    return iteraciones, c
