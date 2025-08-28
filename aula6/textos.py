texto = "Explorando a diversidade de linguagens de programação com Python."

# descobrindo tamanho do texto
print(f"Tamanho do texto = {len(texto)}")

# pedindo se existe a palavra "Python" dentro do texto, se tiver "python" retorna falso
print(f"Python in texto = {'Python' in texto}")

# quantidade de letra "e" no texto
print(f"Quantidade de e no texto = {texto.count('e')}")

# 5 primeiras letras
print(f"As 5 primeiras letras são: {texto[:5]}")

#pegando ponto especifico dentro do texto
texto[64]