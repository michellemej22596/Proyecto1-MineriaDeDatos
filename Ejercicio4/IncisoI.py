import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# Cargar el archivo CSV con encoding 'latin1'
df = pd.read_csv('../movies.csv', encoding='latin1')

# Asegurar que las columnas necesarias existen
required_columns = ['castWomenAmount', 'castMenAmount', 'revenue', 'popularity']
for col in required_columns:
    if col not in df.columns:
        raise ValueError(f"El CSV no contiene la columna necesaria: {col}")

# Convertir las columnas de cantidad de actores a tipo numérico
df[required_columns] = df[required_columns].apply(pd.to_numeric, errors='coerce')

# Eliminar filas con valores NaN en las columnas relevantes
df = df.dropna(subset=['castWomenAmount', 'castMenAmount', 'revenue', 'popularity'])

# Calcular la proporción de mujeres y hombres en el reparto evitando divisiones por cero
df['total_cast'] = df['castWomenAmount'] + df['castMenAmount']
df = df[df['total_cast'] > 0]
df['women_ratio'] = df['castWomenAmount'] / df['total_cast']
df['men_ratio'] = df['castMenAmount'] / df['total_cast']

# Análisis de correlación
correlations = df[['women_ratio', 'men_ratio', 'revenue', 'popularity']].corr()
print(f"Correlación entre la proporción de mujeres en el reparto y los ingresos: {correlations.loc['women_ratio', 'revenue']:.2f}")
print(f"Correlación entre la proporción de mujeres en el reparto y la popularidad: {correlations.loc['women_ratio', 'popularity']:.2f}")
print(f"Correlación entre la proporción de hombres en el reparto y los ingresos: {correlations.loc['men_ratio', 'revenue']:.2f}")
print(f"Correlación entre la proporción de hombres en el reparto y la popularidad: {correlations.loc['men_ratio', 'popularity']:.2f}")

# Gráfica de dispersión para ingresos y popularidad por proporción de mujeres
fig, axes = plt.subplots(1, 2, figsize=(14, 6))
sns.scatterplot(ax=axes[0], x=df['women_ratio'], y=np.log1p(df['revenue']), alpha=0.5)
axes[0].set_xlabel("Proporción de Mujeres en el Reparto")
axes[0].set_ylabel("Log de Ingresos ($)")
axes[0].set_title("Mujeres en el Reparto vs Ingresos")

sns.scatterplot(ax=axes[1], x=df['women_ratio'], y=df['popularity'], alpha=0.5)
axes[1].set_xlabel("Proporción de Mujeres en el Reparto")
axes[1].set_ylabel("Popularidad")
axes[1].set_title("Mujeres en el Reparto vs Popularidad")
plt.show()

# Gráfica de dispersión para ingresos y popularidad por proporción de hombres
fig, axes = plt.subplots(1, 2, figsize=(14, 6))
sns.scatterplot(ax=axes[0], x=df['men_ratio'], y=np.log1p(df['revenue']), alpha=0.5)
axes[0].set_xlabel("Proporción de Hombres en el Reparto")
axes[0].set_ylabel("Log de Ingresos ($)")
axes[0].set_title("Hombres en el Reparto vs Ingresos")

sns.scatterplot(ax=axes[1], x=df['men_ratio'], y=df['popularity'], alpha=0.5)
axes[1].set_xlabel("Proporción de Hombres en el Reparto")
axes[1].set_ylabel("Popularidad")
axes[1].set_title("Hombres en el Reparto vs Popularidad")
plt.show()
