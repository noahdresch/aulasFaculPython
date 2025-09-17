# Passo 1: Conectar ao banco de dados SQLite (ou criá-lo se não existir)
import sqlite3
conn = sqlite3.connect("funcionarios.db")