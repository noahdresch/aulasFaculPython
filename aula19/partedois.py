import tensorflow as tf
from tensorflow.keras.layers import Input, Dense
from tensorflow.keras.models import Model

# Dados de exemplo
X_unsupervised = tf.constant([[1.0, 2.0], [2.0, 3.0], [3.0, 4.0], [4.0, 5.0]])

# Aqui, você define os dados de exemplo que serão usados para treinar e testar o modelo autoencoder.
# Esses dados são armazenados na variável X_unsupervised como um tensor TensorFlow.
# Cada linha representa um exemplo com duas características.


# Modelo Autoencoder Simples
input_layer = Input(shape=(2,))
encoded = Dense(units=1)(input_layer)
decoded = Dense(units=2)(encoded)

autoencoder = Model(inputs=input_layer, outputs=decoded)
autoencoder.compile(optimizer='adam', loss='mean_squared_error')


# Define o modelo autoencoder simples usando a API Keras:

# input_layer = Input(shape=(2,)): Define uma camada de entrada com duas características.
# encoded = Dense(units=1)(input_layer): Define uma camada densa (totalmente conectada) com uma unidade (neurônio) que representa a camada codificada do autoencoder.
# decoded = Dense(units=2)(encoded): Define uma camada densa com duas unidades que representa a camada decodificada do autoencoder.
# autoencoder = Model(inputs=input_layer, outputs=decoded): Cria o modelo autoencoder, especificando as camadas de entrada e saída.
# autoencoder.compile(optimizer='adam', loss='mean_squared_error'): Compila o modelo, definindo o otimizador Adam e a função de perda como erro quadrático médio.



# Treinamento do modelo não supervisionado
autoencoder.fit(X_unsupervised, X_unsupervised, epochs=1000, verbose=0)

# Nesta parte, você treina o modelo autoencoder usando os dados de exemplo X_unsupervised.
# O autoencoder é treinado para reconstruir os dados de entrada a partir de sua representação codificada.
# O treinamento é executado por 1000 épocas (epochs) e é silencioso (verbose=0), o que significa que não exibirá informações de progresso.


# Previsão
prediction_unsupervised = autoencoder.predict(X_unsupervised)
print("Predição Não Supervisionada:", prediction_unsupervised)

# Reduzir a dimensionalidade de imagens mantendo a maior parte das informações importantes.