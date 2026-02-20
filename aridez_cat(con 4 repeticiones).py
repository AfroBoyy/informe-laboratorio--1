contador= 0
while contador <4:
    T=float(input("ingrese la temperatura media anual: "))
    P=float(input("ingrese la precipitacion media anual: "))
    while T> -10:
     I= P/(T+10)
     if 0 <= I <5:
      print("LA ZONA ES *DESERTICA* ADEMAS EL INDICE DE ARIDEZ ES: ", I)
      break 
     elif 5 <= I <10:
      print("LA ZONA ES *SEMIARIDA* ADEMAS EL INDICE DE ARIDEZ ES: ", I)
      break
     elif 10 <= I <20:
      print("LA ZONA ES *ARIDA/SEMIARIDA SUBTERRANEA* ADEMAS EL INDICE DE ARIDEZ ES: ", I)
      break
     elif 20 <= I <30:
      print("LA ZONA ES *SUBHUMEDA* ADEMAS EL INDICE DE ARIDEZ ES: ", I)
      break
     elif 30 <= I <60:
      print("LA ZONA ES *HUMEDA* ADEMAS EL INDICE DE ARIDEZ ES: ", I)
      break
     elif I >=60:
      print("LA ZONA ES *PERHUMEDA* ADEMAS EL INDICE DE ARIDEZ ES: ", I)
     break
    contador +=1
#0-5: Zona desértica.
#5-10: Zona semiárida.
#10-20: Zona árida/semiárida mediterránea.
#20-30: Zona subhúmeda.
#30-60: Zona húmeda.
#> 60: Zona perhúmeda.