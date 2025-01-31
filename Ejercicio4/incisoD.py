import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Cargar el dataset
df = pd.read_csv('../movies.csv', encoding='latin1')

# Obtener la peor película según los votos de los usuarios
print("\nPeor película según los votos de los usuarios:")
worst_rated_movie = df[['title', 'voteAvg']].sort_values(by='voteAvg', ascending=True).head(1)
print(worst_rated_movie)
