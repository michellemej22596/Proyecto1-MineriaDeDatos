import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Cargar el dataset
df = pd.read_csv('../movies.csv', encoding='latin1')

# Obtener las 10 películas con mayores ingresos
print("\nLas 10 películas con mayores ingresos:")
top_revenue_movies = df[['title', 'revenue']].sort_values(by='revenue', ascending=False).head(10)
print(top_revenue_movies)

# Gráfico de barras de las 10 películas con mayores ingresos
plt.figure(figsize=(10, 6))
sns.barplot(data=top_revenue_movies, x='revenue', y='title', palette='magma')
plt.xlabel("Ingresos ($)")
plt.ylabel("Película")
plt.title("Top 10 películas con mayores ingresos")
plt.gca().invert_yaxis()  # Invertir eje para mejor visualización
plt.show()
