import sqlite3

# 1. Conectar ao banco de dados (ou criar um novo)
# usando a função connect do módulo sqlite3 para se conectar a um banco de dados SQLite
# chamado 'exemplo.db'. Se o banco de dados não existir, ele será criado automaticamente.
conn = sqlite3.connect("exemplo.db")

# 2. Criar um objeto cursor
# O cursor é usado para executar comandos SQL no banco de dados.
# Ele atua como uma espécie de ponteiro que percorre os resultados de consultas.
cursor = conn.cursor()

# 3. Definir o comando SQL para criar a tabela
# Define uma string create_table que contém um comando SQL para criar uma tabela chamada "Produtos".
# Esta tabela terá quatro colunas: id (chave primária), nome (texto), preco (número real) e estoque (número inteiro).
# IF NOT EXISTS garante que a tabela só será criada se ainda não existir
create_table = """
CREATE TABLE IF NOT EXISTS Produtos (
    id INTEGER PRIMARY KEY,
    nome TEXT NOT NULL,
    preco REAL NOT NULL,
    estoque INTEGER
);
"""

# 4. Executar o comando SQL para criar a tabela
# Usa o método execute do objeto cursor para executar o comando SQL definido anteriormente e criar a tabela no banco de dados.
cursor.execute(create_table)

# 5. Confirmar as alterações (commit)
# Após a execução bem-sucedida do comando SQL, usa o método commit no objeto de conexão (conn) para confirmar as alterações no banco de dados.
# Isso garante que as alterações sejam efetivamente aplicadas.
conn.commit()

# 6. Fechar a conexão com o banco de dados
# Finalmente, você usa o método close no objeto de conexão para encerrar a conexão com o banco de dados.
# É uma prática recomendada fechar a conexão após a conclusão das operações, para liberar recursos e evitar possíveis problemas de concorrência.
conn.close()

# adicionar produto
import sqlite3

# Conectando ao banco de dados
conn = sqlite3.connect("exemplo.db")
cursor = conn.cursor()

# Dados do novo produto
novo_produto = ("Camiseta", 19.99, 50)

# Comando SQL para inserir o novo produto na tabela
inserir_produto = "INSERT INTO Produtos (nome, preco, estoque) VALUES (?, ?, ?)"

# Executando o comando SQL para inserção
cursor.execute(inserir_produto, novo_produto)

# Confirmando as alterações
conn.commit()

# Fechando a conexão
conn.close()

# visualizar produto
import sqlite3

# Conectando ao banco de dados
conn = sqlite3.connect("exemplo.db")
cursor = conn.cursor()

# Comando SQL para selecionar todos os produtos
selecionar_produtos = "SELECT * FROM Produtos"

# Executando o comando SQL
cursor.execute(selecionar_produtos)

# Obtendo todos os registros e exibindo-os
produtos = cursor.fetchall()
for produto in produtos:
    print(produto)

# Fechando a conexão
conn.close()

# atualizar produto
import sqlite3

# Conectando ao banco de dados
conn = sqlite3.connect("exemplo.db")
cursor = conn.cursor()

# Novo preço e ID do produto a ser atualizado
novo_preco = 24.99
produto_id = 1  # Suponhamos que queremos atualizar o produto com ID 1

# Comando SQL para atualizar o preço do produto
atualizar_preco = "UPDATE Produtos SET preco = ? WHERE id = ?"

# Executando o comando SQL de atualização
cursor.execute(atualizar_preco, (novo_preco, produto_id))

# Confirmando as alterações
conn.commit()

# Fechando a conexão
conn.close()

import sqlite3

# CREATE (Criação da tabela e inserção de dados de exemplo)
conn = sqlite3.connect("contatos.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS Contatos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT,
    email TEXT,
    telefone TEXT
)
""")

dados_exemplo = [
    ("João", "joao@email.com", "123-456-7890"),
    ("Maria", "maria@email.com", "987-654-3210"),
    ("Carlos", "carlos@email.com", "555-555-5555")
]

cursor.executemany("INSERT INTO Contatos (nome, email, telefone) VALUES (?, ?, ?)", dados_exemplo)
conn.commit()

# READ (Leitura e exibição dos contatos)
cursor.execute("SELECT * FROM Contatos")
contatos = cursor.fetchall()
print("Contatos:")
for contato in contatos:
    print(contato)

# UPDATE (Atualização do número de telefone do contato com ID 2)
novo_telefone = "999-999-9999"
contato_id = 2
cursor.execute("UPDATE Contatos SET telefone = ? WHERE id = ?", (novo_telefone, contato_id))
conn.commit()

# DELETE (Exclusão do contato com ID 1)
contato_id_para_excluir = 1
cursor.execute("DELETE FROM Contatos WHERE id = ?", (contato_id_para_excluir,))
conn.commit()

# Fechando a conexão
conn.close()

