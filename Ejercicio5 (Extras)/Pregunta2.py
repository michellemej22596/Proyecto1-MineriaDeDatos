import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Cargar el dataset
df = pd.read_csv('../movies.csv', encoding='latin1')

common_language = df['originalLanguage'].value_counts().head(1)
print("\nIdioma más común en las películas:")
print(common_language)
