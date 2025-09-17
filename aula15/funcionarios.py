# Passo 1: Conectar ao banco de dados SQLite (ou criá-lo se não existir)
import sqlite3
conn = sqlite3.connect("funcionarios.db")

# Passo 2: Criar a tabela de funcionários
cursor = conn.cursor()
cursor.execute("""
CREATE TABLE IF NOT EXISTS funcionarios (
    id INTEGER PRIMARY KEY,
    nome TEXT,
    cargo TEXT,
    salario REAL
)
""")

# Passo 3: Inserir um novo funcionário na tabela
#novo_funcionario = (2, "Maria", "Gerente", 10000.00)
novo_funcionario = (1, "Joao", "Analista", 5000.00)
cursor.execute("INSERT INTO funcionarios VALUES (?, ?, ?, ?)", novo_funcionario)
conn.commit()
