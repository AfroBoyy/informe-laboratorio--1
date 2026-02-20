# funciones

def calcular_aridez(P, T):
    I = P / (T + 10)
    return I


def categorizar_clima(I):

    if 0 <= I < 5:
        return "desertica"
    elif 5 <= I < 10:
        return "semiarida"
    elif 10 <= I < 20:
        return "arida/arida subterranea"
    elif 20 <= I < 30:
        return "subhumeda"
    elif 30 <= I < 60:
        return "humeda"
    else:
        return "perhumeda"


def limites_semiarida():
    return 5, 10


def interpretar_indice(I):

    inferior, superior = limites_semiarida()

    if inferior <= I < superior:
        print("El municipio está dentro del rango SEMIÁRIDO")
    elif I < inferior:
        print("El municipio está por debajo del rango (más seco)")
    else:
        print("El municipio está por encima del rango (más húmedo)")


def calcular_porcentajes(categoria):

    total = len(categoria)

    print("\nPORCENTAJES:")

    print("Desertica:", categoria.count("desertica") * 100 / total, "%")
    print("Semiarida:", categoria.count("semiarida") * 100 / total, "%")
    print("Arida/arida subterranea:", categoria.count("arida/arida subterranea") * 100 / total, "%")
    print("Subhumeda:", categoria.count("subhumeda") * 100 / total, "%")
    print("Humeda:", categoria.count("humeda") * 100 / total, "%")
    print("Perhumeda:", categoria.count("perhumeda") * 100 / total, "%")


# pRincipal

categoria = []
contador = 0

while contador < 4:

    valoreso = input("Ingrese precipitacion y temperatura separadas por coma: ")
    valor = valoreso.split(",")

    P = float(valor[0])
    T = float(valor[1])

    if T > -10:

        I = calcular_aridez(P, T)

        categorias = categorizar_clima(I)

        print("La zona es:", categorias)
        print("Indice de aridez:", I)

        interpretar_indice(I)

        categoria.append(categorias)

        contador += 1

print("Lista final:", categoria)

calcular_porcentajes(categoria)