import tensorflow as tf
import gymnasium as gym

# Ambiente CartPole do Gymnasium
env = gym.make('CartPole-v1')

# Modelo Simples para Aprendizado por Reforço
model_reinforcement = tf.keras.Sequential([
    tf.keras.layers.Dense(24, activation='relu', input_shape=(env.observation_space.shape[0],)),
    tf.keras.layers.Dense(env.action_space.n, activation='linear')
])

model_reinforcement.compile(optimizer=tf.keras.optimizers.Adam(learning_rate=0.001), loss='mse')

# Treinamento por Reforço (exemplo fictício)
max_episodes = 1000 # Defina o número máximo de episódios
for episode in range(max_episodes):
    # Reinicializa o ambiente para um novo episódio
    state, info = env.reset() # Alteração aqui
    done = False

    while not done:
        # Escolhe uma ação aleatória do espaço de ação
        action = env.action_space.sample()

        # Executa a ação e obtém o próximo estado, recompensa e se o episódio terminou
        next_state, reward, done, _, info = env.step(action) # Alteração aqui

        # Calcula o alvo para a ação tomada
        target = reward + 0.95 * tf.reduce_max(model_reinforcement.predict(next_state.reshape(1, -1)))

        # Obtém o valor Q previsto para o estado atual
        target_f = model_reinforcement.predict(state.reshape(1, -1))

        # Atualiza o valor Q para a ação tomada com o novo alvo
        target_f[0][action] = target

        # Treina o modelo usando o par (estado, novo valor Q)
        model_reinforcement.fit(state.reshape(1, -1), target_f, epochs=1, verbose=0)

        # Atualiza o estado para o próximo estado
        state = next_state

    # Condição de parada: Se a média da recompensa dos últimos 10 episódios atingir 1
    if episode % 10 == 0:
        average_reward = sum(reward for _ in range(10)) / 10.0
        print(f'Episódio {episode}, Recompensa Média: {average_reward}')

        # Adicionando uma condição de parada
        if average_reward >= 1: # Pode ajustar esse valor conforme necessário
            print(f'Resolvido após {episode} episódios!')
            break