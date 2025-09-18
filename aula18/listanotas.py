def calcular_media(notas):
    assert len(notas) > 0, "A lista de notas não pode estar vazia"

    soma = sum(notas)
    media = soma / len(notas)
    return media

# Exemplo 1: Lista de notas válida
notas_validas = [8, 7, 9, 6, 8]
media = calcular_media(notas_validas)  # Isso funcionará corretamente
print(media)