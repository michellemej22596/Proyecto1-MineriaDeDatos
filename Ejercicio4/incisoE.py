import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Cargar el dataset
df = pd.read_csv('../movies.csv', encoding='latin1')

# Convertir la fecha de lanzamiento a tipo datetime
df['releaseDate'] = pd.to_datetime(df['releaseDate'], errors='coerce')
df['releaseYear'] = df['releaseDate'].dt.year

# Contar películas por año
movies_per_year = df['releaseYear'].value_counts().sort_index()

# Mostrar el año con más películas
max_year = movies_per_year.idxmax()
max_count = movies_per_year.max()
print(f"\nEl año con más películas fue {max_year} con {max_count} películas.")

# Gráfico de barras de cantidad de películas por año
plt.figure(figsize=(12, 6))
sns.barplot(x=movies_per_year.index, y=movies_per_year.values)
plt.xlabel("Año")
plt.ylabel("Cantidad de Películas")
plt.title("Cantidad de películas estrenadas por año")
plt.xticks(rotation=45)
plt.show()

