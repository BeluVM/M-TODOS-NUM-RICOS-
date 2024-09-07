import math

# Constante de Stefan-Boltzmann
sigma = 5.67e-8

# Datos del problema (valores y errores)
A = 0.15  # Área en m²
delta_A = 0.01  # Error en área

e = 0.90  # Emisividad
delta_e = 0.05  # Error en emisividad

T = 650  # Temperatura en K
delta_T = 20  # Error en temperatura

# Cálculo del valor de H
H = A * e * sigma * T**4

# Cálculo del error en H usando la propagación de errores
relative_error_A = (delta_A / A) ** 2
relative_error_e = (delta_e / e) ** 2
relative_error_T = (4 * (delta_T / T)) ** 2  # T^4, así que el error se multiplica por 4

# Error relativo total
relative_error_H = math.sqrt(relative_error_A + relative_error_e + relative_error_T)

# Error absoluto en H
delta_H = relative_error_H * H

# Mostrar resultados
print("Valor de H:", H)
print("Error en H:", delta_H)
print("Intervalo de confianza para H:", H - delta_H, "a", H + delta_H)
