#Nombre: Erick Simbaña
#Grupo: GR1S1

#importacion de librerias

import matplotlib.pyplot as plt
import numpy as np
from math import log

#Desarrollo

# Datos de ejemplo para algunos materiales (coeficiente de fricción y rugosidad)
materiales = {
    "acero": {"coef_friccion": 0.02, "rugosidad": 0.000045},
    "cobre": {"coef_friccion": 0.012, "rugosidad": 0.000005},
    "plastico": {"coef_friccion": 0.006, "rugosidad": 0.00002},
    "aluminio": {"coef_friccion": 0.015, "rugosidad": 0.000035},
    "bronce": {"coef_friccion": 0.02, "rugosidad": 0.00005},
    "laton": {"coef_friccion": 0.016, "rugosidad": 0.000027},
    "plomo": {"coef_friccion": 0.018, "rugosidad": 0.0005},
    "hormigon": {"coef_friccion": 0.01, "rugosidad": 0.002},
    "polipropileno": {"coef_friccion": 0.01, "rugosidad": 0.0001},
    "poliester": {"coef_friccion": 0.01, "rugosidad": 0.0002},
    "pvc": {"coef_friccion": 0.008, "rugosidad": 0.000007},
    "termoplastico": {"coef_friccion": 0.007, "rugosidad": 0.00004}
}

#Definicion de formulas y valores a usar.

def flujo_laminar_turbulento(velocidad, diametro, viscosidad):
    # Cálculo del número de Reynolds
    reynolds = (velocidad * diametro) / viscosidad
    
    if reynolds < 2000:
        return "Laminar"
    else:
        return "Turbulento"

def calcular_perdidas(material_elegido, diametro, longitud, velocidad, densidad, viscosidad):
    coef_friccion = materiales[material_elegido]["coef_friccion"]
    rugosidad = materiales[material_elegido]["rugosidad"]
    
    # Modificamos ligeramente la rugosidad para cada material
    rugosidad_modificada = rugosidad + (0.000001 if material_elegido == "material1" else 0.000002)

    # Cálculo de las pérdidas por fricción
    reynolds = (velocidad * diametro) / viscosidad
    if reynolds < 2000:
        factor_friccion = 16 / reynolds
    else:
        factor_friccion = (1 / (-1.8 * log((6.9 / reynolds) + ((rugosidad_modificada / (3.7 * diametro)) ** 1.11)))) ** 2

    perdidas_friccion = factor_friccion * (longitud / diametro) * ((densidad * velocidad ** 2) / 2)

    return perdidas_friccion

def generar_grafica_comparativa(material1, material2, diametro, longitud, velocidad, densidad, viscosidad):
    velocidades = np.linspace(0.1, 2, 1000)  # Mayor cantidad de puntos para curva más suave
    perdidas_materiales = {material: [] for material in [material1, material2]}

    for velocidad_actual in velocidades:
        for material in [material1, material2]:
            perdidas = calcular_perdidas(material, diametro, longitud, velocidad_actual, densidad, viscosidad)
            perdidas_materiales[material].append(perdidas)

#Creacion de grafico comparativo.

    # Gráfico comparativo de pérdidas por fricción
    plt.figure(figsize=(10, 6))
    plt.plot(velocidades, perdidas_materiales[material1], label=f"{material1.capitalize()} - Pérdidas")
    plt.plot(velocidades, perdidas_materiales[material2], label=f"{material2.capitalize()} - Pérdidas")
    plt.xlabel("Velocidad (m/s)")
    plt.ylabel("Pérdidas por fricción (N/m^2)")
    plt.title("Comparación de Pérdidas por Fricción en Tuberías")
    plt.legend()
    plt.grid(True)
    plt.show()

def obtener_datos_usuario():
    print("Ingrese los siguientes datos:")
    material1_elegido = input("Material de la tubería 1 (acero, cobre, plastico, aluminio, bronce, laton, plomo, hormigon, polipropileno, poliester_reforzado_con_fibra_de_vidrio, pvc, termoplastico_polietileno_de_alta_densidad): ").lower()
    material2_elegido = input("Material de la tubería 2 (acero, cobre, plastico, aluminio, bronce, laton, plomo, hormigon, polipropileno, poliester_reforzado_con_fibra_de_vidrio, pvc, termoplastico_polietileno_de_alta_densidad): ").lower()
    diametro_tuberia = float(input("Diámetro de la tubería en metros: "))
    longitud_tuberia = float(input("Longitud de la tubería en metros: "))
    velocidad_flujo = float(input("Velocidad de flujo en m/s: "))
    densidad_fluido = float(input("Densidad del fluido en kg/m^3: "))
    viscosidad_fluido = float(input("Viscosidad del fluido en Pa·s: "))

    return material1_elegido, material2_elegido, diametro_tuberia, longitud_tuberia, velocidad_flujo, densidad_fluido, viscosidad_fluido

if __name__ == "__main__":
    print("Programa para calcular flujo laminar o turbulento y pérdidas en una tubería.")


#Datos para interfaz inicial del usuario

    # Datos del usuario
    material1_elegido, material2_elegido, diametro_tuberia, longitud_tuberia, velocidad_flujo, densidad_fluido, viscosidad_fluido = obtener_datos_usuario()

    # Verificación del flujo (laminar o turbulento)
    flujo1 = flujo_laminar_turbulento(velocidad_flujo, diametro_tuberia, viscosidad_fluido)
    flujo2 = flujo_laminar_turbulento(velocidad_flujo, diametro_tuberia, viscosidad_fluido)

    # Cálculo de pérdidas
    perdidas1 = calcular_perdidas(material1_elegido, diametro_tuberia, longitud_tuberia,
                                  velocidad_flujo, densidad_fluido, viscosidad_fluido)
    perdidas2 = calcular_perdidas(material2_elegido, diametro_tuberia, longitud_tuberia,
                                  velocidad_flujo, densidad_fluido, viscosidad_fluido)
# Conclusiones

    # Resultados
    print("\nResultados Tubería 1:")
    print(f"Material: {material1_elegido.capitalize()}")
    print(f"Flujo: {flujo1}")
    print(f"Pérdidas por fricción: {perdidas1} N/m^2")

    print("\nResultados Tubería 2:")
    print(f"Material: {material2_elegido.capitalize()}")
    print(f"Flujo: {flujo2}")
    print(f"Pérdidas por fricción: {perdidas2} N/m^2")

    # Generación de gráfica comparativa
    generar_grafica_comparativa(material1_elegido, material2_elegido, diametro_tuberia, longitud_tuberia,
                                velocidad_flujo, densidad_fluido, viscosidad_fluido)

   
