def interpretar_indice(I):

    inferior, superior = limites_semiarida()

    if inferior <= I < superior:
        print("El municipio está dentro del rango SEMIÁRIDO")
    elif I < inferior:
        print("El municipio está por debajo del rango (más seco)")
    else:
        print("El municipio está por encima del rango (más húmedo)")