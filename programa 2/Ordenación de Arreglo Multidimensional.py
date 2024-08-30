# Definimos la matriz 3x3
matriz = [
    [15, 8, 12],
    [9, 3, 7],
    [4, 16, 1]
]


def bubble_sort(fila):
    # Implementación del algoritmo de Bubble Sort
    n = len(fila)
    for i in range(n):
        for j in range(0, n - i - 1):
            if fila[j] > fila[j + 1]:
                fila[j], fila[j + 1] = fila[j + 1], fila[j]


def ordenar_fila(matriz, fila_index):
    # Ordena la fila especificada de la matriz
    if 0 <= fila_index < len(matriz):
        print(f"Matriz antes de ordenar la fila {fila_index}:")
        for fila in matriz:
            print(fila)

        bubble_sort(matriz[fila_index])

        print(f"\nMatriz después de ordenar la fila {fila_index}:")
        for fila in matriz:
            print(fila)
    else:
        print("Índice de fila fuera de rango.")


# Índice de la fila que queremos ordenar (por ejemplo, la fila 1)
fila_a_ordenar = 1

# Llamada a la función para ordenar la fila específica
ordenar_fila(matriz, fila_a_ordenar)
