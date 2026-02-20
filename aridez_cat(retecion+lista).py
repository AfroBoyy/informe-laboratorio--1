categorias=[]
contador= 0
while contador <4:
    valoreso=input("ingrese la precipitacion y temperatura respectivamente separadas por una coma : ")
    valor= valoreso.split(",")
    argumento=(float(valor[0]),float(valor[1]))
    P= argumento[0]
    T= argumento[1]
    while T> -10:
     I= P/(T+10)
     if  0 <= I  <5:
      categoria= "desertica"
      print("LA ZONA ES *DESERTICA* ADEMAS EL INDICE DE ARIDEZ ES: ", I)
      categorias.append(categoria)
      break 
     elif  5 <=  I <10:
      categoria= "semiarida"
      print("LA ZONA ES *SEMIARIDA* ADEMAS EL INDICE DE ARIDEZ ES: ", I)
      categorias.append(categoria)
      break
     elif  10 <=  I <20:
      categoria= "arida/arida subterranea"
      print("LA ZONA ES *ARIDA/SEMIARIDA SUBTERRANEA* ADEMAS EL INDICE DE ARIDEZ ES: ", I)
      categorias.append(categoria)
      break
     elif 20 <= I <30:
      categoria= "subhumeda"
      print("LA ZONA ES *SUBHUMEDA* ADEMAS EL INDICE DE ARIDEZ ES: ", I)
      categorias.append(categoria)
      break
     elif 30 <= I <60:
      categoria= "humeda" 
      print("LA ZONA ES *HUMEDA* ADEMAS EL INDICE DE ARIDEZ ES: ", I)
      categorias.append(categoria)
      break
     elif I >=60:
      categoria= "perhumeda"
      print("LA ZONA ES *PERHUMEDA* ADEMAS EL INDICE DE ARIDEZ ES: ", I)
      categorias.append(categoria)
      break
    contador +=1
print("la lista de las categorias aparecidads son", categorias)
#5-10: Zona semiárida.
#10-20: Zona árida/semiárida mediterránea.
#20-30: Zona subhúmeda.
#30-60: Zona húmeda.
#> 60: Zona perhúmeda.