import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Cargar el dataset
df = pd.read_csv('../movies.csv', encoding='latin1')

df = df[df['budget'] > 0]  # Filtrar presupuestos mayores a cero
df['roi'] = df['revenue'] / df['budget']
most_profitable_movie = df[['title', 'roi']].sort_values(by='roi', ascending=False).head(1)
print("\nPelícula con mayor retorno de inversión (ROI):")
print(most_profitable_movie)

