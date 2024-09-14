def calcular_temperatura_promedio(ciudades_temperaturas):
    """
    Calcula la temperatura promedio para cada ciudad durante un período de semanas.

    Parámetros:
    ciudades_temperaturas (dict): Un diccionario donde:
        - La clave es el nombre de la ciudad (str).
        - El valor es una lista de listas, donde cada sublista representa las temperaturas diarias
          de una semana. Ejemplo: {'Madrid': [[30, 32, 31], [28, 27, 29]]}

    Retorna:
    dict: Un diccionario con:
        - Claves (str): Los nombres de las ciudades.
        - Valores (float): La temperatura promedio de cada ciudad redondeada a dos decimales.
    """

    # Diccionario para almacenar los promedios por ciudad
    promedios = {}

    # Verificar que el parámetro sea un diccionario
    if not isinstance(ciudades_temperaturas, dict):
        raise ValueError("El parámetro debe ser un diccionario con los datos de las ciudades.")

    # Iteramos sobre cada ciudad y sus respectivas temperaturas semanales
    for ciudad, semanas in ciudades_temperaturas.items():
        # Verificar que el valor asociado a la ciudad sea una lista de listas (cada lista es una semana)
        if not isinstance(semanas, list) or not all(isinstance(semana, list) for semana in semanas):
            raise ValueError(f"Los datos de temperatura para la ciudad {ciudad} deben ser una lista de listas.")

        # Variables para acumular el total de temperaturas y el número de días
        total_temperaturas = 0
        total_dias = 0

        # Iterar sobre las semanas de la ciudad
        for semana in semanas:
            # Asegurarse de que todas las temperaturas en la semana sean numéricas (int o float)
            if not all(isinstance(temperatura, (int, float)) for temperatura in semana):
                raise ValueError(f"Todas las temperaturas en los datos de la ciudad {ciudad} deben ser números.")

            # Sumar las temperaturas de la semana actual
            total_temperaturas += sum(semana)
            # Contar el número de días en la semana (tamaño de la lista)
            total_dias += len(semana)

        # Si no hay días registrados, el promedio es 0 para evitar la división por cero
        if total_dias == 0:
            promedio = 0
        else:
            # Calcular el promedio dividiendo la suma total de temperaturas entre el número total de días
            promedio = total_temperaturas / total_dias

        # Almacenar el promedio de la ciudad en el diccionario, redondeado a dos decimales
        promedios[ciudad] = round(promedio, 2)

    return promedios


# Ejemplo de uso
ciudades_temperaturas = {
    'Madrid': [[30, 32, 33, 29, 28, 31, 30], [28, 27, 26, 25, 29, 30, 31]],
    'Barcelona': [[25, 27, 26, 24, 23, 22, 21], [20, 21, 22, 23, 24, 25, 26]],
    'Sevilla': [[35, 36, 37, 35, 34, 33, 32], [34, 33, 32, 31, 30, 29, 28]],
    'Granada': [[], []]  # Ejemplo con semanas vacías
}

# Llamada a la función
promedios = calcular_temperatura_promedio(ciudades_temperaturas)
print(promedios)
