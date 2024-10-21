# Importiamo le librerie necessarie
import pandas as pd
import matplotlib.pyplot as plt
import geopandas as gpd
from geopy.distance import geodesic

# Step 1: Importare il dataset con Pandas
# Carichiamo il dataset delle temperature globali
data = pd.read_csv("./GlobalTemperatures.csv")

# Step 2: Esplorare i dati
# Visualizziamo le prime righe del dataset per avere un'idea del contenuto
print(data.head())

# Step 3: Pulizia del dataset
# Visualizzare il numero di valori mancanti per ciascuna colonna
print(data.isnull().sum())

# Rimuoviamo le righe con valori mancanti nelle colonne 'AverageTemperature' e 'AverageTemperatureUncertainty'
data_cleaned = data.dropna(subset=['AverageTemperature', 'AverageTemperatureUncertainty'])

# Convertire la colonna 'dt' in formato datetime 
data_cleaned['dt'] = pd.to_datetime(data_cleaned['dt'])

# Assicurati che le colonne Latitude e Longitude siano di tipo numerico
data_cleaned['Latitude'] = pd.to_numeric(data_cleaned['Latitude'], errors='coerce')
data_cleaned['Longitude'] = pd.to_numeric(data_cleaned['Longitude'], errors='coerce')

# Step 4: Filtriamo i dati dal 1750
data_filtered = data_cleaned[data_cleaned['dt'] >= '1750-01-01']

# Estraiamo l'anno dalla colonna 'dt'
data_filtered['Year'] = data_filtered['dt'].dt.year

# Step 5: Creiamo i periodi da 50 anni
# Creiamo una nuova colonna 'Period' per definire i periodi di 50 anni
data_filtered['Period'] = (data_filtered['Year'] // 50) * 50

# Calcoliamo la temperatura massima e minima per ogni città in ciascun periodo
temp_range_by_city_period = data_filtered.groupby(['City', 'Country', 'Period'])['AverageTemperature'].agg(['max', 'min']).reset_index()

# Calcoliamo l'intervallo di temperatura
temp_range_by_city_period['TemperatureRange'] = temp_range_by_city_period['max'] - temp_range_by_city_period['min']

# Step 6: Identificare le 3 città con i più ampi intervalli di temperatura per ogni periodo
top_cities_by_period = temp_range_by_city_period.sort_values(['Period', 'TemperatureRange'], ascending=[True, False]).groupby('Period').head(3)

# Visualizza le città con i più ampi intervalli di temperatura per ciascun periodo
print(top_cities_by_period[['Period', 'City', 'Country', 'TemperatureRange']])

# Se desideri anche visualizzarlo in un grafico
# Puoi usare un grafico a barre per ogni periodo
plt.figure(figsize=(14, 8))
for period in top_cities_by_period['Period'].unique():
    period_data = top_cities_by_period[top_cities_by_period['Period'] == period]
    plt.bar(period_data['City'] + ' (' + period.astype(str) + ')', period_data['TemperatureRange'], label=period)

plt.title('Top 3 Città con i Maggiori Temperature Range per Periodo di 50 Anni (1750 - Oggi)')
plt.xlabel('Città (Anno)')
plt.ylabel('Temperature Range (°C)')
plt.xticks(rotation=45)
plt.grid(True)
plt.legend()
plt.show()

# Step 5: Creiamo i periodi da 70 anni
# Creiamo una nuova colonna 'Period' per definire i periodi di 70 anni
data_filtered['Period'] = (data_filtered['Year'] // 70) * 70

# Calcoliamo la temperatura massima e minima per ogni città in ciascun periodo
temp_range_by_city_period = data_filtered.groupby(['City', 'Country', 'Period'])['AverageTemperature'].agg(['max', 'min']).reset_index()

# Calcoliamo l'intervallo di temperatura
temp_range_by_city_period['TemperatureRange'] = temp_range_by_city_period['max'] - temp_range_by_city_period['min']

# Step 6: Identificare le 3 città con i più ampi intervalli di temperatura per ogni periodo
top_cities_by_period = temp_range_by_city_period.sort_values(['Period', 'TemperatureRange'], ascending=[True, False]).groupby('Period').head(3)

# Visualizza le città con i più ampi intervalli di temperatura per ciascun periodo
print(top_cities_by_period[['Period', 'City', 'Country', 'TemperatureRange']])

# Se desideri anche visualizzarlo in un grafico
# Puoi usare un grafico a barre per ogni periodo
plt.figure(figsize=(14, 8))
for period in top_cities_by_period['Period'].unique():
    period_data = top_cities_by_period[top_cities_by_period['Period'] == period]
    plt.bar(period_data['City'] + ' (' + period.astype(str) + ')', period_data['TemperatureRange'], label=period)

plt.title('Top 3 Città con i Maggiori Temperature Range per Periodo di 70 Anni (1750 - Oggi)')
plt.xlabel('Città (Anno)')
plt.ylabel('Temperature Range (°C)')
plt.xticks(rotation=45)
plt.grid(True)
plt.legend()
plt.show()