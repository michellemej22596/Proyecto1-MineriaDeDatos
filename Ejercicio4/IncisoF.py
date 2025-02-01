import pandas as pd
import matplotlib.pyplot as plt

# Cargar el archivo CSV con encoding 'latin1'
df = pd.read_csv('../movies.csv', encoding='latin1')

# Verificar las columnas disponibles
print(df.columns)

# Asegurar que las columnas necesarias existen (ajustar nombres si son diferentes)
if 'releaseDate' not in df.columns or 'genres' not in df.columns or 'runtime' not in df.columns:
    raise ValueError("El CSV no contiene las columnas necesarias: releaseDate, genres, runtime")

# Convertir releaseDate a tipo datetime
df['releaseDate'] = pd.to_datetime(df['releaseDate'], errors='coerce')

# Obtener las 20 películas más recientes
recent_movies = df.sort_values(by='releaseDate', ascending=False).head(20)
most_common_genre_recent = recent_movies.assign(genres=recent_movies['genres'].str.split('|')).explode('genres')['genres'].mode()[0]

# Obtener el género predominante en todo el conjunto de datos
most_common_genre_overall = df.assign(genres=df['genres'].str.split('|')).explode('genres')['genres'].mode()[0]

# Obtener el género de las películas más largas
longest_movies = df.sort_values(by='runtime', ascending=False).head(10)
most_common_genre_longest = longest_movies.assign(genres=longest_movies['genres'].str.split('|')).explode('genres')['genres'].mode()[0]

# Separar los géneros en filas individuales
genres_expanded = df.assign(genres=df['genres'].str.split('|')).explode('genres')

# Graficar la distribución de géneros en todo el dataset
plt.figure(figsize=(12, 6))
genres_expanded['genres'].value_counts().plot(kind='bar', color='skyblue', edgecolor='black')
plt.xlabel("Género")
plt.ylabel("Cantidad de películas")
plt.title("Distribución de Géneros en el Dataset")
plt.xticks(rotation=45)
plt.show()

# Imprimir resultados
print(f"Género principal de las 20 películas más recientes: {most_common_genre_recent}")
print(f"Género que predomina en el conjunto de datos: {most_common_genre_overall}")
print(f"Género principal de las películas más largas: {most_common_genre_longest}")
