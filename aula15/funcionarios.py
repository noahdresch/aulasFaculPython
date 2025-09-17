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
