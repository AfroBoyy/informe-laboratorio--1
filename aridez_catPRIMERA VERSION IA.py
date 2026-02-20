# aridez_cat.py
# Programa que calcula el Índice de Aridez de De Martonne
# y clasifica el clima según los rangos oficiales.

def calcular_indice(precipitacion, temperatura):
    return precipitacion / (temperatura + 10)

def clasificar_clima(indice):
    if indice < 5:
        return "Árido"
    elif indice < 10:
        return "Semidesértico"
    elif indice < 20:
        return "Semiárido mediterráneo"
    elif indice < 30:
        return "Subhúmedo"
    elif indice < 60:
        return "Húmedo"
    else:
        return "Perhúmedo"

def main():
    print("Cálculo del Índice de Aridez de De Martonne")
    P = float(input("Ingrese la precipitación anual (mm): "))
    T = float(input("Ingrese la temperatura media anual (°C): "))

    indice = calcular_indice(P, T)
    categoria = clasificar_clima(indice)

    print(f"\nÍndice de Aridez: {indice:.2f}")
    print(f"Categoría climática: {categoria}")

if __name__ == "__main__":
    main()
