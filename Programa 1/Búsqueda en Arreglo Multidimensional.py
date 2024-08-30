# Definimos una matriz bidimensional de 3x3
matrix = [
    [5, 3, 8],
    [4, 7, 1],
    [9, 2, 6]
]

# Definimos la función para buscar un valor en la matriz
def find_value(matrix, value):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] == value:
                return (i, j)
    return None

# Valor a buscar en la matriz
value_to_find = 7

# Buscar el valor en la matriz
position = find_value(matrix, value_to_find)

# Mostrar el resultado
if position:
    print(f"El valor {value_to_find} se encontró en la posición {position}.")
else:
    print(f"El valor {value_to_find} no se encontró en la matriz.")
