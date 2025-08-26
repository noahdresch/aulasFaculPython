#Lista de filmes para classificação
filmes = ["Filme 1", "Filme 2", "Filme 3", "Filme 4", "Filme 5"]

filmes

#Lista de filmes para classificação
filmes = ["Filme 1", "Filme 2", "Filme 3", "Filme 4", "Filme 5"]

#Mensagens de boas-vindas
print("Bem-vindo à classificação de filmes!")
print("Você tem cinco filmes para classificar.")
print("Digite '0' a qualquer momento para parar.\n")

#Loop para interar sobre cada filme na lista
for filme in filmes:
  #Solicita a classificação ao usuário
  classificacao = input(f"Como você classificaria '{filme}' de 1 a 5? ( ou 0 para parar): ")

  #Verifica se o usuário deseja parar
  if classificacao == '0':
    print("Que pena que você não irá classificar mais os filmes.")
    break #Encerra o loop principal

    #Converte a classificação para um número inteiro
    classificacao = int(classificacao)

    #Verifica se a classificação está dentro do intervalo válido
    if classificacao < 1 or classificacao > 5:
      print("Por favor, digite uma classificação válida de 1 a 5")
    else:
      #Exibe a classificação e passa o próximo filme
      print(f"Você classificou '{filme}' com {classificacao} estrelas.\n")

#Mensagem de agradecimento ao finalizar
print("Obrigado por classificar os filmes!")