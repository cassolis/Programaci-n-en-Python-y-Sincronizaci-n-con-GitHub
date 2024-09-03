# Ejemplo de matriz 3D para temperaturas en 3 ciudades, durante 2 semanas, para 7 días de la semana
temperaturas = [
    [  # Ciudad 1
        [25, 26, 24, 23, 22, 24, 26],  # Semana 1
        [27, 26, 25, 24, 26, 27, 28]  # Semana 2
    ],
    [  # Ciudad 2
        [15, 16, 14, 13, 12, 14, 16],  # Semana 1
        [17, 16, 15, 14, 16, 17, 18]  # Semana 2
    ],
    [  # Ciudad 3
        [30, 31, 29, 28, 27, 29, 31],  # Semana 1
        [32, 31, 30, 29, 31, 32, 33]  # Semana 2
    ]
]

# Iterar sobre las ciudades
for i, ciudad in enumerate(temperaturas):
    print(f"Ciudad {i + 1}:")

    # Iterar sobre las semanas
    for j, semana in enumerate(ciudad):
        suma_temperaturas = 0

        # Iterar sobre los días de la semana
        for dia in semana:
            suma_temperaturas += dia

        # Calcular el promedio de la semana
        promedio = suma_temperaturas / len(semana)
        print(f"  Semana {j + 1} - Promedio de temperatura: {promedio:.2f}°C")
