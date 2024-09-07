import sympy as sp

# Definir la variable simbólica
x = sp.Symbol('x')

# Definir la función f(x)
f = 25*x**3 - 6*x**2 + 7*x - 88

# Punto base y punto de evaluación
x_base = 1
x_eval = 3

# Derivadas de la función
f_prime = sp.diff(f, x)  # Primera derivada
f_double_prime = sp.diff(f_prime, x)  # Segunda derivada
f_triple_prime = sp.diff(f_double_prime, x)  # Tercera derivada

# Evaluar f(x) y sus derivadas en x = 1
f_base = f.subs(x, x_base)
f_prime_base = f_prime.subs(x, x_base)
f_double_prime_base = f_double_prime.subs(x, x_base)
f_triple_prime_base = f_triple_prime.subs(x, x_base)

# Calcular la expansión de Taylor de cero hasta tercer orden
taylor_approx_0 = f_base
taylor_approx_1 = f_base + f_prime_base * (x_eval - x_base)
taylor_approx_2 = taylor_approx_1 + (f_double_prime_base / 2) * (x_eval - x_base)**2
taylor_approx_3 = taylor_approx_2 + (f_triple_prime_base / 6) * (x_eval - x_base)**3

# Calcular el valor exacto de f(3)
f_exact = f.subs(x, x_eval)

# Calcular el error relativo porcentual
error_0 = abs((f_exact - taylor_approx_0) / f_exact) * 100
error_1 = abs((f_exact - taylor_approx_1) / f_exact) * 100
error_2 = abs((f_exact - taylor_approx_2) / f_exact) * 100
error_3 = abs((f_exact - taylor_approx_3) / f_exact) * 100

# Mostrar resultados
print("Aproximación de orden 0:", taylor_approx_0)
print("Aproximación de orden 1:", taylor_approx_1)
print("Aproximación de orden 2:", taylor_approx_2)
print("Aproximación de orden 3:", taylor_approx_3)
print("Valor exacto de f(3):", f_exact)

print("Error relativo porcentual de orden 0:", error_0)
print("Error relativo porcentual de orden 1:", error_1)
print("Error relativo porcentual de orden 2:", error_2)
print("Error relativo porcentual de orden 3:", error_3)
