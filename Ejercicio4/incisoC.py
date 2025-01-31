import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Cargar el dataset
df = pd.read_csv('../movies.csv', encoding='latin1')

# Obtener la película con más votos
print("\nPelícula con más votos:")
top_voted_movie = df[['title', 'voteCount']].sort_values(by='voteCount', ascending=False).head(1)
print(top_voted_movie)
