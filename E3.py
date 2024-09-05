import math

# Definimos el valor de x_0 y el punto en el que queremos aproximar f(2.5)
x0 = 1
x = 2.5

# Valor exacto de ln(2.5)
valor_exacto = math.log(x)

# Serie de Taylor de ln(x) en torno a x0 = 1 hasta el cuarto orden
def taylor_ln_4th_order(x, x0):
    # Expansión de la serie de Taylor
    term_0 = math.log(x0)
    term_1 = (1/x0) * (x - x0)
    term_2 = -(1/(2 * x0**2)) * (x - x0)**2
    term_3 = (1/(3 * x0**3)) * (x - x0)**3
    term_4 = -(1/(4 * x0**4)) * (x - x0)**4
    return term_0 + term_1 + term_2 + term_3 + term_4

# Calculamos la aproximación usando la serie de Taylor de cuarto orden
aproximacion = taylor_ln_4th_order(x, x0)

# Cálculo del error relativo porcentual verdadero
error_relativo_porcentual = abs((valor_exacto - aproximacion) / valor_exacto) * 100

# Resultados
print(f"Aproximación de ln(2.5) usando la serie de Taylor de cuarto orden: {aproximacion}")
print(f"Valor exacto de ln(2.5): {valor_exacto}")
print(f"Error relativo porcentual verdadero: {error_relativo_porcentual:.5f}%")

