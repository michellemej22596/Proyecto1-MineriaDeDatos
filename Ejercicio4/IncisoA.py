import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Cargar el dataset
df = pd.read_csv('../movies.csv', encoding='latin1')

# Obtener las 10 películas con mayor presupuesto
print("\nLas 10 películas con mayor presupuesto:")
top_budget_movies = df[['title', 'budget']].sort_values(by='budget', ascending=False).head(10)
print(top_budget_movies)

# Gráfico de barras de las 10 películas con mayor presupuesto
plt.figure(figsize=(10, 6))
sns.barplot(data=top_budget_movies, x='budget', y='title', palette='viridis')
plt.xlabel("Presupuesto ($)")
plt.ylabel("Película")
plt.title("Top 10 películas con mayor presupuesto")
plt.gca().invert_yaxis()
plt.show()
