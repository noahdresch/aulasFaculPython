import matplotlib.pyplot as plt
import random

dados1 = random.sample(range(100), k=20)
dados2 = random.sample(range(100), k=20)

print(dados1)
print(dados2)

plt.bar(dados1,dados2)