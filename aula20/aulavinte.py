import tensorflow as tf
mnist = tf.keras.datasets.mnist

# Carrega o conjunto de dados MNIST, que consiste em imagens de dígitos escritos à mão (0 a 9).

(x_train, y_train), (x_test, y_test) = mnist.load_data()
x_train, x_test = x_train / 255.0, x_test / 255.0

# Normaliza os valores dos pixels das imagens para o intervalo [0, 1]. Isso ajuda no treinamento da rede neural.

model = tf.keras.models.Sequential([
    tf.keras.layers.Flatten(input_shape=(28, 28)),
    tf.keras.layers.Dense(128, activation='relu'),
    tf.keras.layers.Dropout(0.2),
    tf.keras.layers.Dense(10, activation='softmax')
])

# O modelo é sequencial e consiste em três camadas:
# Flatten: Transforma a matriz 2D das imagens (28x28 pixels) em um vetor unidimensional.
# Dense: Camada totalmente conectada com 128 neurônios e ativação ReLU.
# Dropout: Reduz o overfitting, desativando aleatoriamente 20% dos neurônios durante o treinamento.
# Dense: Camada de saída com 10 neurônios (um para cada dígito) e ativação softmax.

model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])

# Compila o modelo com o otimizador Adam,
# a função de perda entropia cruzada categórica esparsa (apropriada para rótulos categóricos) e a métrica de acurácia.

model.fit(x_train, y_train, epochs=5)
model.evaluate(x_test, y_test)