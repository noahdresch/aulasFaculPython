# Criando uma página HTML usando Python
html_code = """
<!DOCTYPE html>
<html>
<head>
    <title>Exemplo de Front-end com Python</title>
</head>
<body>
    <h1>Olá, mundo!</h1>
    <p>Esta é uma página web criada usando Python no Google Colab.</p>
</body>
</html>
"""

with open("pagina.html", "w", encoding="utf-8") as f:
    f.write(html_code)
print("Arquivo 'pagina.html' criado com sucesso. Abra-o em seu navegador.")