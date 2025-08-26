# Definindo uma função chamada "e_par"
def e_par(numero):
  #operador módulo %
  if numero % 2 == 0:
    return True
  else:
    return False
  
numero = 14
if e_par(numero):
  print(f"{numero} é um par.")
else:
  print(f"{numero} não é um número par.")