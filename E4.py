import numpy as np

# Datos del problema
B = 20  # Ancho en metros
H = 0.3  # Profundidad en metros
n = 0.03  # Coeficiente de rugosidad
S = 0.0003  # Pendiente

# Fórmula de Manning
def flujo_manning(B, H, n, S):
    A = B * H  # Área transversal
    P = B + 2 * H  # Perímetro mojado
    R = A / P  # Radio hidráulico
    Q = (1/n) * (R**(2/3)) * (A**(5/3)) * np.sqrt(S)
    return Q

# Flujo calculado con valores nominales
Q_nominal = flujo_manning(B, H, n, S)
print(f"Flujo nominal (Q): {Q_nominal:.5f} m^3/s")

# Análisis de sensibilidad: variaciones en n y S
n_variation = [0.027, 0.033]
S_variation = [0.00027, 0.00033]

# Flujo con variaciones en n
for n_var in n_variation:
    Q_var_n = flujo_manning(B, H, n_var, S)
    print(f"Flujo con n = {n_var}: {Q_var_n:.5f} m^3/s")

# Flujo con variaciones en S
for S_var in S_variation:
    Q_var_S = flujo_manning(B, H, n, S_var)
    print(f"Flujo con S = {S_var}: {Q_var_S:.5f} m^3/s")
