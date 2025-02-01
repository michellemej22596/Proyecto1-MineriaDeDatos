import pandas as pd

# Cargar el archivo CSV con encoding 'latin1'
df = pd.read_csv('../movies.csv', encoding='latin1')

# Asegurar que las columnas necesarias existen (ajustar nombres si son diferentes)
if 'genres' not in df.columns or 'revenue' not in df.columns:
    raise ValueError("El CSV no contiene las columnas necesarias: genres, revenue")

# Separar los géneros en filas individuales
genre_revenue = df.assign(genres=df['genres'].str.split('|')).explode('genres')

# Sumar las ganancias por género
genre_revenue = genre_revenue.groupby('genres')['revenue'].sum()

# Obtener el género con mayores ganancias
most_profitable_genre = genre_revenue.idxmax()
most_profitable_revenue = genre_revenue.max()

# Imprimir resultado
print(f"El género con mayores ganancias es: {most_profitable_genre} con un total de ${most_profitable_revenue:,.2f}")
