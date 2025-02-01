import pandas as pd

# Cargar el archivo CSV con encoding 'latin1'
df = pd.read_csv('../movies.csv', encoding='latin1')

# Asegurar que las columnas necesarias existen
if 'director' not in df.columns or 'voteAvg' not in df.columns or 'voteCount' not in df.columns:
    raise ValueError("El CSV no contiene las columnas necesarias: director, voteAvg, voteCount")

# Convertir la columna de calificación a numérico
df['voteAvg'] = pd.to_numeric(df['voteAvg'], errors='coerce')
df['voteCount'] = pd.to_numeric(df['voteCount'], errors='coerce')

# Filtrar datos no válidos y asegurar un número mínimo de votos para evitar sesgos
df = df.dropna(subset=['director', 'voteAvg', 'voteCount'])
df = df[df['voteCount'] > 50]  # Solo considerar películas con más de 50 votos

# Obtener las 20 películas mejor calificadas con un número significativo de votos
top_movies = df.sort_values(by=['voteAvg', 'voteCount'], ascending=[False, False]).head(20)

# Obtener los directores de estas películas
top_directors = top_movies[['director', 'voteAvg', 'title']]

# Imprimir resultados
print("Directores de las 20 películas mejor calificadas:")
print(top_directors.to_string(index=False))
