from IPython.display import HTML
html_code = """
<!DOCTYPE html>
<html lang="en">
<head>
    <!-- Definindo a codificação e a viewport para dispositivos móveis -->
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Meu Perfil</title>
</head>
<body style="font-family: Arial, sans-serif; background-color: #f3f8f8; margin: 0; padding: 0;">

    <!-- Cabeçalho da Página -->
    <header style="text-align: center; background-color: #3498db; color: #fff; padding: 20px;">
        <!-- Título principal -->
        <h1 style="margin: 0;">Noah Dresch</h1>
        <!-- Descrição -->
        <p style="margin: 5px 0;">Desenvolvedor Web</p>
    </header>

    <!-- Seção de Informações Pessoais -->
    <section style="margin: 20px; text-align: center;">
        <!-- Imagem com estilos -->
        <img src="sua_foto.jpg" alt="Sua Foto" style="border-radius: 50%; margin-bottom: 20px;">
        <!-- Informações pessoais -->
        <div style="max-width: 400px; margin: 0 auto;">
            <p><b>Idade:</b> 21</p>
            <p><b>País:</b> Brasil</p>
            <p><b>Interesses:</b> Web Development, Programação, etc.</p>
        </div>
    </section>

    <!-- Seção de Habilidades -->
    <section style="margin: 20px; text-align: center;">
        <!-- Título da seção -->
        <h2>Habilidades</h2>
        <!-- Lista de habilidades -->
        <ul style="list-style: none; padding: 0;">
            <li><b>Linguagens:</b> Python, HTML, CSS, JavaScript</li>
            <li><b>Ferramentas:</b> Git, VS Code</li>
        </ul>
    </section>

    <!-- Seção de Projeto Recente -->
    <section style="margin: 20px; text-align: center;">
        <!-- Título do projeto recente -->
        <h2>Projeto Recente</h2>
        <!-- Descrição do projeto -->
        <p>Trabalhando em um site pessoal para mostrar meu portfólio.</p>
    </section>

    <!-- Rodapé da Página -->
    <footer style="text-align: center; margin-top: 20px;">
        <!-- Link para o LinkedIn -->
        <a href="https://www.linkedin.com/in/noah-dresch/" target="_blank" style="margin: 0 10px; color: #3498db; text-decoration: none;">LinkedIn</a>
    </footer>
</body>
</html>

"""
# Exibindo a página HTML
HTML(html_code)