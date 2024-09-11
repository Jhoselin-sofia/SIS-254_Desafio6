import numpy as np

# Crear la matriz 'a' con los porcentajes de cada cantera
a = np.array([[0.52, 0.20, 0.25],
              [0.30, 0.50, 0.20],
              [0.18, 0.30, 0.55]])

# Crear el vector 'b' con los requerimientos de arena, grano fino y grano grueso
b = np.array([4800, 5810, 5690])

# Calcular la inversa de la matriz
a_inv = np.linalg.inv(a)

# Mostrar la inversa de la matriz
print("----------- INVERSA DE LA MATRIZ A: ----------")
print(a_inv)

# Calcular la solución usando la inversa de la matriz multiplicada por b
x_inv = a_inv @ b

# Mostrar el resultado de la multiplicación de la inversa con b
print("\n------- SOLUCION x=inv(a)*b ------------")
print(x_inv)

# Calcular la matriz identidad
mat_id =a @ a_inv 

#REDONDEAMOSS
mat_id_red = np.round(mat_id, 0).astype(int)

# Mostrar el resultado de la multiplicación de la inversa con b
print("\n------- MATRIZ IDENTIDAD ------------")
print(mat_id_red)
