import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Cargar el dataset
df = pd.read_csv('movies.csv', encoding='latin1')


# Mostrar las primeras filas del dataset
print("\nPrimeras filas del dataset:")
print(df.head())

# Información general del dataset
print("\nInformación del dataset:")
print(df.info())

# Resumen estadístico de las variables numéricas
print("\nResumen estadístico de variables numéricas:")
print(df.describe())

# Contar valores nulos por columna
print("\nValores nulos por columna:")
print(df.isnull().sum())

# Visualizar valores nulos
def plot_missing_values(df):
    plt.figure(figsize=(12, 6))
    sns.heatmap(df.isnull(), cmap='viridis', cbar=False, yticklabels=False)
    plt.title('Mapa de valores nulos en el dataset')
    plt.show()

plot_missing_values(df)

# Resumen de variables categóricas
print("\nResumen de variables categóricas:")
categorical_cols = df.select_dtypes(include=['object']).columns
for col in categorical_cols:
    print(f"{col}: {df[col].nunique()} valores únicos")
