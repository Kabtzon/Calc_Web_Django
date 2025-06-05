import sympy as sp

def metodo_newton_modificado(f_expr, x0, tol, max_iter):
    x = sp.Symbol('x')
    f = sp.lambdify(x, f_expr, 'numpy')
    df_expr = sp.diff(f_expr, x)
    d2f_expr = sp.diff(df_expr, x)
    df = sp.lambdify(x, df_expr, 'numpy')
    d2f = sp.lambdify(x, d2f_expr, 'numpy')
    
    iteraciones = []

    for i in range(1, max_iter + 1):
        fx = f(x0)
        dfx = df(x0)
        d2fx = d2f(x0)
        if dfx**2 - fx * d2fx == 0:
            raise ZeroDivisionError("División por cero en fórmula modificada")

        x1 = x0 - (fx * dfx) / (dfx**2 - fx * d2fx)
        error = abs(x1 - x0)

        iteraciones.append({'iter': i, 'x': x0, 'f(x)': fx, 'f\'(x)': dfx, 'f\'\'(x)': d2fx, 'error': error})

        if error < tol:
            break
        x0 = x1

    return iteraciones, x1
