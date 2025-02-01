import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# Cargar el archivo CSV con encoding 'latin1'
df = pd.read_csv('../movies.csv', encoding='latin1')

# Asegurar que las columnas necesarias existen
if 'actorsAmount' not in df.columns or 'revenue' not in df.columns or 'releaseDate' not in df.columns:
    raise ValueError("El CSV no contiene las columnas necesarias: actorsAmount, revenue, releaseDate")

# Convertir releaseDate a tipo datetime
df['releaseDate'] = pd.to_datetime(df['releaseDate'], errors='coerce')
df['year'] = df['releaseDate'].dt.year

# Filtrar valores atípicos (descartar películas con más de 500 actores o ingresos negativos)
df = df[(df['actorsAmount'] > 0) & (df['actorsAmount'] <= 500) & (df['revenue'] > 0)]

# Análisis de correlación entre cantidad de actores e ingresos
correlation = df[['actorsAmount', 'revenue']].corr().iloc[0, 1]
print(f"Correlación entre la cantidad de actores y los ingresos: {correlation:.2f}")

# Graficar relación entre cantidad de actores e ingresos con escala logarítmica
plt.figure(figsize=(10, 6))
sns.scatterplot(x=df['actorsAmount'], y=np.log1p(df['revenue']), alpha=0.5)
plt.xlabel("Cantidad de Actores")
plt.ylabel("Log de Ingresos ($)")
plt.title("Relación entre Cantidad de Actores e Ingresos de Películas (Log)")
plt.show()

# Análisis de cantidad de actores en los últimos años
actors_per_year = df.groupby('year')['actorsAmount'].mean()

# Graficar evolución de la cantidad de actores en el tiempo
plt.figure(figsize=(10, 6))
actors_per_year.plot()
plt.xlabel("Año")
plt.ylabel("Cantidad Promedio de Actores")
plt.title("Evolución de la Cantidad de Actores en Películas por Año")
plt.show()
