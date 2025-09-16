import pandas as pd

dados = {
    'Produto':['A','B','C'],
    'qtde_vendida':[33,50,45]
    }
df = pd.DataFrame(dados)

# Gráfico de barras
df.plot(x='Produto', y='qtde_vendida', kind='bar')

# Gráfico de pizza
df.plot(x='Produto', y='qtde_vendida', kind='pie')