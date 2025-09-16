import seaborn as sns
import matplotlib.pyplot as plt

sns.set(style="whitegrid")

df = sns.load_dataset("tips")

#total de gastos por periodo (almoco ou jantar)
plt.figure(figsize=(8, 5))
sns.barplot(x='time', y='total_bill', data=df, estimator=sum, ci=None, palette="Set2")
plt.xlabel('Período (Time)')
plt.ylabel('Total de Gastos')
plt.title('Total de Gastos por Período (Almoço ou Jantar)')
plt.show()

#media de gastos por periodo (almoco ou jantar)
plt.figure(figsize=(8, 5))
sns.barplot(x='time', y='total_bill', data=df)  # por padrão calcula a média
plt.xlabel('Período (Time)')
plt.ylabel('Média de Gastos')
plt.title('Média de Gastos por Período (Almoço ou Jantar)')
plt.show()

#media da gorjeta por periodo (almoco ou jantar)
#Cria um gráfico de barras com Seaborn para mostrar a média da gorjeta por período
plt.figure(figsize=(8, 5))
sns.barplot(x="time", y="total_bill", data=df, palette="Set3")
plt.xlabel("Período (Time)")
plt.ylabel("Média da Gorjeta")
plt.title("Média da Gorjeta por Período (Almoço ou Jantar)")
plt.show()