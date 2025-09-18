import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
import matplotlib.pyplot as plt

# Dados de exemplo
X_train = tf.constant([[1.0], [2.0], [3.0], [4.0]])
y_train = tf.constant([[2.0], [4.0], [6.0], [8.0]])

# Definimos os dados de exemplo X_train (entradas) e y_train (saídas desejadas) para treinar o modelo.
# No exemplo, estamos usando pares de entrada e saída que representam uma relação linear simples. (o dobro das entradas).


# Modelo de Regressão Linear Simples
model = Sequential()
model.add(Dense(units=1, input_shape=(1,)))
model.compile(optimizer='sgd', loss='mean_squared_error')

# Definimos o modelo de Regressão Linear Simples usando a API Keras Sequential.
# O modelo consiste em uma única camada densa (ou totalmente conectada) com um neurônio (ou unidade) e uma entrada.
# Estamos usando a função de perda (loss) de erro quadrático médio (mean squared error - 'mean_squared_error') e
# o otimizador 'sgd' (descida de gradiente estocástica



# Treinamento do modelo
history = model.fit(X_train, y_train, epochs=1000, verbose=0)

# Nesta seção, treinamos o modelo usando os dados de exemplo.
# Executamos 1000 épocas de treinamento (epochs) e armazenamos o histórico do treinamento em history.
# O argumento verbose=0 faz com que o treinamento seja executado em modo silencioso, sem exibir informações de progresso.


# Previsão
X_new = tf.constant([[5.0]])
prediction = model.predict(X_new)
print("Predição:", prediction[0][0])

# Aqui, fazemos uma previsão usando o modelo treinado.
# Informamos uma nova entrada X_new (5.0) e calculamos a previsão. O resultado é impresso na tela.


# Plotar os resultados
plt.plot(history.history['loss'])
plt.title('Model Loss Over Training')
plt.xlabel('Epoch')
plt.ylabel('Loss')
plt.show()

# Por fim, plotamos a perda (loss) do modelo ao longo do treinamento. Usamos history.history['loss'] para obter a lista das perdas em cada época.
# Configuramos o título e rótulos dos eixos e exibimos o gráfico com plt.show().
# Isso nos permite visualizar como a perda do modelo diminuiu durante o treinamento, o que é uma indicação do aprendizado do modelo.