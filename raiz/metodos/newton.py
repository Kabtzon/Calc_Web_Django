import sympy as sp

def metodo_newton_raphson(f_expr, x0, tol, max_iter):
    x = sp.Symbol('x')
    f = sp.lambdify(x, f_expr, 'numpy')
    df_expr = sp.diff(f_expr, x)
    df = sp.lambdify(x, df_expr, 'numpy')
    
    iteraciones = []
    
    for i in range(1, max_iter + 1):
        fx = f(x0)
        dfx = df(x0)
        if dfx == 0:
            raise ZeroDivisionError("La derivada es cero")

        x1 = x0 - fx / dfx
        error = abs(x1 - x0)

        iteraciones.append({'iter': i, 'x': x0, 'f(x)': fx, 'f\'(x)': dfx, 'error': error})
        
        if error < tol:
            break
        x0 = x1

    return iteraciones, x1
