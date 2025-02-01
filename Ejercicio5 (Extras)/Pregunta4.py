import pandas as pd
import matplotlib.pyplot as plt

# Cargar el archivo CSV con encoding 'latin1'
df = pd.read_csv('../movies.csv', encoding='latin1')

# Asegurar que las columnas necesarias existen
if 'releaseDate' not in df.columns or 'revenue' not in df.columns:
    raise ValueError("El CSV no contiene las columnas necesarias: releaseDate, revenue")

# Convertir la fecha a formato datetime
df['releaseDate'] = pd.to_datetime(df['releaseDate'], errors='coerce')
df['year'] = df['releaseDate'].dt.year

# Convertir ingresos a numérico
df['revenue'] = pd.to_numeric(df['revenue'], errors='coerce')

# Eliminar valores nulos o incorrectos
df = df.dropna(subset=['year', 'revenue'])
df = df[df['revenue'] > 0]  # Filtrar ingresos inválidos

# Calcular los ingresos totales por año
yearly_revenue = df.groupby('year')['revenue'].sum()
mejor_anio = yearly_revenue.idxmax()
mayor_ganancia = yearly_revenue.max()

print(f"El año con mayor ganancia fue {mejor_anio} con un total de ${mayor_ganancia:,.2f}")

# Visualización con gráfico de líneas
plt.figure(figsize=(10, 5))
plt.plot(yearly_revenue.index, yearly_revenue.values, marker='o', linestyle='-', color='b')
plt.xlabel("Año")
plt.ylabel("Ingresos Totales ($)")
plt.title("Ingresos Totales por Año en la Industria del Cine")
plt.grid()
plt.show()
