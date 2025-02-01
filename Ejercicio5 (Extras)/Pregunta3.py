import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Cargar el archivo CSV con encoding 'latin1'
df = pd.read_csv('../movies.csv', encoding='latin1')

# Asegurar que las columnas necesarias existen
if 'runtime' not in df.columns or 'voteAvg' not in df.columns:
    raise ValueError("El CSV no contiene las columnas necesarias: runtime, voteAvg")

# Convertir las columnas a valores numéricos
df['runtime'] = pd.to_numeric(df['runtime'], errors='coerce')
df['voteAvg'] = pd.to_numeric(df['voteAvg'], errors='coerce')

# Eliminar valores nulos o incorrectos
df = df.dropna(subset=['runtime', 'voteAvg'])
df = df[df['runtime'] > 0]  # Filtrar duraciones inválidas

# Calcular la correlación entre duración y calificación
correlation = df[['runtime', 'voteAvg']].corr().iloc[0, 1]
print(f"Correlación entre la duración de una película y su calificación promedio: {correlation:.2f}")

# Visualización con un gráfico de dispersión
plt.figure(figsize=(10, 6))
sns.scatterplot(x=df['runtime'], y=df['voteAvg'], alpha=0.5)
plt.xlabel("Duración de la película (minutos)")
plt.ylabel("Calificación Promedio")
plt.title("Relación entre la Duración de una Película y su Calificación Promedio")
plt.show()
