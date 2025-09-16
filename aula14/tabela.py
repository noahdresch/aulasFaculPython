import seaborn as sns
import matplotlib.pyplot as plt

sns.set(style="whitegrid")  # opções: darkgrid, whitegrid, dark, white, ticks

df_tips = sns.load_dataset("tips")
print(df_tips)