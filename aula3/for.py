for x in range(5): #lembre-se que o range começa em 0
  print(x)

for y in range(2, 7): #observe que aqui o 7 não entra no looping
  print(y)

for z in range(1, 11, 2): #observe que aqui o 11 não entra no looping
  print(z)

for numero in range(1, 11):
  if numero % 2 == 0:
    print("O primeiro número par encontrado é: ", numero)
    break
  
for numero in range(1, 11):
  if numero == 5:
    continue
  print(numero)